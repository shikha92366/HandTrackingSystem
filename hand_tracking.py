import cv2
import mediapipe as mp
import time
import serial


# ============================================================
# ESP32 SERIAL SETUP
# ============================================================

PORT = "COM3"
BAUD_RATE = 115200

print("Connecting to ESP32...")

try:
    esp32 = serial.Serial(
        PORT,
        BAUD_RATE,
        timeout=1
    )

    time.sleep(2)

    print("ESP32 connected!")

except serial.SerialException as e:
    print("ERROR: Could not connect to ESP32.")
    print(e)
    exit()


# ============================================================
# MEDIAPIPE SETUP
# ============================================================

BaseOptions = mp.tasks.BaseOptions
HandLandmarker = mp.tasks.vision.HandLandmarker
HandLandmarkerOptions = mp.tasks.vision.HandLandmarkerOptions
VisionRunningMode = mp.tasks.vision.RunningMode


options = HandLandmarkerOptions(
    base_options=BaseOptions(
        model_asset_path="hand_landmarker.task"
    ),
    running_mode=VisionRunningMode.IMAGE,
    num_hands=1,
    min_hand_detection_confidence=0.7,
    min_hand_presence_confidence=0.7,
    min_tracking_confidence=0.7
)


detector = HandLandmarker.create_from_options(options)


# ============================================================
# CAMERA
# ============================================================

camera = cv2.VideoCapture(0)

if not camera.isOpened():

    print("ERROR: Camera could not be opened.")

    esp32.close()
    detector.close()

    exit()


print("Camera opened successfully!")


# ============================================================
# FPS
# ============================================================

previous_time = 0


# ============================================================
# GESTURE STABILIZATION
# ============================================================

current_stable_gesture = None

candidate_gesture = None

candidate_count = 0

REQUIRED_FRAMES = 8


# ============================================================
# HAND CONNECTIONS
# ============================================================

connections = [

    (0, 1),
    (1, 2),
    (2, 3),
    (3, 4),

    (0, 5),
    (5, 6),
    (6, 7),
    (7, 8),

    (0, 9),
    (9, 10),
    (10, 11),
    (11, 12),

    (0, 13),
    (13, 14),
    (14, 15),
    (15, 16),

    (0, 17),
    (17, 18),
    (18, 19),
    (19, 20),

    (5, 9),
    (9, 13),
    (13, 17)
]


# ============================================================
# FINGER DETECTION
# ============================================================

def count_fingers(hand_landmarks, handedness):

    fingers = []


    # --------------------------------------------------------
    # THUMB
    # --------------------------------------------------------

    if handedness == "Right":

        if hand_landmarks[4].x > hand_landmarks[3].x:
            fingers.append(1)
        else:
            fingers.append(0)

    else:

        if hand_landmarks[4].x < hand_landmarks[3].x:
            fingers.append(1)
        else:
            fingers.append(0)


    # --------------------------------------------------------
    # INDEX
    # --------------------------------------------------------

    if hand_landmarks[8].y < hand_landmarks[6].y:
        fingers.append(1)
    else:
        fingers.append(0)


    # --------------------------------------------------------
    # MIDDLE
    # --------------------------------------------------------

    if hand_landmarks[12].y < hand_landmarks[10].y:
        fingers.append(1)
    else:
        fingers.append(0)


    # --------------------------------------------------------
    # RING
    # --------------------------------------------------------

    if hand_landmarks[16].y < hand_landmarks[14].y:
        fingers.append(1)
    else:
        fingers.append(0)


    # --------------------------------------------------------
    # PINKY
    # --------------------------------------------------------

    if hand_landmarks[20].y < hand_landmarks[18].y:
        fingers.append(1)
    else:
        fingers.append(0)


    total = sum(fingers)


    return (
        fingers[0],
        fingers[1],
        fingers[2],
        fingers[3],
        fingers[4],
        total
    )


# ============================================================
# GESTURE NAME
# ============================================================

def get_gesture_name(count):

    gesture_names = {
        0: "ZERO",
        1: "ONE",
        2: "TWO",
        3: "THREE",
        4: "FOUR",
        5: "FIVE"
    }

    return gesture_names.get(count, "UNKNOWN")


# ============================================================
# MAIN LOOP
# ============================================================

