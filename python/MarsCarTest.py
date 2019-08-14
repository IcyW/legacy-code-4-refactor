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

    def test_turnLeft(self):
        mc = MarsCarDemo()
        pos = {"x": 3, "y": 4, "fc": 'N', "rip": None}
        mc.setMarsCarPos(pos)

        directions_map = {'N': 0, 'W': 1, 'S': 2, 'E': 3}
        directions_list = ['N', 'W', 'S', 'E']
        init_pos = mc.getMarsCarPos()["fc"]
        # print("init_pos:", init_pos)
        tar_pos = directions_list[(directions_map[init_pos] + 1) % 4]
        # print("tar_pos:", tar_pos)

        mc.turnLeft(pos)
        self.assertEqual(mc.getMarsCarPos()["fc"], tar_pos)

    def test_turnRight(self):
        mc = MarsCarDemo()
        pos = {"x": 3, "y": 4, "fc": 'N', "rip": None}
        mc.setMarsCarPos(pos)

        directions_map = {'N': 0, 'W': 1, 'S': 2, 'E': 3}
        directions_list = ['N', 'W', 'S', 'E']
        init_pos = mc.getMarsCarPos()["fc"]
        tar_pos = directions_list[(directions_map[init_pos] - 1) % 4]

        mc.turnRight(pos)
        self.assertEqual(mc.getMarsCarPos()["fc"], tar_pos)

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

