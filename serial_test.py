import serial
import time

# ESP32 COM port
PORT = "COM3"

# Communication speed
BAUD_RATE = 115200

print("Connecting to ESP32...")

esp32 = serial.Serial(
    PORT,
    BAUD_RATE,
    timeout=1
)

time.sleep(2)

print("ESP32 connected!")

while True:

    command = input("Enter a number (0-5), or q to quit: ")

    if command == "q":
        break

    if command in ["0", "1", "2", "3", "4", "5"]:

        esp32.write((command + "\n").encode())

        print("Sent:", command)

    else:
        print("Please enter only 0, 1, 2, 3, 4, 5 or q.")


esp32.close()

print("Connection closed.")