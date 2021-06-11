#!/usr/bin/env python3

import sys

with open('./files/day_6.txt', 'r') as f:
    declaration = f.read().strip().split("\n\n")

customs = sum([len(set(words.replace("\n", ""))) for words in declaration])

print("Part 1 of day 6 is: %s" % customs)


"""Answer part 1 : 6768"""