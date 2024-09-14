from machine import Pin
import time

# Set up the LED pin (e.g., GPIO 2 for ESP8266)
led_pin = 21
led = Pin(led_pin, Pin.OUT)

# Set up the button pin (e.g., GPIO 0 for ESP8266)
button_pin = 15
button = Pin(button_pin, Pin.IN, Pin.PULL_UP)  # Assuming a pull-up resistor

# Initial LED state
led_state = False
led.value(led_state)

try:
    while True:
        # Check if the button is pressed (button_pin will be LOW if pressed)
        if not button.value():
            # Debounce delay
            time.sleep(0.05)
            if not button.value():
                # Toggle the LED state
                led_state = not led_state
                led.value(led_state)
                
                # Wait until the button is released
                while not button.value():
                    time.sleep(0.05)

        time.sleep(0.05)  # Polling interval

except KeyboardInterrupt:
    print("Script stopped")