import time
import random

TARGET_TEMP = 24
TOLERANCE = 1

def get_temperature():
    # Replace this with a real temperature sensor
    return random.randint(20, 35)

def ac_control(temp):
    if temp > TARGET_TEMP + TOLERANCE:
        return "AC ON ❄️"
    elif temp < TARGET_TEMP - TOLERANCE:
        return "AC OFF 🛑"
    else:
        return "AC STANDBY 🌡️"

while True:
    temperature = get_temperature()

    status = ac_control(temperature)

    print(f"Room Temperature: {temperature}°C")
    print(f"Status: {status}")
    print("-" * 30)

    time.sleep(5)
