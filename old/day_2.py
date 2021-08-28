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

with open('./files/day_2.txt', 'r') as f:
    passwords = f.read().splitlines()
    f.close()

total = len(passwords)
valid = 0


def day_2_part_1():
    global valid

    for x in passwords:
        numbers, letter, valid_pass = x.split(" ")
        lower, higher = numbers.split("-")
        letters = letter.split(":")[0]
        counter = valid_pass.count(letters)
        # print(lower, higher, letters, valid_pass, counter)
        if int(lower) <= counter <= int(higher):
            valid += 1

    print(f'Valid passwords: %d ' % valid)
    print(f'Total passwords: %d' % total)


def day_2_part_2():
    global valid

    for x in passwords:
        number, letter, valid_pass = x.split(' ')
        lower, higher = map(int, number.split('-'))
        password_1 = valid_pass[lower-1] == letter[0]
        password_2 = valid_pass[higher-1] == letter[0]

        if password_1 != password_2:
            valid += 1

    print(f'Valid passwords: %d' % valid)
    print(f'Total passwords: %d' % total)


def passwords_policy():
    print(f'Password validated with passwords policy!')
    day_2_part_1()
    print()
    print(f'Updated password policy according Toboggan Corporate Policies.')
    day_2_part_2()


if __name__ == '__main__':
    passwords_policy()

"""
Part 1
Output:
Valid passwords: 524 
Total passwords: 1000

Part 2
Valid passwords: 485
"""