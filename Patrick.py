"""
Pushup Flappy Bird
By: Jirehl Ngo
https://www.programiz.com/python-programming/docstrings
"""

import Model_Pygame
import cv2
import pygame
import pygame.camera

class Camera(): # Make all the methods static, remove need for camera object?
    """A class to initialize a camera
    """
    def __init__(self):
        """Constructor
        """
        pygame.camera.init()
        self.refresh_camera_list()
    def get_cameras(self):
        self.cameras = pygame.camera.list_cameras() 
        return self.cameras
    def start_camera(self, selected_camera_index):
        global cam_started
        if not cam_started:
            self.cam = pygame.camera.Camera(self.get_cameras()[selected_camera_index], (720, 480))
            self.cam.start()
            cam_started = True
    def stop_camera(self):
        """
        """
        global cam_started
        if cam_started:
            cam_started = False
            self.cam.stop()
    def refresh_camera_list(self):
        """Loads a list of all available cameras
        """
        self.cameras = pygame.camera.list_cameras()

Model_Pygame.Model()


def detect_up_down_movement(self, frame):
        # Convert the frame to grayscale
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Apply frame differencing if there is a previous frame
        if self.previous_frame is not None:
            diff_frame = cv2.absdiff(self.previous_frame, gray_frame)
            _, thresholded = cv2.threshold(diff_frame, 30, 255, cv2.THRESH_BINARY)

            # Find contours in the thresholded image
            contours, _ = cv2.findContours(thresholded, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

            for contour in contours:
                # Calculate centroid of the contour
                M = cv2.moments(contour)
                if M["m00"] != 0:
                    cx = int(M["m10"] / M["m00"])
                    cy = int(M["m01"] / M["m00"])

                    # Determine direction based on the change in centroid position
                    if cy < self.previous_cy:
                        print("Moving Up")
                    elif cy > self.previous_cy:
                        print("Moving Down")

                    # Update previous centroid position
                    self.previous_cx, self.previous_cy = cx, cy

            # Display the frames
            cv2.imshow('Motion Detection', frame)
            cv2.imshow('Thresholded', thresholded)
