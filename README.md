# Hand Tracking System Using Python & Computer Vision

### AI-Based Hand Gesture Recognition and ESP32 LED Control

An interactive computer-vision project that detects hand gestures in real time using **Python, OpenCV, and MediaPipe**, identifies the number of raised fingers, and communicates the detected gesture to an **ESP32** through serial communication.

The ESP32 then controls **5 LEDs**, where each finger count corresponds to one specific LED.

---

# 📖 Overview

The **Hand Tracking System** combines computer vision, hand landmark detection, Python programming, and embedded hardware control into one real-time system.

A laptop camera captures the user's hand, while **MediaPipe Hand Landmarker** detects **21 hand landmarks**. The Python program analyzes these landmarks to determine the number of raised fingers from **0 to 5**.

The detected gesture is displayed on the screen along with:

- Hand type
- Finger status
- Finger count
- Stable gesture
- FPS

The recognized gesture is then transmitted from Python to the **ESP32 through USB serial communication**.

The ESP32 receives the finger count and activates the corresponding LED.

---
# 📸 Project Gallery

### 🎥 Project Demonstration

The following video demonstrates the complete working of the Hand Tracking System, including real-time hand gesture detection, finger counting, serial communication, and ESP32 LED control.

[▶️ Watch Project Demonstration](./demo/hand_tracking_demo.mp4)

# 🎥 Demonstration

The system works in real time:

```text
User Hand
    ↓
Laptop Camera
    ↓
OpenCV
    ↓
MediaPipe Hand Landmarker
    ↓
21 Hand Landmarks
    ↓
Finger Detection
    ↓
Finger Count (0–5)
    ↓
Gesture Stabilization
    ↓
Python Serial Communication
    ↓
USB Serial
    ↓
ESP32
    ↓
Corresponding LED
````

---

## 📂 Demo Gallery

### Included Demonstrations

* ✋ Real-time hand detection
* 🖐️ Five-finger gesture detection
* ☝️ One-finger gesture detection
* ✌️ Two-finger gesture detection
* 🤟 Three-finger gesture detection
* 🖖 Four-finger gesture detection
* ✊ Zero-finger gesture detection
* 💡 ESP32 LED control
* 📡 Python-to-ESP32 serial communication

---

# ✨ Key Features

* 🖐️ Real-time hand tracking
* 🎯 Detection of 21 hand landmarks
* 👈👉 Left and right hand identification
* ☝️ Real-time finger detection
* 🔢 Finger counting from 0 to 5
* 🧠 Gesture stabilization using consecutive frames
* 📊 Real-time FPS counter
* 🖥️ Visual gesture information on screen
* 🔌 Serial communication with ESP32
* 💡 Control of 5 LEDs
* ⚡ Real-time hardware response
* 🐍 Python-based computer vision
* 🤖 MediaPipe hand landmark detection

---

# 🛠 Tech Stack

## 💻 Software

| Technology          | Purpose                             |
| ------------------- | ----------------------------------- |
| Python              | Main programming language           |
| OpenCV              | Camera capture and image processing |
| MediaPipe           | Hand landmark detection             |
| PySerial            | Serial communication with ESP32     |
| NumPy               | Numerical processing                |
| MediaPipe Tasks API | Hand Landmarker implementation      |

## 🔧 Hardware

| Component               |    Quantity |
| ----------------------- | ----------: |
| ESP32 Development Board |           1 |
| LED                     |           5 |
| 1kΩ Resistor            |           5 |
| Breadboard              |           1 |
| Jumper Wires            | As required |
| USB Cable               |           1 |
| Laptop Webcam           |           1 |

---

# 🏗️ System Architecture

```text
                    ┌──────────────────────┐
                    │     Laptop Camera    │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │       OpenCV         │
                    │  Image Acquisition   │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │      MediaPipe       │
                    │   Hand Landmarker    │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │  21 Hand Landmarks   │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │   Finger Detection   │
                    │     & Counting       │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │ Gesture Stabilization│
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │   Python / PySerial  │
                    │ Serial Communication │
                    └──────────┬───────────┘
                               │
                         USB Serial
                               │
                               ▼
                    ┌──────────────────────┐
                    │        ESP32         │
                    │  Gesture Processing  │
                    └──────────┬───────────┘
                               │
              ┌────────────────┼────────────────┐
              │                │                │
              ▼                ▼                ▼
           LED 1            LED 2            LED 3
              │                │                │
              └────────────────┬───────────────┘
                               │
                    ┌──────────┴───────────┐
                    │       LED 4 / 5       │
                    └───────────────────────┘
