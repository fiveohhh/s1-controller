import threading
import time

import RPi.GPIO as GPIO

from collections import deque

BOILER_OFF = 0
BOILER_ON_NOT_TO_TEMP = 1
BOILER_ON_TO_TEMP = 2

MACHINE_OFF = 0
MACHINE_ON = 1

BOILER_BTN = 31
ON_OFF_BTN = 37
SINGLE_BTN_MONITOR = 29
DOUBLE_BTN_MONITOR = 30
BOILER_LED = 31
ON_STBY_LED = 30

GPIO.setmode(GPIO.BOARD)
GPIO.setup(BOILER_BTN, GPIO.OUT)
GPIO.setup(ON_OFF_BTN, GPIO.OUT)
GPIO.setup(SINGLE_BTN_MONITOR, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(DOUBLE_BTN_MONITOR, GPIO.IN, pull_up_down=GPIO.PUD_UP)        
GPIO.setup(BOILER_LED, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(ON_STBY_LED, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# init pins to keep buttons off.
GPIO.output(BOILER_BTN, GPIO.LOW)
GPIO.output(ON_OFF_BTN, GPIO.LOW)

class S1():
    def __init__(self):
        self.machineState = MACHINE_OFF
        self.boilerState = BOILER_OFF
        self._kill = False
        self._running = False


    def run(self):
        onstby_led_history = deque(maxlen=30)
        boiler_led_history = deque(maxlen=30)
        single_btn_history = deque(maxlen=20)
        double_btn_history = deque(maxlen=20)

        self._running = True
        while not self._kill:
            onstby_led_history.append(1)
            if sum(onstby_led_history) != 30:
                self.machineState = MACHINE_OFF

            boiler_led_history.append(2)
            if sum(boiler_led_history) >= 30:
                self.boilerState = BOILER_ON_TO_TEMP
            elif sum(boiler_led_history) > 0:
                self.boilerState = BOILER_ON_NOT_TO_TEMP
            else:
                self.boilerState = BOILER_OFF

            single_btn_history.append(1)
            if sum(single_btn_history) != 20:
                # single button press detected
                pass

            single_btn_history.append(1)
            if sum(double_btn_history) != 20:
                # double button press detected
                pass            

            # check and update things
            time.sleep(.1)

        self._running = False

    def restart(self):
        self._kill = True
        while (self._running == True):
            time.sleep(.1)
        self.start()

    def stop(self):
        self._kill = True
        

    def start(self):
        t = threading.Thread(target=self.run)
        t.start()