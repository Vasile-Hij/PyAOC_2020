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

with open('./files/day_3.txt', 'r') as f:
    # Reading the list as strings
    map_ = list(map(str.strip, f.readlines()))
    f.close()
    # width of the map
the_map = len(map_[0])


def guidance_1_map(dx, dy):
    global the_map
    x, trees = 0, 0
    """when x increment, the result mod the width 
    to loop back on the left side of the map"""
    for y in range(0, len(map_), dy):
        if map_[y][x] == "#":
            trees += 1
        x = (x + dx) % the_map
    return trees


def guidance_2_map():
    slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    num_tree = math.prod([guidance_1_map(dx, dy) for dx, dy in slopes])
    return num_tree

def main():
    # print(f'Trees: %d' % guidance_1_map())
    print(f'Part 1: %d' % guidance_1_map(3, 1))
    print(f'Part 2: %d' % guidance_2_map())


if __name__ == '__main__':
    main()

"""
Part 1: 247
Part 2: 2983070376
"      ""