```

---

# ⚙️ Working Modules

## 1️⃣ Camera Module

The laptop webcam continuously captures frames using OpenCV.

```python
cap = cv2.VideoCapture(0)
```

The captured frames are processed in real time.

---

## 2️⃣ Hand Landmark Detection

The project uses the **MediaPipe Hand Landmarker** to detect the hand.

MediaPipe provides **21 landmarks** for a detected hand.

These landmarks are used to determine the position of different parts of the hand and fingers.

---

## 3️⃣ Hand Identification

The system identifies whether the detected hand is:

```text
Left Hand
Right Hand
```

This information is displayed on the computer-vision interface.

---

## 4️⃣ Finger Detection

The program analyzes landmark positions to determine whether individual fingers are raised.

The five fingers are represented as:

```text
THU → Thumb
IND → Index
MID → Middle
RIN → Ring
PIN → Pinky
```

The interface displays the status of each finger.

---

## 5️⃣ Finger Counting

The detected fingers are counted and classified into six gestures:

```text
0 → ZERO
1 → ONE
2 → TWO
3 → THREE
4 → FOUR
5 → FIVE
```

---

## 6️⃣ Gesture Stabilization

To avoid unstable gesture changes caused by small movements of the hand or camera, the system checks consecutive frames.

A gesture must remain consistent for multiple frames before being treated as the stable gesture.

This reduces unwanted rapid switching between gestures.

---

## 7️⃣ Serial Communication

Once a stable gesture is detected, Python sends the corresponding finger count to the ESP32 using **PySerial**.

Communication settings:

```text
Port      : COM3
Baud Rate : 115200
```

The command is transmitted through USB serial communication.

---

## 8️⃣ ESP32 LED Controller

The ESP32 receives the finger count and controls five LEDs.

The LED pins used are:

| LED   | ESP32 GPIO |
| ----- | ---------: |
| LED 1 |    GPIO 25 |
| LED 2 |    GPIO 26 |
| LED 3 |    GPIO 27 |
| LED 4 |    GPIO 32 |
| LED 5 |    GPIO 33 |

---

# 💡 Gesture → LED Mapping

Only **one LED is ON at a time**.

| Finger Count | Gesture | LED          |
| -----------: | ------- | ------------ |
|            0 | ZERO    | All LEDs OFF |
|            1 | ONE     | LED 1        |
|            2 | TWO     | LED 2        |
|            3 | THREE   | LED 3        |
|            4 | FOUR    | LED 4        |
|            5 | FIVE    | LED 5        |

Example:

```text
☝️  1 Finger
     ↓
   LED 1 ON

✌️  2 Fingers
     ↓
   LED 2 ON

🤟  3 Fingers
     ↓
   LED 3 ON

🖖  4 Fingers
     ↓
   LED 4 ON

🖐️  5 Fingers
     ↓
   LED 5 ON

✊  0 Fingers
     ↓
   All LEDs OFF
```

---

# 🔌 ESP32 Pin Configuration

```text
LED 1 → GPIO 25 → 1kΩ Resistor → LED → GND

LED 2 → GPIO 26 → 1kΩ Resistor → LED → GND

LED 3 → GPIO 27 → 1kΩ Resistor → LED → GND

LED 4 → GPIO 32 → 1kΩ Resistor → LED → GND

LED 5 → GPIO 33 → 1kΩ Resistor → LED → GND
```

Each LED is connected through a **1kΩ current-limiting resistor**.

---

# 📂 Project Structure

```text
HandTrackingSystem/
│
├── hand_tracking.py
│
├── camera_test.py
│
├── serial_test.py
│
├── hand_tracking_backup.py
│
├── requirements.txt
│
├── .gitignore
│
├── esp/
│   └── esp32_led_controller.ino
│
└── hand_landmarker.task
```

> `hand_landmarker.task` is not included in the GitHub repository because the model file is excluded through `.gitignore`.

---

# 📦 Installation

## 1️⃣ Clone the Repository

```bash
git clone https://github.com/shikha92366/HandTrackingSystem.git
```

Move into the project directory:

```bash
cd HandTrackingSystem
```

---

## 2️⃣ Create a Virtual Environment

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

---

## 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

The required Python libraries are:

```text
mediapipe
opencv-contrib-python
numpy
pyserial
```

---

# 🧠 MediaPipe Model

The project uses the MediaPipe Hand Landmarker model:

```text
hand_landmarker.task
```

Place the model file in the project root directory:

```text
HandTrackingSystem/
│
├── hand_tracking.py
├── hand_landmarker.task
└── ...
```

The Python program loads the model using:

```python
BaseOptions(model_asset_path="hand_landmarker.task")
```

---

# 🔧 ESP32 Setup

## 1. Open Arduino IDE

Open:

```text
esp/esp32_led_controller.ino
```

---

## 2. Select ESP32 Board

In Arduino IDE select:

```text
Board → ESP32 Dev Module
```

---

## 3. Select COM Port

Select the COM port corresponding to your ESP32.

Example:

```text
COM3
```

---

## 4. Upload the Program

Upload the following ESP32 controller program:

```cpp
const int leds[] = {25, 26, 27, 32, 33};

