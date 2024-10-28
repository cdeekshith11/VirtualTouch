import cv2
import mediapipe as mp
import numpy as np
import pyautogui
from pynput.mouse import Button, Controller
import threading
import queue
import random

# Initialize the mouse controller
mouse = Controller()
screen_width, screen_height = pyautogui.size()

# Initialize MediaPipe Hands
mpHands = mp.solutions.hands
hands = mpHands.Hands(
    static_image_mode=False,
    model_complexity=1,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7,
    max_num_hands=1
)

# Previous mouse positions for smoothing
prev_x, prev_y = None, None

# Queue for video frames
frame_queue = queue.Queue(maxsize=10)

# Function to find the index and middle finger tips
def find_finger_tips(processed):
    if processed.multi_hand_landmarks:
        hand_landmarks = processed.multi_hand_landmarks[0]
        index_finger_tip = hand_landmarks.landmark[mpHands.HandLandmark.INDEX_FINGER_TIP]
        middle_finger_tip = hand_landmarks.landmark[mpHands.HandLandmark.MIDDLE_FINGER_TIP]
        return index_finger_tip, middle_finger_tip
    return None, None

# Function to move the mouse based on the midpoint of index and middle finger tips with smoothing
def move_mouse(index_finger_tip, middle_finger_tip):
    global prev_x, prev_y
    if index_finger_tip is not None and middle_finger_tip is not None:
        x1, y1 = int(index_finger_tip.x * screen_width), int(index_finger_tip.y * screen_height)
        x2, y2 = int(middle_finger_tip.x * screen_width), int(middle_finger_tip.y * screen_height)

        # Calculate the midpoint
        x = int((x1 + x2) / 2)
        y = int((y1 + y2) / 2)

        # Smoothing the mouse movement by averaging
        if prev_x is not None and prev_y is not None:
            x = int((prev_x + x) / 2)
            y = int((prev_y + y) / 2)

        # Ensure coordinates are within screen bounds
        x = min(max(x, 0), screen_width - 1)
        y = min(max(y, 0), screen_height - 1)

        pyautogui.moveTo(x, y)
        print(f"Mouse moved to ({x}, {y})")

        prev_x, prev_y = x, y

def get_distance(landmark_list):
    """
    Calculate the normalized distance between the first two points in landmark_list.
    Normalize the distance to a range of [0, 1000].
    """
    if len(landmark_list) < 2:
        raise ValueError("landmark_list must contain at least two points")

    (x1, y1), (x2, y2) = landmark_list[0], landmark_list[1]
    L = np.hypot(x2 - x1, y2 - y1)
    return np.interp(L, [0, 1], [0, 1000])  # Normalize to 1000 for better control

def get_angle(a, b, c):
    radians = np.arctan2(c[1] - b[1], c[0] - b[0]) - np.arctan2(a[1] - b[1], a[0] - b[0])
    angle = np.abs(np.degrees(radians))
    return min(angle, 360 - angle)

def is_left_click(landmarks_list, thumb_index_dist):
    angle1 = get_angle(landmarks_list[5], landmarks_list[6], landmarks_list[8])
    angle2 = get_angle(landmarks_list[9], landmarks_list[10], landmarks_list[12])
    return (angle1 < 50 and angle2 > 90 and thumb_index_dist > 50)

def is_right_click(landmarks_list, thumb_index_dist):
    angle1 = get_angle(landmarks_list[9], landmarks_list[10], landmarks_list[12])
    angle2 = get_angle(landmarks_list[5], landmarks_list[6], landmarks_list[8])
    return (angle1 < 50 and angle2 > 90 and thumb_index_dist > 50)

def is_double_click(landmarks_list, thumb_index_dist):
    angle1 = get_angle(landmarks_list[5], landmarks_list[6], landmarks_list[8])
    angle2 = get_angle(landmarks_list[9], landmarks_list[10], landmarks_list[12])
    return (angle1 < 50 and angle2 < 50 and thumb_index_dist > 50)

def is_screenshot(landmarks_list, thumb_index_dist):
    angle1 = get_angle(landmarks_list[5], landmarks_list[6], landmarks_list[8])
    angle2 = get_angle(landmarks_list[9], landmarks_list[10], landmarks_list[12])
    return (angle1 < 50 and angle2 < 50 and thumb_index_dist < 50)

# Function to detect gestures and perform actions
def detect_gestures(frame, landmarks_list, processed):
    if len(landmarks_list) >= 21:
        index_finger_tip, middle_finger_tip = find_finger_tips(processed)
        thumb_index_dist = get_distance([landmarks_list[4], landmarks_list[5]])

        if thumb_index_dist < 50 and get_angle(landmarks_list[5], landmarks_list[6], landmarks_list[8]) > 90:
            move_mouse(index_finger_tip, middle_finger_tip)

        if is_left_click(landmarks_list, thumb_index_dist):
            print("Left Click Detected!")
            mouse.press(Button.left)
            mouse.release(Button.left)
            cv2.putText(frame, "Left Click", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

        elif is_right_click(landmarks_list, thumb_index_dist):
            print("Right Click Detected!")
            mouse.press(Button.right)
            mouse.release(Button.right)
            cv2.putText(frame, "Right Click", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

        elif is_double_click(landmarks_list, thumb_index_dist):
            print("Double Click Detected!")
            pyautogui.doubleClick()
            cv2.putText(frame, "Double Click", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 0), 2)

        elif is_screenshot(landmarks_list, thumb_index_dist):
            print("Screenshot Detected!")
            im1 = pyautogui.screenshot()
            label = random.randint(1, 1000)
            im1.save(f'my_screenshot_{label}.png')
            cv2.putText(frame, "Screenshot Taken", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 0), 2)

def video_capture_thread():
    cap = cv2.VideoCapture(0)
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        frame = cv2.flip(frame, 1)
        if frame_queue.qsize() < 10:
            frame_queue.put(frame)
    cap.release()

def gesture_processing_thread():
    draw = mp.solutions.drawing_utils
    while True:
        if not frame_queue.empty():
            frame = frame_queue.get()
            frameRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            processed = hands.process(frameRGB)

            landmarks_list = []
            if processed.multi_hand_landmarks:
                hand_landmarks = processed.multi_hand_landmarks[0]
                draw.draw_landmarks(frame, hand_landmarks, mpHands.HAND_CONNECTIONS)

                for lm in hand_landmarks.landmark:
                    landmarks_list.append((lm.x, lm.y))

            detect_gestures(frame, landmarks_list, processed)

            cv2.imshow('Frame', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
    cv2.destroyAllWindows()

# Main function to run the application
def main():
    capture_thread = threading.Thread(target=video_capture_thread, daemon=True)
    processing_thread = threading.Thread(target=gesture_processing_thread, daemon=True)

    capture_thread.start()
    processing_thread.start()

    capture_thread.join()
    processing_thread.join()

if __name__ == '__main__':
    main()
