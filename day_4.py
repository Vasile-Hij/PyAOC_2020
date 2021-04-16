#!/usr/bin/env python3
"""https://adventofcode.com/2020/day/4

Passport data is validated in batch files (your puzzle input).
Each passport is represented as a sequence of key:value pairs separated by spaces or newlines.
Passports are separated by blank lines.

E.g.
ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
byr:1937 iyr:2017 cid:147 hgt:183cm

iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
hcl:#cfa07d byr:1929
"""

with open('./files/day_4.txt', 'r') as f:
    passports = f.read().split('\n\n')
    f.close()

keys = [
    'byr',  # (Birth Year)
    'iyr',  # (Issue Year)
    'eyr',  # (Expiration Year)
    'hgt',  # (Height)
    'hcl',  # (Hair Color)
    'ecl',  # (Eye Color)
    'pid'  # (Passport ID)
]


def separator_passport_part_1():
    valid_keys = sum([all([k in p for k in keys]) for p in passports])
    return valid_keys


def valid_passport_part_2():
    pass


def main():
    print(f'Part 1: %d' % separator_passport_part_1())
    print(f'Part 2: %d' % valid_passport_part_2())


if __name__ == '__main__':
    main()
