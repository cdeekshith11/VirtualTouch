# # # # import streamlit as st
# # # # import cv2 as cv
# # # # import numpy as np
# # # # import imutils
# # # # import json
# # # # import pyautogui
# # # # from streamlit_webrtc import webrtc_streamer, VideoTransformerBase

# # # # # Define the keyboard layout and coordinates, similar to your initial setup
# # # # nums = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
# # # # row1 = ["Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P"]
# # # # row2 = ["A", "S", "D", "F", "G", "H", "J", "K", "L"]
# # # # row3 = ["Z", "X", "C", "V", "B", "N", "M"]
# # # # row4 = ["space", "enter", "backspace", "shift"]
# # # # row5 = ["left", "up", "down", "right"]
# # # # row6 = ["volumeup", "volumedown", "volumemute"]
# # # # arr = []

# # # # # Add your keyboard configuration logic here
# # # # def setup_keyboard():
# # # #     x = 10
# # # #     y = 20
# # # #     # Similar logic as your provided code
# # # #     for i in range(0, 10):
# # # #         arr.append({"x": x, "y": y, "w": 100, "h": 80, "value": nums[i]})
# # # #         x = x + 100
# # # #     # Calculate the positions of other keys similarly...
# # # #     # Omitted for brevity, please populate arr like before

# # # # setup_keyboard()
# # # # json_data = json.loads(json.dumps(arr))

# # # # class VideoProcessor(VideoTransformerBase):
# # # #     def transform(self, frame):
# # # #         img = frame.to_ndarray(format="bgr24")
        
# # # #         # Add your OpenCV processing logic here
# # # #         # This is where you transform the frame according to the logic above
        
# # # #         # Flip the frame horizontally
# # # #         img = cv.flip(img, 1)
# # # #         img = cv.GaussianBlur(img, (5, 5), 0)
# # # #         img = imutils.resize(img, width=1030, height=700)
# # # #         height, width = img.shape[:2]
      
# # # #         # Drawing keyboard interface (Similar logic as your provided code)
# # # #         # Your drawing code here...
      
# # # #         # Detect hand and simulate key press
# # # #         hsv_img = cv.cvtColor(img, cv.COLOR_BGR2HSV)
# # # #         mask = cv.inRange(hsv_img, np.array([65, 60, 60]), np.array([80, 255, 255]))
# # # #         mask_open = cv.morphologyEx(mask, cv.MORPH_OPEN, np.ones((5, 5)))
# # # #         mask_close = cv.morphologyEx(mask_open, cv.MORPH_CLOSE, np.ones((20, 20)))
# # # #         mask_final = mask_close
# # # #         conts, _ = cv.findContours(mask_final.copy(), cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
        
# # # #         if len(conts) == 1:
# # # #             x, y, w, h = cv.boundingRect(conts[0])
# # # #             cx = round(x + w / 2)
# # # #             cy = round(y + h / 2)
# # # #             cv.circle(img, (cx, cy), 20, (0, 0, 255), 2)
# # # #             word = ""
# # # #             for i in range(len(json_data)):
# # # #                 if cx >= int(json_data[i]["x"]) and cx <= int(json_data[i]["x"]) + int(json_data[i]["w"]) and cy >= int(json_data[i]["y"]) and cy <= int(json_data[i]["y"]) + int(json_data[i]["h"]):
# # # #                     word = json_data[i]["value"]
# # # #             pyautogui.press(word)

# # # #         return img

# # # # st.title("Virtual Keyboard App")
# # # # st.text("Press ESC to stop the camera")

# # # # webrtc_streamer(key="keyboard-app", video_processor_factory=VideoProcessor)

# # # import streamlit as st
# # # import cv2 as cv
# # # import numpy as np
# # # import imutils
# # # import json
# # # import pyautogui
# # # from streamlit_webrtc import webrtc_streamer, VideoTransformerBase

# # # # Set up the keyboard configuration
# # # def setup_keyboard():
# # #     global arr
# # #     x = 10
# # #     y = 20
# # #     for i in range(0, 10):
# # #         arr.append({"x": x, "y": y, "w": 100, "h": 80, "value": nums[i]})
# # #         x += 100
# # #     # Set up for each row positions and widths
# # #     # Populate arr for row1, row2, row3, row4, row5, row6 similarly
# # #     ...

# # # setup_keyboard()
# # # json_data = json.loads(json.dumps(arr))

