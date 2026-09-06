
<div align="center">

# ✋ Hand Tracking System

### AI-Based Hand Gesture Recognition & ESP32 LED Control

An interactive computer-vision and embedded systems project that detects hand gestures in real time using Python, OpenCV, and MediaPipe, and controls LEDs through an ESP32 using serial communication.

</div>

---

<div align="center">

### 🎥 Project Demonstration

https://github.com/user-attachments/assets/7c522c67-0783-40a0-829b-d96885ade400

</div>

---

<div align="center">

**Computer Vision • Python • MediaPipe • OpenCV • ESP32 • Embedded Systems**

</div>

<p align="center">

<img src="https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python&logoColor=white">
<img src="https://img.shields.io/badge/OpenCV-Computer%20Vision-red?style=for-the-badge&logo=opencv&logoColor=white">
<img src="https://img.shields.io/badge/MediaPipe-Hand%20Tracking-orange?style=for-the-badge">
<img src="https://img.shields.io/badge/ESP32-Embedded%20Systems-black?style=for-the-badge&logo=espressif&logoColor=white">
<img src="https://img.shields.io/badge/PySerial-Serial%20Communication-green?style=for-the-badge">
<img src="https://img.shields.io/badge/Arduino%20IDE-ESP32-blue?style=for-the-badge&logo=arduino&logoColor=white">

</p>

---

# 📖 Overview

The **Hand Tracking System** combines computer vision and embedded hardware to create a real-time gesture-controlled LED system.

A laptop camera captures the user's hand. **MediaPipe Hand Landmarker** detects 21 hand landmarks, which are analyzed using Python and OpenCV to determine the number of raised fingers.

The detected finger count is stabilized and transmitted to an **ESP32 through USB serial communication**. The ESP32 then activates the corresponding LED.

### ✋ Gesture Recognition

```text
0 Fingers → All LEDs OFF
1 Finger  → LED 1 ON
2 Fingers → LED 2 ON
3 Fingers → LED 3 ON
4 Fingers → LED 4 ON
5 Fingers → LED 5 ON
````

---

# ✨ Key Features

* 🖐️ Real-time hand tracking
* 🎯 21 hand landmark detection
* 👈👉 Left and right hand identification
* ☝️ Finger detection and counting
* 🔢 Gesture recognition from 0–5 fingers
* 🧠 Gesture stabilization
* 📊 Real-time FPS display
* 🔌 USB serial communication
* 🤖 ESP32 integration
* 💡 Individual LED control
* ⚡ Real-time hardware response

---

# 🛠 Tech Stack

## 💻 Software

| Technology  | Purpose                             |
| ----------- | ----------------------------------- |
| Python      | Main programming language           |
| OpenCV      | Camera capture and image processing |
| MediaPipe   | Hand landmark detection             |
| PySerial    | Serial communication                |
| NumPy       | Numerical processing                |
| Arduino IDE | ESP32 programming                   |

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
Laptop Camera
      ↓
    OpenCV
      ↓
MediaPipe Hand Landmarker
      ↓
21 Hand Landmarks
      ↓
Finger Detection & Counting
      ↓
Gesture Stabilization
      ↓
Python / PySerial
      ↓
 USB Serial
      ↓
    ESP32
      ↓
LED Controller
      ↓
Corresponding LED
```

---

# ⚙️ Working Modules

## 1️⃣ Hand Detection

The laptop webcam captures the user's hand using OpenCV.

## 2️⃣ Landmark Detection

MediaPipe detects **21 landmarks** on the hand.

## 3️⃣ Finger Detection

The landmark positions are analyzed to determine whether each finger is raised.

```text
THU → Thumb
IND → Index
MID → Middle
RIN → Ring
PIN → Pinky
```

## 4️⃣ Finger Counting

The system recognizes:

```text
ZERO
ONE
TWO
THREE
FOUR
FIVE
```

## 5️⃣ Gesture Stabilization

The gesture must remain consistent across consecutive frames before it is considered stable. This helps prevent unwanted gesture switching caused by small hand movements.

