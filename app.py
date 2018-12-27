from flask import Flask

from s1 import S1, BoilerState, MachineState

from datetime import datetime

app = Flask(__name__)

s1 = S1()


@app.route("/vivaldi/cmds")
def cmd(request):
    if request.json["cmd"] == "on":
        if request.json["boiler"] == "off":
            s1.powerOn(boilerState=BoilerState.OFF)
        else:
            s1.powerOn()
    elif request.json["cmd"] == "off":
        s1.powerOff()


@app.route("/vivaldi")
def state(request):
    state = {}
    state["boiler"] = str(s1.boilerState).split(".")[1]
    state["machine"] = str(s1.machineState).split(".")[1]
    if s1.startTime != None:
        state["uptime"] = datetime.now() - s1.startTime


def main():
    s1.start()