# # # class VideoProcessor(VideoTransformerBase):
# # #     def transform(self, frame):
# # #         img = frame.to_ndarray(format="bgr24")
# # #         img = cv.flip(img, 1)
# # #         img = cv.GaussianBlur(img, (5, 5), 0)
# # #         img = imutils.resize(img, width=1030, height=700)
        
# # #         # Draw keyboard layout
# # #         # Assuming keyboard drawing logic is similar to your previous OpenCV drawing
# # #         # Draw each key as a rectangle with corresponding label

# # #         # Process frame for hand detection and simulate key press
# # #         hsv_img = cv.cvtColor(img, cv.COLOR_BGR2HSV)
# # #         mask = cv.inRange(hsv_img, np.array([65, 60, 60]), np.array([80, 255, 255]))
# # #         mask_open = cv.morphologyEx(mask, cv.MORPH_OPEN, np.ones((5, 5)))
# # #         mask_close = cv.morphologyEx(mask_open, cv.MORPH_CLOSE, np.ones((20, 20)))
# # #         mask_final = mask_close
# # #         conts, _ = cv.findContours(mask_final.copy(), cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
        
# # #         if len(conts) == 1:
# # #             x, y, w, h = cv.boundingRect(conts[0])
# # #             cx = round(x + w / 2)
# # #             cy = round(y + h / 2)
# # #             cv.circle(img, (cx, cy), 20, (0, 0, 255), 2)
# # #             word = ""
# # #             for key in json_data:
# # #                 if cx >= int(key["x"]) and cx <= int(key["x"]) + int(key["w"]) and cy >= int(key["y"]) and cy <= int(key["y"]) + int(key["h"]):
# # #                     word = key["value"]
# # #                     break
# # #             if word:
# # #                 pyautogui.press(word)  # Ensure this operates safely

# # #         return img

# # # st.title("Virtual Keyboard App")
# # # st.text("Control using hand gestures and see keyboard input reflected in real-time")

# # # webrtc_streamer(key="keyboard-app", video_processor_factory=VideoProcessor)

# # import streamlit as st
# # import cv2 as cv
# # import numpy as np
# # import json
# # import imutils
# # from PIL import Image
# # import pyautogui

# # # Simulated video processing function
# # def process_frame(frame, json_data):
# #     frame = cv.flip(frame, 1)
# #     frame = cv.GaussianBlur(frame, (5, 5), 0)
# #     frame = imutils.resize(frame, width=1030, height=700)
    
# #     nums = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
# #     row1 = ["Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P"]
# #     row2 = ["A", "S", "D", "F", "G", "H", "J", "K", "L"]
# #     row3 = ["Z", "X", "C", "V", "B", "N", "M"]
# #     row4 = ["space", "enter", "backspace", "shift"]
# #     row5 = ["left", "up", "down", "right"]
# #     row6 = ["volumeup", "volumedown", "volumemute"]
    
# #     # Drawing rectangles and putting text - transformed for PIL
# #     x = 10
# #     y = 20
# #     for i in range(0, 10):
# #         cv.rectangle(frame, (x, y), (x + 100, y + 80), (0, 255, 255), 2)
# #         cv.putText(frame, nums[i], (x + 50, y + 40), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv.LINE_AA)
# #         x = x + 100
# #     y = 100
# #     x = 10
# #     for i in range(0, 10):
# #         cv.rectangle(frame, (x, y), (x + 100, y + 80), (0, 255, 255), 2)
# #         cv.putText(frame, row1[i], (x + 50, y + 40), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv.LINE_AA)
# #         x = x + 100
# #     x = 110
# #     y = 180
# #     for i in range(0, 9):
# #         cv.rectangle(frame, (x, y), (x + 100, y + 80), (0, 255, 255), 2)
# #         cv.putText(frame, row2[i], (x + 50, y + 40), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv.LINE_AA)
# #         x = x + 100

# #     x = 210
# #     y = 260
    
# #     for i in range(0, 7):
        
