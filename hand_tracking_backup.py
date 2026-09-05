import cv2
import mediapipe as mp
import time


# ==========================================
# 1. MediaPipe Hand Landmarker setup
# ==========================================

BaseOptions = mp.tasks.BaseOptions
HandLandmarker = mp.tasks.vision.HandLandmarker
HandLandmarkerOptions = mp.tasks.vision.HandLandmarkerOptions
VisionRunningMode = mp.tasks.vision.RunningMode


options = HandLandmarkerOptions(
    base_options=BaseOptions(
        model_asset_path="hand_landmarker.task"
    ),
    running_mode=VisionRunningMode.IMAGE,
    num_hands=2,
    min_hand_detection_confidence=0.7,
    min_hand_presence_confidence=0.7,
    min_tracking_confidence=0.7
)


# ==========================================
# 2. Create the hand detector
# ==========================================

detector = HandLandmarker.create_from_options(options)


# ==========================================
# 3. Open laptop webcam
# ==========================================

camera = cv2.VideoCapture(0)

if not camera.isOpened():
    print("ERROR: Camera could not be opened.")
    detector.close()
    exit()

print("Camera opened successfully!")


# ==========================================
# 4. FPS variables
# ==========================================

previous_time = 0


# ==========================================
# 5. Hand connections
# ==========================================

connections = [
    (0, 1), (1, 2), (2, 3), (3, 4),

    (0, 5), (5, 6), (6, 7), (7, 8),

    (0, 9), (9, 10), (10, 11), (11, 12),

    (0, 13), (13, 14), (14, 15), (15, 16),

    (0, 17), (17, 18), (18, 19), (19, 20),

    (5, 9),
    (9, 13),
    (13, 17)
]


# ==========================================
# 6. Main loop
# ==========================================

while True:

    success, frame = camera.read()

    if not success:
        print("ERROR: Could not read camera frame.")
        break


    # --------------------------------------
    # Convert BGR → RGB
    # --------------------------------------

    rgb_frame = cv2.cvtColor(
        frame,
        cv2.COLOR_BGR2RGB
    )


    # --------------------------------------
    # Convert to MediaPipe image
    # --------------------------------------

    mp_image = mp.Image(
        image_format=mp.ImageFormat.SRGB,
        data=rgb_frame
    )


    # --------------------------------------
    # Detect hands
    # --------------------------------------

    result = detector.detect(mp_image)


    # ======================================
    # 7. Draw hand landmarks
    # ======================================

    if result.hand_landmarks:

        for hand_landmarks in result.hand_landmarks:

            height, width, _ = frame.shape


            # ------------------------------
            # Draw connections
            # ------------------------------

            for start, end in connections:

                x1 = int(
                    hand_landmarks[start].x * width
                )
                y1 = int(
                    hand_landmarks[start].y * height
                )

                x2 = int(
                    hand_landmarks[end].x * width
                )
                y2 = int(
                    hand_landmarks[end].y * height
                )

                cv2.line(
                    frame,
                    (x1, y1),
                    (x2, y2),
                    (203, 192, 255),
                    3
                )


            # ------------------------------
            # Draw landmark points
            # ------------------------------

            for landmark in hand_landmarks:

                x = int(
                    landmark.x * width
                )
                y = int(
                    landmark.y * height
                )

                cv2.circle(
                    frame,
                    (x, y),
                    6,
                    (180, 105, 255),
                    -1
                )


    # ======================================
    # 8. Calculate FPS
    # ======================================

    current_time = time.time()

    if previous_time != 0:

        fps = 1 / (
            current_time - previous_time
        )

    else:

        fps = 0

    previous_time = current_time


    # ======================================
    # 9. Display FPS
    # ======================================

    cv2.putText(
        frame,
        f"FPS: {int(fps)}",
        (20, 50),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (203, 192, 255),
        3
    )


    # ======================================
    # 10. Display camera
    # ======================================

    cv2.imshow(
        "Hand Tracking System",
        frame
    )


    # ======================================
    # 11. Quit with Q
    # ======================================

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break


# ==========================================
# 12. Cleanup
# ==========================================

camera.release()

cv2.destroyAllWindows()

detector.close()

print("Program stopped.")