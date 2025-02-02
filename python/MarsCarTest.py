#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 14/8/2019 下午7:14
@Author  : Icy Huang
@Site    : 
@File    : MarsCarTest.py
@Software: PyCharm Community Edition
@Python  : 
"""

import copy
import unittest
from MarsCarDemo import MarsCarDemo


class MyTestCase(unittest.TestCase):
    def test_getXyMax(self):
        mc = MarsCarDemo()
        self.assertEqual(mc.getXyMax(), {"xMax": 0, "yMax": 0})

    def test_setXyMax(self):
        mc = MarsCarDemo()
        xy = {"xMax": 1, "yMax": 2}
        mc.setXyMax(xy)
        self.assertEqual(mc.xyMax, xy)

    def test_getMarsCarPos(self):
        mc = MarsCarDemo()
        self.assertEqual(mc.getMarsCarPos(), {"x": 0, "y": 0, "fc": None, "rip": None})

    def test_setMarsCarPos(self):
        mc = MarsCarDemo()
        pos = {"x": 3, "y": 4, "fc": None, "rip": None}
        mc.setMarsCarPos(pos)
        self.assertEqual(mc.getMarsCarPos(), pos)

    def test_checkRipY_pass(self):
        mc = MarsCarDemo()
        xy = {"xMax": 5, "yMax": 5}
        mc.setXyMax(xy)
        y = 4
        print(mc.checkRipY(y))
        self.assertEqual(mc.checkRipY(y), False)

    def test_checkRipY_bigger(self):
        mc = MarsCarDemo()
        xy = {"xMax": 5, "yMax": 5}
        mc.setXyMax(xy)
        y = 6
        self.assertEqual(mc.checkRipY(y), True)

    def test_checkRipY_smaller(self):
        mc = MarsCarDemo()
        xy = {"xMax": 5, "yMax": 5}
        mc.setXyMax(xy)
        y = -1
        self.assertEqual(mc.checkRipY(y), True)

    def test_turnLeft(self):
        mc = MarsCarDemo()
        pos = {"x": 3, "y": 4, "fc": 'N', "rip": None}
        mc.setMarsCarPos(pos)

        tar_pos = {"x": 3, "y": 4, "fc": 'W', "rip": None}
        mc.turnLeft(pos)
        self.assertEqual(mc.getMarsCarPos(), tar_pos)

    def test_turnRight(self):
        mc = MarsCarDemo()
        pos = {"x": 3, "y": 4, "fc": 'N', "rip": None}
        mc.setMarsCarPos(pos)

        tar_pos = {"x": 3, "y": 4, "fc": 'E', "rip": None}
        mc.turnRight(pos)
        self.assertEqual(mc.getMarsCarPos(), tar_pos)

    def test_moveStep_rip(self):
        mc = MarsCarDemo()
        xy = {"xMax": 4, "yMax": 4}
        mc.setXyMax(xy)
        pos = {"x": 3, "y": 4, "fc": 'N', "rip": None}
        mc.setMarsCarPos(pos)

        # print(mc.getMarsCarPos())
        mc.moveStep(pos)
        # print(mc.getMarsCarPos())
        self.assertEqual(mc.getMarsCarPos()["rip"], 'RIP')

    def test_moveStep_alive(self):
        mc = MarsCarDemo()
        xy = {"xMax": 5, "yMax": 5}
        mc.setXyMax(xy)
        pos = {"x": 3, "y": 4, "fc": 'E', "rip": None}
        mc.setMarsCarPos(pos)

        tar_pos = copy.deepcopy(pos)
        tar_pos['x'] += 1
        # print(mc.getMarsCarPos())
        mc.moveStep(pos)
        # print(mc.getMarsCarPos())
        self.assertEqual(mc.getMarsCarPos(), tar_pos)


if __name__ == '__main__':
    unittest.main()

