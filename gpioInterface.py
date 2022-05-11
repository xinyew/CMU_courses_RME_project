from gpiozero import Button
from signal import pause
from datetime import datetime

button = Button(2)
f = open("testAndSending.py", "r")
s = f.read()
f.close()


def capture():
    print(datetime.now().isoformat())
    exec(s)


button.when_pressed = capture

pause()