# #         cv.rectangle(frame, (x, y), (x + 100, y + 80), (0, 255, 255), 2)
# #         cv.putText(frame, row3[i], (x + 50, y + 40), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv.LINE_AA)
# #         x = x + 100
# #     x = 110
# #     y = 340
# #     cv.rectangle(frame, (x, y), (x + 200, y + 80), (0, 255, 255), 2)
# #     cv.putText(frame, row4[0], (x + 70, y + 40), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv.LINE_AA)
# #     x = 310
# #     y = 340
# #     cv.rectangle(frame, (x, y), (x + 200, y + 80), (0, 255, 255), 2)
# #     cv.putText(frame, row4[1], (x + 70, y + 40), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv.LINE_AA)
# #     x = 510
# #     y = 340
# #     cv.rectangle(frame, (x, y), (x + 250, y + 80), (0, 255, 255), 2)
# #     cv.putText(frame, row4[2], (x + 70, y + 40), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv.LINE_AA)
# #     x = 760
# #     y = 340
# #     cv.rectangle(frame, (x, y), (x + 200, y + 80), (0, 255, 255), 2)
# #     cv.putText(frame, row4[3], (x + 70, y + 40), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv.LINE_AA)
# #     x = 110
# #     y = 420
# #     cv.rectangle(frame, (x, y), (x + 200, y + 80), (0, 255, 255), 2)
# #     cv.putText(frame, row5[0], (x + 100, y + 40), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv.LINE_AA)
# #     x = 310
# #     y = 420
# #     cv.rectangle(frame, (x, y), (x + 200, y + 80), (0, 255, 255), 2)
# #     cv.putText(frame, row5[1], (x + 100, y + 40), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv.LINE_AA)
# #     x = 510
# #     y = 420
# #     cv.rectangle(frame, (x, y), (x + 200, y + 80), (0, 255, 255), 2)
# #     cv.putText(frame, row5[2], (x + 100, y + 40), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv.LINE_AA)
# #     x = 710
# #     y = 420
# #     cv.rectangle(frame, (x, y), (x + 200, y + 80), (0, 255, 255), 2)
# #     cv.putText(frame, row5[3], (x + 100, y + 40), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv.LINE_AA)
# #     x = 10
# #     y = 500
# #     cv.rectangle(frame, (x, y), (x + 200, y + 80), (0, 255, 255), 2)
# #     cv.putText(frame, "V+", (x + 60, y + 40), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv.LINE_AA)
# #     x = 210
# #     y = 500
# #     cv.rectangle(frame, (x, y), (x + 200, y + 80), (0, 255, 255), 2)
# #     cv.putText(frame, "V-", (x + 60, y + 40), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv.LINE_AA)
# #     x = 410
# #     y = 500
# #     cv.rectangle(frame, (x, y), (x + 200, y + 80), (0, 255, 255), 2)
# #     cv.putText(frame, "Vmute", (x + 60, y + 40), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv.LINE_AA)
    
# #     # Convert BGR frame to RGB for display in Streamlit
# #     frame = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
# #     return frame

# # # JSON data preparation
# # arr = []
# # # Fill in JSON data browsing...  # This section remains the same as in original code
# # # [Your code to construct 'arr' Assuming that your original code for filling 'arr' is in place...
# # # Convert arr to JSON string
# # json_string = json.dumps(arr)
# # json_data = json.loads(json_string)

# # # Create a Streamlit app
# # def main():
# #     # Initialize camera
# #     cam = cv.VideoCapture(0)
    
# #     st.title("OpenCV Streamlit App")
# #     st.text("Press 'q' to quit or close the window")

# #     frame_placeholder = st.empty()  # Placeholder for displaying frames

# #     while True:
# #         ret, frame = cam.read()
# #         if not ret:
# #             st.error("Failed to grab frame")
# #             break

# #         # Process and display the frame
# #         processed_frame = process_frame(frame, json_data)
# #         img_pil = Image.fromarray(processed_frame)

# #         # Update the frame display
# #         frame_placeholder.image(img_pil, use_column_width=True)
        
# #         # Add a stop condition using Streamlit's button or keyboard interrupt
# #         # if st.button('Stop'):
# #         #     break

# #     cam.release()

# # if __name__ == "__main__":
# #     main()

# import cv2 as cv
# import numpy as np
# import json
# import pyautogui
# import streamlit as st
# from streamlit_webrtc import webrtc_streamer, VideoTransformerBase

# # Function to create keyboard layout as JSON data
# def create_keyboard_layout():
#     arr = []
#     nums = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
#     row1 = ["Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P"]
#     row2 = ["A", "S", "D", "F", "G", "H", "J", "K", "L"]
#     row3 = ["Z", "X", "C", "V", "B", "N", "M"]
#     row4 = ["space", "enter", "backspace", "shift"]
#     row5 = ["left", "up", "down", "right"]
#     row6 = ["volumeup", "volumedown", "volumemute"]

