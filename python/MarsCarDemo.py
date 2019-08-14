#!usr/bin/env python  
# -*- coding:utf-8 _*-  
""" 
@author:perrywu 
@file: mar.py 
@time: 2019/04/25 
"""


class MarsCarDemo:

    def __init__(self):
        self.xyMax = {"xMax": 0, "yMax": 0}
        self.marsCarPos = {"x": 0, "y": 0, "fc": None, "rip": None}

    def getXyMax(self):
        return self.xyMax

    def setXyMax(self, xy):
        self.xyMax["xMax"] = xy["xMax"]
        self.xyMax["yMax"] = xy["yMax"]

    def getMarsCarPos(self):
        return self.marsCarPos

    def setMarsCarPos(self, pos):
        self.marsCarPos["x"] = pos["x"]
        self.marsCarPos["y"] = pos["y"]
        self.marsCarPos["fc"] = pos["fc"]
        self.marsCarPos["rip"] = pos["rip"]

    def turnLeft(self, pos):
        fc = self.marsCarPos["fc"].lower()
        if fc == "e":
            pos["fc"] = "N"
        elif fc == "n":
            pos["fc"] = "W"
        elif fc == "w":
            pos["fc"] = "S"
        elif fc == "s":
            pos["fc"] = "E"
        self.setMarsCarPos(pos)

    def turnRight(self, pos):
        fc = self.marsCarPos["fc"].lower()
        if fc == "e":
            pos["fc"] = "S"
        elif fc == "s":
            pos["fc"] = "W"
        elif fc == "w":
            pos["fc"] = "N"
        elif fc == "n":
            pos["fc"] = "E"
        self.setMarsCarPos(pos)

    def moveStep(self, pos):
        fc = self.marsCarPos["fc"].lower()
        if fc == "e":
            if self.checkRipX(pos["x"]+1):
                pos["rip"] = "RIP"
            else:
                pos["x"] += 1
        elif fc == "s":
            if self.checkRipY(pos["y"]-1):
                pos["rip"] = "RIP"
            else:
                pos["y"] -= 1
        elif fc == "w":
            if self.checkRipX(pos["x"]-1):
                pos["rip"] = "RIP"
            else:
                pos["x"] -= 1
        elif fc == "n":
            if self.checkRipY(pos["y"]+1):
                pos["rip"] = "RIP"
            else:
                pos["y"] += 1
        self.setMarsCarPos(pos)

    def checkRipX(self, x):
        if (x >= self.xyMax["xMax"]) or (x < 0):
            return True
        else:
            return False

    def checkRipY(self, y):
        if (y >= self.xyMax["yMax"]) or (y < 0):
            return True
        else:
            return False

    def exCmd(self, cmd, pos, cars=None):
        if len(cmd) > 0:
            for c in cmd:
                if (c.lower()) == "r":
                    self.turnRight(pos)
                elif (c.lower()) == "l":
                    self.turnLeft(pos)
                elif (c.lower()) == "m":
                    # check move step is rip car step
                    if not self.checkIsRipCarMoveStep(pos, cars):
                        self.moveStep(pos)
                if pos["rip"]:
                    break
            self.setMarsCarPos(pos)

    @staticmethod
    def checkIsRipCarMoveStep(pos, cars):
        rip = False
        if cars:
            for car in cars:
                carPos = car.marsCarPos
                if (pos["x"] == carPos["x"]) and (pos["y"] == carPos["y"]) and (pos["fc"] == carPos["fc"]) and carPos["rip"]:
                    rip = True
                    break
        return rip

    def marsCarRunning(self, pos=None, cmd=None, cars=None):
        if pos and cmd:
            self.setMarsCarPos(pos)
            self.exCmd(cmd, pos, cars)

if __name__ == '__main__':
    input1 = "55"
    xyMax = {"xMax": int(input1[0]), "yMax": int(input1[1])}

    ### Test case1

    mc = MarsCarDemo()
    mc.setXyMax(xyMax)
    input2 = "12"
    input3 = "N"
    marsCarPos = {"x": int(input2[0]), "y": int(input2[1]), "fc": input3, "rip": None}
    # mc.setMarsCarPos(marsCarPos)
    input4 = "LMLMLMLMM"

    cars = []
    # car.marsCarPos = {"x": 0, "y": 0, "fc": None, "rip": None}
    mc.marsCarRunning(pos=marsCarPos, cmd=input4, cars=cars)
    output = str(mc.marsCarPos['x']) + str(mc.marsCarPos['y']) + " " + str(mc.marsCarPos['fc'])
    if mc.marsCarPos['rip']:
        output += " " + str(mc.marsCarPos['rip'])
    print(output)

    ### Test case2

    mc1 = MarsCarDemo()
    mc1.setXyMax(xyMax)
    input2 = "33"
    input3 = "E"
    input4 = "MMM"
    marsCarPos = {"x": int(input2[0]), "y": int(input2[1]), "fc": input3, "rip": None}

    cars = []
    mc1.marsCarRunning(pos=marsCarPos, cmd=input4, cars=cars)
    output = str(mc1.marsCarPos['x']) + str(mc1.marsCarPos['y']) + " " + str(mc1.marsCarPos['fc'])
    if mc1.marsCarPos['rip']:
        output += " " + str(mc1.marsCarPos['rip'])
    print(output)
