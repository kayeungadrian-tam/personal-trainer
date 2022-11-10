import cv2
from cv2 import destroyAllWindows
import mediapipe as mp
import numpy as np
import os
from multiprocessing import Process

import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty("voices")

engine.setProperty("voice", voices[73].id)
engine.setProperty("rate", 120)


def speak(str):
    engine.say(str)
    engine.runAndWait()


def calculate_angle(a, b, c):
    a = np.array(a)  # First
    b = np.array(b)  # Mid
    c = np.array(c)  # End

    radians = np.arctan2(c[1] - b[1], c[0] - b[0]) - np.arctan2(
        a[1] - b[1], a[0] - b[0]
    )
    angle = np.abs(radians * 180.0 / np.pi)

    if angle > 180.0:
        angle = 360 - angle

    return angle


def rescale_frame(frame, percent=50):
    width = int(frame.shape[1] * percent / 100)
    height = int(frame.shape[0] * percent / 100)
    dim = (width, height)
    return cv2.resize(frame, dim, interpolation=cv2.INTER_AREA)


mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_pose = mp.solutions.pose

cap = cv2.VideoCapture("data/push_up_1.mp4")
# cap = cv2.VideoCapture(4)

width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH) + 0.5)
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT) + 0.5)
size = (640, 480)


def main():

    angle_hip = 0
    angle_knee = 0
    counter = 1
    stage = None

    with mp_pose.Pose(
        static_image_mode=False, min_detection_confidence=0.5, model_complexity=2
    ) as pose:
        while cap.isOpened():
            ret, frame = cap.read()
            if frame is not None:
                frame_ = rescale_frame(frame, percent=75)

                # Recolor image to RGB
                image = cv2.cvtColor(frame_, cv2.COLOR_BGR2RGB)
                image.flags.writeable = False

                # Make detection
                results = pose.process(image)

                # Recolor back to BGR
                image.flags.writeable = True
                image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

                try:
                    landmarks = results.pose_landmarks.landmark
                    mp_drawing.draw_landmarks(
                        frame_,
                        results.pose_landmarks,
                        mp_pose.POSE_CONNECTIONS,
                        landmark_drawing_spec=mp_drawing_styles.get_default_pose_landmarks_style(),
                    )

                    shoulder = [
                        landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].x,
                        landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].y,
                    ]

                    hip = [
                        landmarks[mp_pose.PoseLandmark.RIGHT_HIP.value].x,
                        landmarks[mp_pose.PoseLandmark.RIGHT_HIP.value].y,
                    ]

                    knee = [
                        landmarks[mp_pose.PoseLandmark.RIGHT_KNEE.value].x,
                        landmarks[mp_pose.PoseLandmark.RIGHT_KNEE.value].y,
                    ]

                    ankle = [
                        landmarks[mp_pose.PoseLandmark.RIGHT_ANKLE.value].x,
                        landmarks[mp_pose.PoseLandmark.RIGHT_ANKLE.value].y,
                    ]

                    wrist = [
                        landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value].x,
                        landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value].y,
                    ]

                    angle_hip = calculate_angle(shoulder, hip, knee)
                    angle_hip = round(angle_hip, 2)

                    angle_knee = calculate_angle(shoulder, knee, wrist)
                    angle_knee = round(angle_knee, 2)

                    if angle_knee > 45:
                        stage = "up"
                    if angle_knee <= 25 and stage == "up":
                        stage = "down"
                        speak(counter)
                        counter += 1
                        # os.system("python speaker.py 1")
                except:
                    pass

                cv2.putText(
                    frame_,
                    f"Stage : {stage} ",
                    (30, 30),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1,
                    (255, 0, 255),
                    2,
                    cv2.LINE_AA,
                )

                cv2.putText(
                    frame_,
                    "Count : " + str(counter),
                    (30, 60),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1,
                    (255, 0, 255),
                    2,
                    cv2.LINE_AA,
                )

                cv2.putText(
                    frame_,
                    "Angle : " + str(angle_knee),
                    (30, 100),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1,
                    (255, 0, 255),
                    2,
                    cv2.LINE_AA,
                )

                cv2.imshow("Mediapipe Feed", frame_)
                if cv2.waitKey(25) & 0xFF == ord("q"):
                    break

            else:
                break
        cap.release()

    destroyAllWindows()


if __name__ == "__main__":
    main()
