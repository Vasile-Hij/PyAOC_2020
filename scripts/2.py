#!/usr/bin/env python3
"""
https://adventofcode.com/2020/day/2

Part 1
Each line gives the password policy and then the password. The password policy indicates
the lowest and highest number of times a given letter must appear for the password to be valid.
For example, 1-3 a means that the password must contain a at least 1 time and at most 3 times.
How many passwords are valid according to their policies?
1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc


Part 2
Each policy actually describes two positions in the password,
where 1 means the first character, 2 means the second character, and so on.
(Be careful; Toboggan Corporate Policies have no concept of "index zero"!)
Exactly one of these positions must contain the given letter.
Other occurrences of the letter are irrelevant for the purposes of policy enforcement.

1-3 a: abcde is valid: position 1 contains a and position 3 does not.
1-3 b: cdefg is invalid: neither position 1 nor position 3 contains b.
2-9 c: ccccccccc is invalid: both position 2 and position 9 contain c.
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


with open('./input/2.txt', 'r') as f:
    passwords = f.read().splitlines()
    f.close()

total = len(passwords)
valid = 0

# Password validated with passwords policy!
def part_1():
    global valid

    for x in passwords:
        numbers, letter, valid_pass = x.split(" ")
        lower, higher = numbers.split("-")
        letters = letter.split(":")[0]
        counter = valid_pass.count(letters)
        # print(lower, higher, letters, valid_pass, counter)
        if int(lower) <= counter <= int(higher):
            valid += 1
    return valid


# Updated password policy according Toboggan Corporate Policies.
def part_2():
    global valid

    for x in passwords:
        number, letter, valid_pass = x.split(' ')
        lower, higher = map(int, number.split('-'))
        password_1 = valid_pass[lower-1] == letter[0]
        password_2 = valid_pass[higher-1] == letter[0]
        if password_1 != password_2:
            valid += 1
    return valid


def main():
    logger.info(f'Part 1 of {name} is {part_1()}. Runtime {datetime.now()-run_time}')
    logger.info(f'Part 2 of {name} is {part_2()}. Runtime {datetime.now()-run_time}')


if __name__ == '__main__':
    main()
