import random
import cv2
import pygame
import numpy as np
from ultralytics import YOLO


class Patrick:
    def __init__(self):
        # Opening the file in read mode
        my_file = open("coco.txt", "r")
        # Reading the file
        data = my_file.read()
        # Replacing and splitting the text when newline ('\n') is seen.
        self.class_list = data.split("\n")
        my_file.close()

        # Generate random colors for class list
        self.detection_colors = [(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)) for _ in self.class_list]

        # Load a pretrained YOLOv8n model
        self.model = YOLO("weights/yolov8n.pt", "v8")

        # Vals to resize video frames | small frame optimize the run
        frame_wid = 640
        frame_hyt = 480

        # OpenCV camera capture
        self.cap = cv2.VideoCapture(0)
        self.cap.set(cv2.CAP_PROP_FPS, 60)
        if not self.cap.isOpened():
            print("Cannot open camera")
            exit()

# clock = pygame.time.Clock()
    def recognize(self, screen, screen_width, screen_height):
        # Capture frame-by-frame
        ret, frame = self.cap.read()

        # if not ret:
        #     print("Can't receive frame (stream end?). Exiting ...")
        #     break

        # Predict on image
        detect_params = self.model.predict(source=[frame], conf=0.45, save=False)

        # Convert tensor array to numpy
        DP = detect_params[0].numpy()
        print(DP)

        if len(DP) != 0:
            for i in range(len(detect_params[0])):
                print(i)

                boxes = detect_params[0].boxes
                box = boxes[i]  # returns one box
                clsID = box.cls.numpy()[0]
                conf = box.conf.numpy()[0]
                bb = box.xyxy.numpy()[0]

                cv2.rectangle(
                    frame,
                    (int(bb[0]), int(bb[1])),
                    (int(bb[2]), int(bb[3])),
                    self.detection_colors[int(clsID)],
                    3,
                )

                # Display class name and confidence
                font = cv2.FONT_HERSHEY_COMPLEX
                cv2.putText(
                    frame,
                    self.class_list[int(clsID)] + " " + str(round(conf, 3)) + "%",
                    (int(bb[0]), int(bb[1]) - 10),
                    font,
                    1,
                    (255, 255, 255),
                    2,
                )

        # Resize frame to match Pygame display resolution
        frame = cv2.resize(frame, (screen_width, screen_height))

        # Rotate the frame 90 degrees counterclockwise
        frame = cv2.rotate(frame, cv2.ROTATE_90_COUNTERCLOCKWISE)

        # Convert frame to RGB format for Pygame
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        
        # Convert frame to Pygame surface
        frame_surface = pygame.surfarray.make_surface(frame_rgb)

        # Display the resulting frame
        screen.blit(frame_surface, (0, 0))