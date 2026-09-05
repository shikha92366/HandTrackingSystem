# AI-Based Hand Gesture Controlled LED System

A real-time hand gesture recognition system that combines **Computer Vision and Embedded Systems**. The system uses a webcam to detect a hand, identifies 21 hand landmarks using MediaPipe, counts the number of raised fingers, and sends the detected finger count to an ESP32 through USB serial communication. The ESP32 then controls five LEDs based on the detected gesture.

## Features

- Real-time hand detection
- Detection of 21 hand landmarks
- Left and right hand recognition
- Finger counting from 0 to 5
- Gesture recognition
- Real-time FPS display
- Individual finger status display
- Gesture stabilization to reduce false detections
- Python-to-ESP32 serial communication
- ESP32-based LED control
- Integration of computer vision with embedded systems

## System Architecture

```text
             LAPTOP
                |
                v
          Webcam Camera
                |
                v
             OpenCV
                |
                v
       MediaPipe Hand Landmarker
                |
                v
         21 Hand Landmarks
                |
                v
       Finger Detection & Count
                |
                v
       Gesture Stabilization
                |
                v
             PySerial
                |
                | USB Serial
                v
              ESP32
                |
        +-------+-------+
        |       |       |
       LED1    LED2    ... LED5
