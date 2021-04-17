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

import re

with open('./files/day_4.txt', 'r') as f:
    passports = f.read().split('\n\n')
    f.close()

keys_part_1 = [
    'byr',  # (Birth Year)
    'iyr',  # (Issue Year)
    'eyr',  # (Expiration Year)
    'hgt',  # (Height)
    'hcl',  # (Hair Color)
    'ecl',  # (Eye Color)
    'pid'  # (Passport ID)
    # "cid", # (Country ID)
]

keys_part_2 = {
    'byr': r'byr:\s*(19[2-9]\d|200[0-2])\b',
    'iyr': r'iyr:\s*20(1\d|20)\b',
    'eyr': r'eyr:\s*20(2\d|30)\b',
    'hgt': r'hgt:\s*(1([5-8]\d|9[0-3])cm|(59|6\d|7[0-6])in)',
    'hcl': r'hcl:\s*#[0-9a-f]{6}\b',
    'ecl': r'ecl:\s*(amb|blu|brn|gry|grn|hzl|oth)\b',
    'pid': r'pid:\s*\d{9}\b'
    # "cid", # (Country ID) not checked
}


def separator_passport_part_1():
    """Looping all over the keys in a nested list comprehension"""
    valid_keys = sum([all([k in p for k in keys_part_1]) for p in passports])
    return valid_keys


def valid_passport_part_2():
    """Same as part 1, but using regex"""
    valid_data = sum([all([re.search(keys_part_2[k], p) for k in keys_part_2]) for p in passports])
    return valid_data


def main():
    print(f'Part 1: %d' % separator_passport_part_1())
    print(f'Part 2: %d' % valid_passport_part_2())


if __name__ == '__main__':
    main()

"""
Part 1: 230
Part 2: 156
"""