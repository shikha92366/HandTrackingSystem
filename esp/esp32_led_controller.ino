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