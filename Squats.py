import cv2
import math
import mediapipe as mp
import sys

num_squats = int(input("What is your goal? "))


def check_rep(angle, prev_angle, correct_reps):
    in_range = False

    if angle > 70 and angle < 90:
        if prev_angle is None or (prev_angle <= 70 or prev_angle >= 90):
            correct_reps += 1
            in_range = True

    prev_angle = angle

    if angle < 60 or angle > 95:
        in_range = False

    return prev_angle, correct_reps, in_range

mp_pose = mp.solutions.pose
mp_drawing = mp.solutions.drawing_utils

pose = mp_pose.Pose(static_image_mode=False, min_detection_confidence=0.5, min_tracking_confidence=0.5)
cap = cv2.VideoCapture(1)

prev_angle = None
correct_reps = 0
restart_counter = 0

def capture():

    correct_reps_threshold = num_squats
    global cap, pose, prev_angle, correct_reps, is_capturing,restart_counter

    ret, frame = cap.read()
    if not ret:
        return

    image = frame

    results = pose.process(image)

    if results.pose_landmarks is not None:
        pose_landmarks = results.pose_landmarks.landmark

        left_hip = pose_landmarks[mp_pose.PoseLandmark.LEFT_HIP.value]
        left_knee = pose_landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value]
        right_hip = pose_landmarks[mp_pose.PoseLandmark.RIGHT_HIP.value]
        right_knee = pose_landmarks[mp_pose.PoseLandmark.RIGHT_KNEE.value]

        hip_knee_angle_left = math.degrees(math.atan2(left_knee.y - left_hip.y, left_knee.x - left_hip.x))
        hip_knee_angle_right = math.degrees(math.atan2(right_knee.y - right_hip.y, right_knee.x - right_hip.x))

        angle = abs(hip_knee_angle_left - hip_knee_angle_right)

        prev_angle, correct_reps, in_range = check_rep(angle, prev_angle, correct_reps)

        if restart_counter != 0:
            prev_angle = 0
            correct_reps = 0
            restart_counter = 0
            correct_reps_threshold = 3

        if correct_reps >= num_squats:
            img = cv2.imread(r'C:\Users\M\PycharmProjects\pythonProject\gt.png')
            cv2.imshow('Congratulations', img)

    annotated_image = image.copy()
    mp_drawing.draw_landmarks(
        annotated_image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)
    cv2.putText(annotated_image, f'Correct reps: {correct_reps}',
                (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    cv2.putText(annotated_image, f'Angle: {angle:.2f} degrees' if 'angle' in locals() else 'Angle: 0 degrees',
                (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    cv2.putText(annotated_image, f'Press "r" to restart', (10, 90), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    cv2.imshow('squats', annotated_image)

    key = cv2.waitKey(1)
    if key == ord('r'):
        restart_counter = 0

    if cv2.waitKey(20) == 27:
        sys.exit()

def play():
    while True:
        capture()

play()