while True:

    # --------------------------------------------------------
    # READ CAMERA
    # --------------------------------------------------------

    success, frame = camera.read()

    if not success:

        print("ERROR: Could not read camera frame.")
        break


    # --------------------------------------------------------
    # CONVERT BGR TO RGB
    # --------------------------------------------------------

    rgb_frame = cv2.cvtColor(
        frame,
        cv2.COLOR_BGR2RGB
    )


    # --------------------------------------------------------
    # MEDIAPIPE IMAGE
    # --------------------------------------------------------

    mp_image = mp.Image(
        image_format=mp.ImageFormat.SRGB,
        data=rgb_frame
    )


    # --------------------------------------------------------
    # DETECT HAND
    # --------------------------------------------------------

    result = detector.detect(mp_image)


    # ========================================================
    # HAND DETECTED
    # ========================================================

    if result.hand_landmarks:

        hand_landmarks = result.hand_landmarks[0]

        height, width, _ = frame.shape


        # ----------------------------------------------------
        # HAND TYPE
        # ----------------------------------------------------

        handedness = result.handedness[0][0].category_name


        # ----------------------------------------------------
        # DRAW CONNECTIONS
        # ----------------------------------------------------

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


        # ----------------------------------------------------
        # DRAW LANDMARKS
        # ----------------------------------------------------

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


        # ----------------------------------------------------
        # RAW FINGER COUNT
        # ----------------------------------------------------

        thumb, index, middle, ring, pinky, raw_count = \
            count_fingers(
                hand_landmarks,
                handedness
            )


        # ====================================================
        # STABILIZATION
        # ====================================================

        if raw_count == candidate_gesture:

            candidate_count += 1

        else:

            candidate_gesture = raw_count
            candidate_count = 1


        # ----------------------------------------------------
        # ACCEPT NEW GESTURE ONLY AFTER 8 FRAMES
        # ----------------------------------------------------

        if candidate_count >= REQUIRED_FRAMES:

            if candidate_gesture != current_stable_gesture:

                current_stable_gesture = candidate_gesture

                gesture = get_gesture_name(
                    current_stable_gesture
                )


                # Send only the stable gesture

                esp32.write(
                    f"{current_stable_gesture}\n".encode()
                )


                print(
                    f"Gesture: {gesture} | "
                    f"Sent: {current_stable_gesture}"
                )


        # ----------------------------------------------------
        # DISPLAY STABLE GESTURE
        # ----------------------------------------------------

        if current_stable_gesture is not None:

            gesture = get_gesture_name(
                current_stable_gesture
            )

        else:

            gesture = "DETECTING..."


        # ----------------------------------------------------
        # DISPLAY HAND
        # ----------------------------------------------------

        cv2.putText(
            frame,
            f"Hand: {handedness}",
            (20, 90),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (203, 192, 255),
            2
        )


        # ----------------------------------------------------
        # DISPLAY FINGER STATUS
        # ----------------------------------------------------

        finger_text = (
            f"THU:{thumb}  "
            f"IND:{index}  "
            f"MID:{middle}  "
            f"RIN:{ring}  "
            f"PIN:{pinky}"
        )


        cv2.putText(
            frame,
            finger_text,
            (20, 125),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (203, 192, 255),
            2
        )


        # ----------------------------------------------------
        # DISPLAY RAW COUNT
        # ----------------------------------------------------

        cv2.putText(
            frame,
            f"Fingers: {raw_count}",
            (20, 165),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (203, 192, 255),
            3
        )


        # ----------------------------------------------------
        # DISPLAY STABLE GESTURE
        # ----------------------------------------------------

        cv2.putText(
            frame,
            gesture,
            (20, 215),
            cv2.FONT_HERSHEY_SIMPLEX,
            1.2,
            (203, 192, 255),
            3
        )


    # ========================================================
    # NO HAND
    # ========================================================

    else:

        candidate_gesture = None
        candidate_count = 0


    # ========================================================
    # FPS
    # ========================================================

    current_time = time.time()


    if previous_time != 0:

        fps = 1 / (current_time - previous_time)

    else:

        fps = 0


    previous_time = current_time


    cv2.putText(
        frame,
        f"FPS: {int(fps)}",
        (20, 50),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (203, 192, 255),
        3
    )


    # ========================================================
    # DISPLAY
    # ========================================================

    cv2.imshow(
        "Hand Tracking System",
        frame
    )


    # ========================================================
    # EXIT
    # ========================================================

    if cv2.waitKey(1) & 0xFF == ord("q"):

        break


# ============================================================
# CLEANUP
# ============================================================

camera.release()

cv2.destroyAllWindows()

detector.close()

esp32.close()

print("Program stopped.")