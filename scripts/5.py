#!/usr/bin/env python3
"""
https://adventofcode.com/2020/day/5

Part I:
This challenge consists in finding seat in airplane where airport terminal are using
binary space partitioning, so FBFBBFFRLR, where F means "front", B means "back",
L means "left", and R means "right".

The first 7 characters will either be F or B from 0 to 127.
The last 3 characters will either be R or L from 0 to 7.

'FBFBBFFRLR' ticket means:
F means to take the lower half, keeping rows 0 through 63.
B means to take the upper half, keeping rows 32 through 63.
F means to take the lower half, keeping rows 32 through 47.
B means to take the upper half, keeping rows 40 through 47.
B keeps rows 44 through 47.
F keeps rows 44 through 45.
The final F keeps the lower of the two, row 44.

R means to take the upper half, keeping columns 4 through 7.
L means to take the lower half, keeping columns 4 through 5.
The final R keeps the upper of the two, column 5.

So, decoding FBFBBFFRLR reveals that it is the seat at row 44, column 5, multiply by 8.
ID: 44 * 8 + 5 = 357


Part II:
Some of the seats at the very front and back of the plane don't exist on this aircraft,
so they'll be missing from your list as well.
Your seat wasn't at the very front or back, though; the seats with IDs +1 and -1
from yours will be in your list.
What is the ID of your seat?
"""

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


# Approaching method: using binary system F=0, B=1, R=1, L=0
with open('./input/5.txt', 'r') as f:
    flight_ticket_seat = (
        f.read()
        .strip()
        .replace('B', '1')
        .replace('F', '0')
        .replace('R', '1')
        .replace('L', '0')
        .split('\n')
    )
    f.close()


def part_1():
    occupied_seats = set([int(s, 2) for s in flight_ticket_seat])
    return occupied_seats


def part_2():
    occupied_seats = part_1()
    allseats = set(range(128 * 8))
    openseats = allseats - occupied_seats
    myseat = [seat for seat in openseats 
    if seat + 1 not in openseats and seat - 1 not in openseats]
    return myseat[0]


def main():
    
    logger.info(f"Part 1 of {name} is {max(part_1())}. Runtime {datetime.now()-run_time}")
    logger.info(f"Part 2 of {name} is {part_2()}. Runtime {datetime.now()-run_time}")


if __name__ == '__main__':
    main()