void setup() {
  Serial.begin(115200);

  for (int i = 0; i < 5; i++) {
    pinMode(leds[i], OUTPUT);
    digitalWrite(leds[i], LOW);
  }
}

void loop() {
  if (Serial.available()) {

    String command = Serial.readStringUntil('\n');
    command.trim();

    int fingerCount = command.toInt();

    // Turn all LEDs OFF
    for (int i = 0; i < 5; i++) {
      digitalWrite(leds[i], LOW);
    }

    // Turn ON only the corresponding LED
    if (fingerCount >= 1 && fingerCount <= 5) {
      digitalWrite(leds[fingerCount - 1], HIGH);
    }

    Serial.print("Received: ");
    Serial.println(fingerCount);
  }
}
```

---

# ▶️ Running the Project

After connecting the ESP32:

```bash
python hand_tracking.py
```

The webcam window will open.

Show your hand in front of the camera.

The system will:

```text
Detect Hand
    ↓
Detect 21 Landmarks
    ↓
Identify Fingers
    ↓
Count Fingers
    ↓
Stabilize Gesture
    ↓
Send Finger Count
    ↓
ESP32 Receives Data
    ↓
Corresponding LED Turns ON
```

Press:

```text
Q
```

to exit the application.

---

# 🖥️ Real-Time Interface

The application displays information such as:

```text
FPS
Hand Type
THU
IND
MID
RIN
PIN
Raw Count
Stable Gesture
```

The hand landmarks and connections are also displayed directly on the camera feed.

---

# 🧪 Testing Utilities

The project also contains utility programs for testing individual components.

### Camera Test

```bash
python camera_test.py
```

Used to verify that the laptop camera can be accessed successfully.

### Serial Test

```bash
python serial_test.py
```

Used to test serial communication between the laptop and ESP32.

---

# 🔄 Complete Working Flow

```text
                    USER
                     │
                     ▼
                Hand Gesture
                     │
                     ▼
              Laptop Webcam
                     │
                     ▼
                  OpenCV
                     │
                     ▼
              MediaPipe Model
                     │
                     ▼
             21 Hand Landmarks
                     │
                     ▼
             Finger Detection
                     │
                     ▼
              Finger Count
                0 → 5
                     │
                     ▼
           Gesture Stabilization
                     │
                     ▼
                 PySerial
                     │
                     ▼
              USB Serial Link
                     │
                     ▼
                  ESP32
                     │
                     ▼
             LED Controller
                     │
          ┌──────────┼──────────┐
          ▼          ▼          ▼
        LED 1      LED 2      LED 3
          │          │          │
          └──────────┼──────────┘
                     │
                  LED 4 / 5
```

---

# 🚀 Applications

This project demonstrates the integration of **Computer Vision and Embedded Systems** and can be extended for:

* 🤖 Gesture-controlled robotics
* 🏠 Smart home interfaces
* ♿ Contactless accessibility systems
* 🎮 Gesture-based control systems
* 🖥️ Human-computer interaction
* 🔌 Computer vision controlled hardware
* 📡 IoT and embedded control applications

---

# 🔮 Future Improvements

Possible future improvements include:

* Multiple-hand tracking
* More advanced gesture recognition
* Wireless communication using Wi-Fi/Bluetooth
* Controlling motors using gestures
* Gesture-controlled robotic arms
* IoT dashboard integration
* Custom gesture commands
* Voice + gesture hybrid control
* Mobile application integration

---

# 🧰 Technologies Used

```text
Python
OpenCV
MediaPipe
NumPy
PySerial
ESP32
Arduino IDE
USB Serial Communication
Computer Vision
Embedded Systems
```

---

# 📌 Learning Outcomes

Through this project, the following concepts were implemented:

* Python programming
* Computer vision
* OpenCV camera handling
* MediaPipe hand landmark detection
* Real-time image processing
* Hand gesture recognition
* Serial communication
* ESP32 programming
* GPIO control
* LED interfacing
* Hardware-software integration
* Debugging and testing

---

# 🔗 Repository

GitHub:

[https://github.com/shikha92366/HandTrackingSystem](https://github.com/shikha92366/HandTrackingSystem)

---

# 👩‍💻 Author

### Shikha

B.Tech — Electronics & Communication Engineering

Interested in:

```text
Embedded Systems
Computer Vision
IoT
Robotics
Artificial Intelligence
```

---

<p align="center">

⭐ If you found this project interesting, consider giving the repository a star!

</p>
