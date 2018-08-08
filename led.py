import time
# import pigpio
from threading import Thread, Event
from flask import Flask

# pio=pigpio.pi()

app = Flask(__name__)
stop_event = Event()

redPin=22
greenPin=27
bluePin=17

Colors={
"red": {"R":255, "G":0, "B":0},
"orange": {"R":255, "G":80, "B":0},
"yellow": {"R":255, "G":150, "B":0},
"green": {"R":0, "G":255, "B":0},
"cyan": {"R":0, "G":255, "B":255},
"skyblue": {"R":0, "G":128, "B":255},
"blue": {"R":0, "G":0, "B":255},
"purple": {"R":128, "G":0, "B":128},
"magenta": {"R":255, "G":0, "B":255},
"pink": {"R":252, "G":90, "B":234},
"lavender": {"R":229, "G":90, "B":255},
"brown": {"R":190, "G":25, "B":0},             #closest thing is a dull orange:/
"grey": {"R":128, "G":128, "B":128},
"black": {"R":0, "G":0, "B":0},
"white": {"R":255, "G":255, "B":255}}

@app.route("/setcolor/<color>")
def set(color):
    color=color.lower()
    if color in Colors:
        # pio.set_PWM_dutycycle(22, Colors[color]["R"])
        # pio.set_PWM_dutycycle(27, Colors[color]["G"])
        # pio.set_PWM_dutycycle(17, Colors[color]["B"])
        new_thread()
        return "color of led is %s" % color
    else:
        return "Sorry color not found"

def new_thread():
    new_thread=Thread(target=sleep)
    new_thread.start()

def sleep():
    print ("timer is starting now")
    time.sleep(10)
    print ("timer is over")
    # pio.set_PWM_dutycycle(22, 0)
    # pio.set_PWM_dutycycle(27, 0)
    # pio.set_PWM_dutycycle(17, 0)

if __name__ == '__main__':
   app.run(host="0.0.0.0",debug = True)