#     x, y = 10, 20
#     for i in range(0, 10):
#         arr.append({"x": x, "y": y, "w": 100, "h": 80, "value": nums[i]})
#         x = x + 100
#     y, x = 100, 10
#     for i in range(0, 10):
#         arr.append({"x": x, "y": y, "w": 100, "h": 80, "value": row1[i]})
#         x = x + 100
#     x, y = 110, 180
#     for i in range(0, 9):
#         arr.append({"x": x, "y": y, "w": 100, "h": 80, "value": row2[i]})
#         x = x + 100
#     x, y = 210, 260
#     for i in range(0, 7):
#         arr.append({"x": x, "y": y, "w": 100, "h": 80, "value": row3[i]})
#         x = x + 100
#     x, y = 110, 340
#     for i in range(len(row4)):
#         w = 200 if row4[i] != "backspace" else 250
#         arr.append({"x": x, "y": y, "w": w, "h": 80, "value": row4[i]})
#         x = x + (w - 50) if i == 2 else x + 200
#     x, y = 110, 420
#     for i in range(len(row5)):
#         arr.append({"x": x + (i * 200), "y": y, "w": 200, "h": 80, "value": row5[i]})
#     x, y = 10, 500
#     for i in range(len(row6)):
#         arr.append({"x": x + (i * 200), "y": y, "w": 200, "h": 80, "value": row6[i]})
    
#     return arr

# json_data = create_keyboard_layout()

# class VirtualKeyboard(VideoTransformerBase):
#     def __init__(self):
#         self.json_data = json_data
    
#     def transform(self, frame):
#         img = frame.to_ndarray(format="bgr24")

#         # Flip, blur and resize the frame
#         img = cv.flip(img, 1)
#         img = cv.GaussianBlur(img, (5, 5), 0)
#         img = cv.resize(img, (1030, 700))

#         # Draw the keyboard
#         self.draw_keyboard(img)

#         # Color detection for gesture and key press detection
#         self.detect_key_press(img)

#         return img

#     def draw_keyboard(self, img):
#         for key_data in self.json_data:
#             x, y, w, h, value = (key_data["x"], key_data["y"], key_data["w"], key_data["h"], key_data["value"])
#             cv.rectangle(img, (x, y), (x + w, y + h), (0, 255, 255), 2)
#             cv.putText(img, value, (x + 50, y + 40), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv.LINE_AA)

#     def detect_key_press(self, img):
#         hsv_img = cv.cvtColor(img, cv.COLOR_BGR2HSV)
#         mask = cv.inRange(hsv_img, np.array([65, 60, 60]), np.array([80, 255, 255]))
#         mask_open = cv.morphologyEx(mask, cv.MORPH_OPEN, np.ones((5, 5)))
#         mask_close = cv.morphologyEx(mask_open, cv.MORPH_CLOSE, np.ones((20, 20)))
#         conts, _ = cv.findContours(mask_close.copy(), cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

#         if conts:
#             x, y, w, h = cv.boundingRect(conts[0])
#             cx = round(x + w / 2)
#             cy = round(y + h / 2)
#             cv.circle(img, (cx, cy), 20, (0, 0, 255), 2)
#             word = self.get_key_at_position(cx, cy)
#             if word:
#                 pyautogui.press(word)
    
#     def get_key_at_position(self, cx, cy):
#         for key_data in self.json_data:
#             if (key_data['x'] <= cx <= key_data['x'] + key_data['w']) and (key_data['y'] <= cy <= key_data['y'] + key_data['h']):
#                 return key_data['value']
#         return None

# def main():
#     st.title("Virtual Keyboard using Gestures")
#     st.write("Control the virtual keyboard by pointing with a specific colored object.")

#     webrtc_streamer(key="virtual_keyboard", video_transformer_factory=VirtualKeyboard, media_stream_constraints={"video": True, "audio": False})

# if __name__ == "__main__":
#     main()
import cv2 as cv
import numpy as np
import imutils
import json
import pyautogui
import streamlit as st
import uuid

