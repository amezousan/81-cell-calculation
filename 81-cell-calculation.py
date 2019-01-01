#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random

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

array_x = list(range(1,10))
array_y = list(range(1,10))

random.shuffle(array_x)
random.shuffle(array_y)

# Print out x axis
print("x/+ |", end=" ")
for x in array_x:
    print(x, end=" ")

# Print out y axis
print("")
for y in array_y:
    print("  %s |" % y)
