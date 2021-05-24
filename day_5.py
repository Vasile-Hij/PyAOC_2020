#!/usr/bin/env python3
"""
https://adventofcode.com/2020/day/5

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
"""

# Approaching method: using binary system F=0, B=1, R=1, L=0
with open('./files/day_5.txt', 'r') as f:
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


def main():
    #For each seat, convert it to binary, and grab the max in the array.
    print("Part 1: %s" % {max([int(s, 2) for s in flight_ticket_seat])})


if __name__ == '__main__':
    main()

"""
*Results*
Part 1: 866
Part 2: 
"""