## 6️⃣ Serial Communication

The stable finger count is sent from Python to the ESP32 at:

```text
Baud Rate: 115200
```

## 7️⃣ LED Control

The ESP32 receives the finger count and switches on only the corresponding LED.

---

# 💡 Gesture → LED Mapping

| Finger Count | Gesture  | Output       |
| -----------: | -------- | ------------ |
|            0 | ✊ ZERO   | All LEDs OFF |
|            1 | ☝️ ONE   | LED 1 ON     |
|            2 | ✌️ TWO   | LED 2 ON     |
|            3 | 🤟 THREE | LED 3 ON     |
|            4 | 🖖 FOUR  | LED 4 ON     |
|            5 | 🖐️ FIVE | LED 5 ON     |

---

# 🔌 ESP32 Pin Configuration

| LED   |    GPIO |
| ----- | ------: |
| LED 1 | GPIO 25 |
| LED 2 | GPIO 26 |
| LED 3 | GPIO 27 |
| LED 4 | GPIO 32 |
| LED 5 | GPIO 33 |

Each LED is connected through a **1kΩ resistor**.

---

# 📂 Project Structure

```text
HandTrackingSystem/
│
├── demo/
│   └── hand_tracking_demo.mp4
│
├── esp/
│   └── esp32_led_controller.ino
│
├── hand_tracking.py
├── hand_tracking_backup.py
├── camera_test.py
├── serial_test.py
├── requirements.txt
├── .gitignore
└── hand_landmarker.task
```

> `hand_landmarker.task` is excluded from the GitHub repository through `.gitignore`.

---

# 📦 Installation

### Clone the repository

```bash
git clone https://github.com/shikha92366/HandTrackingSystem.git
cd HandTrackingSystem
```

### Create virtual environment

```bash
python -m venv venv
```

### Activate virtual environment

```bash
venv\Scripts\activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

---

# 🧠 MediaPipe Model

The project uses the MediaPipe Hand Landmarker model:

```text
hand_landmarker.task
```

Place the model file in the project root:

```text
HandTrackingSystem/
│
├── hand_tracking.py
├── hand_landmarker.task
└── ...
```

---

# 🔧 ESP32 Setup

1. Open `esp/esp32_led_controller.ino` in Arduino IDE.
2. Select **ESP32 Dev Module**.
3. Select the ESP32 COM port.
4. Upload the program.
5. Close Arduino Serial Monitor before running Python.

---

# ▶️ Run the Project

Connect the ESP32 and run:

```bash
python hand_tracking.py
```

The webcam will open and the system will begin detecting hand gestures.

Press:

```text
Q
```

to exit.

---

# 🧪 Testing Utilities

### Camera Test

```bash
python camera_test.py
```

### Serial Test

```bash
python serial_test.py
```

---

# 🚀 Applications

* 🤖 Gesture-controlled robotics
* 🏠 Smart home interfaces
* 🎮 Gesture-based control systems
* 🖥️ Human-computer interaction
* 🔌 Computer-vision controlled hardware
* 📡 IoT and embedded applications

---

# 🔮 Future Improvements

* Multiple-hand tracking
* Advanced gesture recognition
* Wireless ESP32 communication
* Gesture-controlled motors
* Robotic arm control
* IoT integration
* Custom gesture commands

---

# 📌 Learning Outcomes

* Python programming
* Computer vision
* OpenCV
* MediaPipe
* Hand landmark detection
* Gesture recognition
* Serial communication
* ESP32 programming
* GPIO control
* LED interfacing
* Hardware-software integration

---

# 🔗 Repository

[GitHub Repository](https://github.com/shikha92366/HandTrackingSystem)

---

# 👩‍💻 Author

### Shikha

**B.Tech — Electronics & Communication Engineering**

**Interests:** Embedded Systems • Computer Vision • IoT • Robotics • Artificial Intelligence

---

<p align="center">

⭐ If you found this project interesting, consider giving the repository a star!

</p>
