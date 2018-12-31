from flask import Flask, request

from s1 import S1, BoilerState, MachineState

from datetime import datetime
import json

app = Flask(__name__)

s1 = S1()


@app.route("/vivaldi/cmds", methods=["POST"])
def cmd():
    if request.json["cmd"] == "on":
        if request.json["boiler"] == "off":
            s1.powerOn(boilerState=BoilerState.OFF)
        else:
            s1.powerOn()
    elif request.json["cmd"] == "off":
        s1.powerOff()
    elif request.json["cmd"] == "autoOffMinutes":
        s1.autoOffTimeSeconds = int(request.json["time"]) * 60

    return "OK"


@app.route("/vivaldi")
def state():
    state = {}
    state["boiler"] = str(s1.boilerState).split(".")[1]
    state["machine"] = str(s1.machineState).split(".")[1]
    state["autoOffMinutes"] = s1.autoOffTimeSeconds / 60
    if s1.startTime != None:
        state["uptime"] = (datetime.now() - s1.startTime).total_seconds()
        state["uptimeMinutes"] = (datetime.now() - s1.startTime).total_seconds() / 60

    return json.dumps(state)


def main():
    s1.start()
    app.run(debug=True, host="0.0.0.0")


if __name__ == "__main__":
    main()
