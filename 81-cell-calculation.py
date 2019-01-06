#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random
import os

# What to do?
# Print out the following by arranging all the numbers randomly:
# 
# x/+ | 1 2 3 4 5 6 7 8 9
#   1 |
#   2 |
#   3 |
#   4 |
#   5 |
#   6 |
#   7 |
#   8 |
#   9 |

class CellCalculation:
    def __init__(self):
        # init numbers
        self.array_x = list(range(1,10))
        self.array_y = list(range(1,10))
        # shuffle numbers
        random.shuffle(self.array_x)
        random.shuffle(self.array_y)

    def pause(self):
        programPause = input("-- Press the <ENTER> if you've done, then answers will be displayed:")

    def display_problem(self):
        # Print out x axis
        print("x/+ |", end=" ")
        for x in self.array_x:
            print(x, end=" ")

        # Print out y axis
        print("")
        for y in self.array_y:
            print("  %s |" % y)

    def display_answer(self, arithmetic_operation):
        # - Cross
        #   x |  9|  2|  8|  3|  7|  1|  6|  5|  4
        # ---  --- --- --- --- --- --- --- --- ---
        #   3 | 27|  6| 24|  9| 21|  3| 18| 15| 21
        #   7 | 63| 14| 56| 21| 49|  7| 42| 35| 28
        #   5 | 45| 10| 40| 15| 35|  5| 30| 25| 20
        #   8 | 72| 16| 64| 24| 56|  8| 48| 40| 32
        #   4 | 36|  8| 32| 12| 28|  4| 24| 20| 16
        #   6 | 54| 12| 48| 18| 42|  6| 36| 30| 24
        #   2 | 18|  4| 16|  6| 14|  2| 12| 10|  8
        #   1 |  9|  2|  8|  3|  7|  1|  6|  5|  4
        #   9 | 81| 18| 72| 27| 63|  9| 54| 45| 36
        if (arithmetic_operation == "*"):
            print("- Cross")
            print("%3s" % "x", end=" ")
        else:
            print("- Plus")
            print("%3s" % "+", end=" ")

        for x in self.array_x:
            print("|%3s" % x, end="")

        print("\n---  --- --- --- --- --- --- --- --- ---")

        # Print out y axis
        for y in self.array_y:
            print("%3s " % y, end="")
            for num in range(0,9):
                if (arithmetic_operation == "*"):
                    print("|%3s" % (y * self.array_x[num]), end="")
                else:
                    print("|%3s" % (y + self.array_x[num]), end="")

            print("")
        print("")

cellcalc = CellCalculation()
cellcalc.display_problem()
cellcalc.pause()
cellcalc.display_answer("*")
cellcalc.display_answer("+")