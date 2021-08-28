#!/usr/bin/env python3
"""
https://adventofcode.com/2020/day/3

Part 1 is checking how many trees encountered on the way to bottom
 using the rule: right 3, down 1.
Part 2 is using 5 different* trajectories on the way to bottom,
 so the trees that we will encounter, we will multiply together.
 * - right 1, down 1; right 3, down 1 (checked already); right 5, down 1;
  right 7, down 1; and  right 1, down 2.
"""

import math
import os
import logging
from datetime import datetime


run_time = datetime.now()

name = "".join("day_" + os.path.splitext(os.path.basename(__file__))[0])
logger = logging.getLogger(name)
logging.basicConfig(level=logging.INFO)

output_handler = logging.FileHandler('./output/aoc.txt')
output_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(name)s - %(message)s')
output_handler.setFormatter(output_formatter)
logger.addHandler(output_handler)


with open('./input/3.txt', 'r') as f:
    # Reading the list as strings
    map_ = list(map(str.strip, f.readlines()))
    f.close()
    # width of the map
the_map = len(map_[0])


def part_1(dx, dy):
    global the_map
    x, trees = 0, 0
    """when x increment, the result mod the width 
    to loop back on the left side of the map"""
    for y in range(0, len(map_), dy):
        if map_[y][x] == "#":
            trees += 1
        x = (x + dx) % the_map
    return trees


def part_2():
    slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    num_tree = math.prod([part_1(dx, dy) for dx, dy in slopes])
    return num_tree


def main():
    logger.info(f'Part 1 of {name} is {part_1(3, 1)}. Runtime {datetime.now()-run_time}')
    logger.info(f'Part 2 of {name} is {part_2()}. Runtime {datetime.now()-run_time}')


if __name__ == '__main__':
    main()