def main():
    st.title("Virtual Keyboard using Webcam")
    start = st.button("Start Virtual Keyboard")

    if start:
        cam = cv.VideoCapture(0)
        arr = []
        nums = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
        row1 = ["Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P"]
        row2 = ["A", "S", "D", "F", "G", "H", "J", "K", "L"]
        row3 = ["Z", "X", "C", "V", "B", "N", "M"]
        row4 = ["space", "enter", "backspace", "shift"]
        row5 = ["left", "up", "down", "right"]
        row6 = ["volumeup", "volumedown", "volumemute"]
        x = 10
        y = 20

        for i in range(0, 10):
            data = {}
            data["x"] = x
            data["y"] = y
            data["w"] = 100
            data["h"] = 80
            data["value"] = nums[i]
            arr.append(data)
            x = x + 100
        y = 100
        x = 10
        for i in range(0, 10):
            data = {}
            data["x"] = x
            data["y"] = y
            data["w"] = 100
            data["h"] = 80
            data["value"] = row1[i]
            arr.append(data)
            x = x + 100
        x = 110
        y = 180
        for i in range(0, 9):
            data = {}
            data["x"] = x
            data["y"] = y
            data["w"] = 100
            data["h"] = 80
            data["value"] = row2[i]
            arr.append(data)
            x = x + 100
        x = 210
        y = 260
        for i in range(0, 7):
            data = {}
            data["x"] = x
            data["y"] = y
            data["w"] = 100
            data["h"] = 80
            data["value"] = row3[i]
            arr.append(data)
            x = x + 100
        x = 110
        y = 340
        data = {}
        data["x"] = x
        data["y"] = y
        data["w"] = 200
        data["h"] = 80
        data["value"] = row4[0]
        arr.append(data)
        data = {}
        data["x"] = 310
        data["y"] = y
        data["w"] = 200
        data["h"] = 80
        data["value"] = row4[1]
        arr.append(data)
        data = {}
        data["x"] = 510
        data["y"] = 340
        data["w"] = 250
        data["h"] = 80
        data["value"] = row4[2]
        arr.append(data)
        data = {}
        data["x"] = 760
        data["y"] = 340
        data["w"] = 200
        data["h"] = 80
        data["value"] = row4[3]
        arr.append(data)
        x = 110
        y = 420
        data = {}
        data["x"] = x
        data["y"] = y
        data["w"] = 200
        data["h"] = 80
        data["value"] = row5[0]
        arr.append(data)
        data = {}
        data["x"] = 310
        data["y"] = y
        data["w"] = 200
        data["h"] = 80
        data["value"] = row5[1]
        arr.append(data)
        data = {}
        data["x"] = 510
        data["y"] = y
        data["w"] = 200
        data["h"] = 80
        data["value"] = row5[2]
        arr.append(data)
        data = {}
        data["x"] = 710
        data["y"] = y
        data["w"] = 200
        data["h"] = 80
        data["value"] = row5[3]
        arr.append(data)
        x = 10
        y = 500
        data = {}
        data["x"] = x
        data["y"] = y
        data["w"] = 200
        data["h"] = 80
        data["value"] = row6[0]
        arr.append(data)
        data = {}
        data["x"] = 210
        data["y"] = y
        data["w"] = 200
        data["h"] = 80
        data["value"] = row6[1]
        arr.append(data)
        data = {}
        data["x"] = 410
        data["y"] = y
        data["w"] = 200
        data["h"] = 80
        data["value"] = row6[2]
        arr.append(data)

        json_string = json.dumps(arr)
        json_data = json.loads(json_string)

        stframe = st.empty()

        stop_key = 'stop_key'

        while True:
            ret, img = cam.read()
            if not ret:
                break

            img = cv.flip(img, 1)
            img = cv.GaussianBlur(img, (5, 5), 0)
            img = imutils.resize(img, width=1030, height=700)
            height, width = img.shape[:2]
            x = 10
            y = 20
            for i in range(0, 10):
                cv.rectangle(img, (x, y), (x + 100, y + 80), (0, 255, 255), 2)
                cv.putText(img, nums[i], (x + 50, y + 40), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv.LINE_AA, False)
                x = x + 100
            y = 100
            x = 10
            for i in range(0, 10):
                cv.rectangle(img, (x, y), (x + 100, y + 80), (0, 255, 255), 2)
                cv.putText(img, row1[i], (x + 50, y + 40), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv.LINE_AA, False)
                x = x + 100
            x = 110
            y = 180
            for i in range(0, 9):
                cv.rectangle(img, (x, y), (x + 100, y + 80), (0, 255, 255), 2)
                cv.putText(img, row2[i], (x + 50, y + 40), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv.LINE_AA, False)
                x = x + 100

            x = 210
            y = 260
            for i in range(0, 7):
                cv.rectangle(img, (x, y), (x + 100, y + 80), (0, 255, 255), 2)
                cv.putText(img, row3[i], (x + 50, y + 40), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv.LINE_AA, False)
                x = x + 100
            x = 110
            y = 340
            cv.rectangle(img, (x, y), (x + 200, y + 80), (0, 255, 255), 2)
            cv.putText(img, row4[0], (x + 70, y + 40), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv.LINE_AA, False)
            x = 310
            y = 340
            cv.rectangle(img, (x, y), (x + 200, y + 80), (0, 255, 255), 2)
            cv.putText(img, row4[1], (x + 70, y + 40), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv.LINE_AA, False)
            x = 510
            y = 340
            cv.rectangle(img, (x, y), (x + 250, y + 80), (0, 255, 255), 2)
            cv.putText(img, row4[2], (x + 70, y + 40), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv.LINE_AA, False)
            x = 760
            y = 340
            cv.rectangle(img, (x, y), (x + 200, y + 80), (0, 255, 255), 2)
            cv.putText(img, row4[3], (x + 70, y + 40), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv.LINE_AA, False)
            x = 110
            y = 420
            cv.rectangle(img, (x, y), (x + 200, y + 80), (0, 255, 255), 2)
            cv.putText(img, row5[0], (x + 100, y + 40), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv.LINE_AA, False)
            x = 310
            y = 420
            cv.rectangle(img, (x, y), (x + 200, y + 80), (0, 255, 255), 2)
            cv.putText(img, row5[1], (x + 100, y + 40), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv.LINE_AA, False)
            x = 510
            y = 420
            cv.rectangle(img, (x, y), (x + 200, y + 80), (0, 255, 255), 2)
            cv.putText(img, row5[2], (x + 100, y + 40), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv.LINE_AA, False)
            x = 710
            y = 420
            cv.rectangle(img, (x, y), (x + 200, y + 80), (0, 255, 255), 2)
            cv.putText(img, row5[3], (x + 100, y + 40), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv.LINE_AA, False)
            x = 10
            y = 500
            cv.rectangle(img, (x, y), (x + 200, y + 80), (0, 255, 255), 2)
            cv.putText(img, "V+", (x + 60, y + 40), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv.LINE_AA, False)
            x = 210
            y = 500
            cv.rectangle(img, (x, y), (x + 200, y + 80), (0, 255, 255), 2)
            cv.putText(img, "V-", (x + 60, y + 40), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv.LINE_AA, False)
            x = 410
            y = 500
            cv.rectangle(img, (x, y), (x + 200, y + 80), (0, 255, 255), 2)
            cv.putText(img, "Vmute", (x + 60, y + 40), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv.LINE_AA, False)

            hsv_img = cv.cvtColor(img, cv.COLOR_BGR2HSV)
            mask = cv.inRange(hsv_img, np.array([65, 60, 60]), np.array([80, 255, 255]))
            mask_open = cv.morphologyEx(mask, cv.MORPH_OPEN, np.ones((5, 5)))
            mask_close = cv.morphologyEx(mask_open, cv.MORPH_CLOSE, np.ones((20, 20)))
            mask_final = mask_close
            conts, _ = cv.findContours(mask_final.copy(), cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
            # cv.drawContours(img,conts,-1,(255,0,0),3)
            if (len(conts) == 1):
                x, y, w, h = cv.boundingRect(conts[0])
                cx = round(x + w / 2)
                cy = round(y + h / 2)
                cv.circle(img, (cx, cy), 20, (0, 0, 255), 2)
                word = ""
                for i in range(len(json_data)):
                    if cx >= int(json_data[i]["x"]) and cx <= int(json_data[i]["x"]) + int(json_data[i]["w"]) and cy >= int(
                            json_data[i]["y"]) and cy <= int(json_data[i]["y"]) + int(json_data[i]["h"]):
                        word = json_data[i]["value"]
                # print(word)
                pyautogui.press(word)
                # pyautogui.PAUSE=2.5
                
                # time.sleep(1)

            # Convert image from BGR to RGB for Streamlit display
            img_rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
            stframe.image(img_rgb, channels='RGB')

            # Provide a unique key for the Stop button to prevent DuplicateElementId error
            # unique_key = f"stop_key_{uuid.uuid4()}"
            # if st.button('Stop', key=unique_key):
            #     break

        cam.release()

if __name__ == "__main__":
    main()