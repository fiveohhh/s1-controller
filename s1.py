import threading
import time

import RPi.GPIO as GPIO

from collections import deque

import logging
from logging.handlers import RotatingFileHandler


logger = logging.getLogger(__name__)
handler = RotatingFileHandler('s1-logs.log', maxBytes=2000000, backupCount=2)
logger.addHandler(handler)
logger.setLevel(logging.INFO)


BOILER_OFF = 0
BOILER_ON_NOT_TO_TEMP = 1
BOILER_ON_TO_TEMP = 2

MACHINE_OFF = 0
MACHINE_ON = 1

BOILER_BTN = 31
ON_OFF_BTN = 37
SINGLE_BTN_MONITOR = 15
DOUBLE_BTN_MONITOR = 7
BOILER_LED = 13
ON_STBY_LED = 11

class S1():
    def __init__(self):
        logger.info("Creating s1")
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


        self.machineState = MACHINE_OFF
        self.boilerState = BOILER_OFF
        self._kill = False
        self._running = False


    def run(self):
        logger.info("Starting...")
        onstby_led_history = deque(maxlen=20)
        boiler_led_history = deque(maxlen=20)
        #single_btn_history = deque(maxlen=20)
        #double_btn_history = deque(maxlen=20)

        self._running = True
        while not self._kill:
            onstby_led_history.append(GPIO.input(ON_STBY_LED))
            #logger.info("on stby history: {}".format(onstby_led_history)) 
            if sum(onstby_led_history) == 0:
                self.machineState = MACHINE_ON
            else:
                self.machineState = MACHINE_OFF

            boiler_led_history.append(GPIO.input(BOILER_LED))
            logger.info("boiler history: {}".format(boiler_led_history))
            if sum(boiler_led_history) == 0:
                self.boilerState = BOILER_ON_TO_TEMP
            elif sum(boiler_led_history) < 30:
                
                self.boilerState = BOILER_ON_NOT_TO_TEMP
            else:
                self.boilerState = BOILER_OFF
            '''
            single_btn_history.append(1)
            if sum(single_btn_history) != 20:
                # single button press detected
                pass

            single_btn_history.append(1)
            if sum(double_btn_history) != 20:
                # double button press detected
                pass            
            '''
            # check and update things
            time.sleep(.1)
        logger.debug("Stopping")
        self._running = False

    def powerOn(self, boilerState=1):
        if self.machineState == 0:
            GPIO.output(ON_OFF_BTN, GPIO.HIGH)
            time.sleep(3.5)
            GPIO.output(ON_OFF_BTN, GPIO.LOW)

        if boilerState == 0:
            time.sleep(2)
            # power off boiler
            GPIO.output(BOILER_BTN, GPIO.HIGH)
            time.sleep(.25)
            GPIO.output(BOILER_BTN, GPIO.LOW)

    def setBoiler(self, boilerState):
        if (boilerState == 1 and self.boilerState == BOILER_OFF) or
                (boilerState == 0 and self.boilerState != BOILER_OFF):
            GPIO.output(BOILER_BTN, GPIO.HIGH)
            time.sleep(.25)
            GPIO.output(BOILER_BTN, GPIO.LOW)


    def powerOff(self):
        GPIO.output(ON_OFF_BTN, GPIO.HIGH)
        time.sleep(.25)
        GPIO.output(ON_OFF_BTN, GPIO.LOW)

    def restart(self):
        logger.debug("restart request")
        self._kill = True
        while (self._running == True):
            time.sleep(.1)
        logger.debug("restarting")
        self.start()

    def stop(self):
        logger.debug("stop request")
        self._kill = True
        

    def start(self):
        t = threading.Thread(target=self.run)
        t.start()
