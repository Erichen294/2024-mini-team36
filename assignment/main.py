"""
Response time - single-threaded
"""

from machine import Pin
from wifinetwork import WiFi
from thingspeak import ThingSpeakApi
import time
import random
import json

N: int = 10
sample_ms = 10.0
on_ms = 500

# Network initialization
wifi = WiFi()
wifi.ConnectWiFi()

# Thingspeak initialization
thingspeak = ThingSpeakApi()

def random_time_interval(tmin: float, tmax: float) -> float:
    """return a random time interval between max and min"""
    return random.uniform(tmin, tmax)


def blinker(N: int, led: Pin) -> None:
    # %% let user know game started / is over

    for _ in range(N):
        led.high()
        time.sleep(0.1)
        led.low()
        time.sleep(0.1)


def write_json(json_filename: str, data: dict) -> None:
    """Writes data to a JSON file.

    Parameters
    ----------

    json_filename: str
        The name of the file to write to. This will overwrite any existing file.

    data: dict
        Dictionary data to write to the file.
    """

    with open(json_filename, "w") as f:
        json.dump(data, f)


def scorer(t: list[int | None]) -> None:
    # %% collate results
    misses = t.count(None)
    print(f"You missed the light {misses} / {N} times")

    t_good = [x for x in t if x is not None]

    print(t_good)

    # add key, value to this dict to store the minimum, maximum, average response time
    # and score (non-misses / total flashes) i.e. the score a floating point number
    # is in range [0..1]
    data = {}
    data["score"] = t[10]
     
    data["average"] = t[11]
    data["minimum"] = t[12]
    data["maximum"] = t[13]

    # %% make dynamic filename and write JSON

    now: tuple[int] = time.localtime()

    now_str = "-".join(map(str, now[:3])) + "T" + "_".join(map(str, now[3:6]))
    filename = f"score-{now_str}.json"

    print("write", filename)

    write_json(filename, data)


if __name__ == "__main__":
    # using "if __name__" allows us to reuse functions in other script files
    # Edit the exercise_game.py code to compute average, minimum, maximum response time for 10 flashes total.
    led = Pin("LED", Pin.OUT)
    button = Pin(16, Pin.IN, Pin.PULL_UP)

    t: list[int | None] = []

    blinker(3, led)

    for i in range(N):
        time.sleep(random_time_interval(0.5, 5.0))

        led.high()

        tic = time.ticks_ms()
        t0 = None
        while time.ticks_diff(time.ticks_ms(), tic) < on_ms:
            if button.value() == 0:
                t0 = time.ticks_diff(time.ticks_ms(), tic)
                led.low()
                break
        t.append(t0)

        led.low()

    # Calculating score, average, minimum, and maximum
    total = 0
    for element in t:
        if element:
            total += element
    avg = total / N
    minimum = min([v for v in t if v is not None])
    maximum = max([v for v in t if v is not None])
    print("Average:" + str(avg))
    print("Minimum:" + str(minimum))
    print("Maximum:" + str(maximum))
    score = 0
    for x in range(N):
        if t[x]:
            score += 1
    t.append(score)
    t.append(avg)
    t.append(minimum)
    t.append(maximum)
    blinker(5, led)
    
    # Pushing data to cloud service
    thingspeak.WriteMultipleFields(t[10:])
    
    scorer(t)
