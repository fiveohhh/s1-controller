import threading
import time

import RPi.GPIO as GPIO

from collections import deque

import logging
from logging.handlers import RotatingFileHandler
from enum import Enum

from datetime import datetime

logger = logging.getLogger(__name__)
if not len(logger.handlers):
    handler = RotatingFileHandler("s1-logs.log", maxBytes=2000000, backupCount=2)
    logger.addHandler(handler)

    formatter = logging.Formatter(
        fmt="%(asctime)s %(levelname)-8s %(message)s", datefmt="%Y-%m-%d %H:%M:%S"
    )

    handler.setFormatter(formatter)

logger.setLevel(logging.INFO)


class BoilerState(Enum):
    OFF = 0
    ON_NOT_TO_TEMP = 1
    ON_TO_TEMP = 2
    ON = 3


class MachineState(Enum):
    OFF = 0
    ON = 1


BOILER_BTN = 31
ON_OFF_BTN = 37
SINGLE_BTN_MONITOR = 15
DOUBLE_BTN_MONITOR = 7
BOILER_LED = 13
ON_STBY_LED = 11


class S1:
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

        self.machineState = MachineState.OFF
        self.boilerState = BoilerState.OFF
        self._kill = False
        self._running = False
        self.startTime = None
        # set to zero to disable auto off
        self.autoOffTimeSeconds = 60 * 60 * 2  # 2 hours

    def run(self):
        logger.info("Starting...")
        onstby_led_history = deque(maxlen=10)
        boiler_led_history = deque(maxlen=10)

        self._running = True
        while not self._kill:
            onstby_led_history.append(GPIO.input(ON_STBY_LED))
            logger.debug("on stby history: {}".format(onstby_led_history))
            if len(onstby_led_history) == 10:
                if sum(onstby_led_history) == 0:
                    if self.machineState != MachineState.ON:
                        logger.info("Machine turned on")
                        self.machineState = MachineState.ON
                        self.startTime = datetime.now()
                else:
                    if self.machineState != MachineState.OFF:
                        logger.info("Machine turned off")
                        self.machineState = MachineState.OFF
                        self.startTime = None

            boiler_led_history.append(GPIO.input(BOILER_LED))
            logger.debug("boiler history: {}".format(boiler_led_history))
            if len(boiler_led_history) == 10:
                if sum(boiler_led_history) == 0:
                    if self.boilerState != BoilerState.ON_TO_TEMP:
                        logger.info("Boiler to temp")
                        self.boilerState = BoilerState.ON_TO_TEMP
                elif sum(boiler_led_history) < 10:
                    if self.boilerState != BoilerState.ON_NOT_TO_TEMP:
                        logger.info("Boiler heating")
                        self.boilerState = BoilerState.ON_NOT_TO_TEMP
                else:
                    if self.boilerState != BoilerState.OFF:
                        logger.info("Boiler turned off")
                        self.boilerState = BoilerState.OFF

            if (
                (self.autoOffTimeSeconds > 0)
                and self.startTime != None
                and (
                    (datetime.now() - self.startTime).total_seconds()
                    > self.autoOffTimeSeconds
                )
            ):
                self.powerOff()

            # check and update things
            time.sleep(0.1)
        logger.info("Stopping")
        self._running = False

    def powerOn(self, boilerState=1):
        logger.info("Turning machine on")
        if self.machineState == MachineState.OFF:
            GPIO.output(ON_OFF_BTN, GPIO.HIGH)
            time.sleep(3.5)
            GPIO.output(ON_OFF_BTN, GPIO.LOW)

            if boilerState == BoilerState.OFF:
                logger.info("Turning boiler off")
                time.sleep(2)
                # power off boiler
                GPIO.output(BOILER_BTN, GPIO.HIGH)
                time.sleep(0.25)
                GPIO.output(BOILER_BTN, GPIO.LOW)

    def setBoiler(self, boilerState):
        if (boilerState == 1 and self.boilerState == BoilerState.OFF) or (
            boilerState == 0 and self.boilerState != BoilerState.OFF
        ):
            logger.info("Toggling boiler state")
            GPIO.output(BOILER_BTN, GPIO.HIGH)
            time.sleep(0.25)
            GPIO.output(BOILER_BTN, GPIO.LOW)

    def powerOff(self):
        logger.info("Powering off")
        GPIO.output(ON_OFF_BTN, GPIO.HIGH)
        time.sleep(0.25)
        GPIO.output(ON_OFF_BTN, GPIO.LOW)

    def restart(self):
        logger.info("restart request")
        self._kill = True
        while self._running == True:
            time.sleep(0.1)
        logger.info("restarting")
        self.start()

    def stop(self):
        logger.info("stop request")
        self._kill = True

    def start(self):
        t = threading.Thread(target=self.run)
        t.start()
