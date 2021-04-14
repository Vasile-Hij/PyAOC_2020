#!/usr/bin/env python3
"""
https://adventofcode.com/2020/day/1
"""

def main():
    with open('./files/day_1.txt', 'r') as text_input:
        expenses = text_input.readlines()

    nums = [int(line.strip()) for line in expenses]


    def day1_1(num):
        """Find the distinct numbers that sum to 2020, and return their product"""
        for num_1 in num:
            num_2 = 2020 - num_1
            if num_2 in num:
                answer = num_1 * num_2
                print(answer)
                break


    def day1_2(num):
        """Find the distinct numbers that sum to 2020, and return their product"""
        for num_1 in num:
            for num_2 in num:
                for num_3 in num:
                    if num_1 + num_2 + num_3 == 2020:
                        answer = num_1 * num_2 * num_3
                        print(answer)
                        break


    day1_1(nums)
    day1_2(nums)

if __name__ == '__main__':
    main()

"""
Part one: Your puzzle answer was 969024.
Part two: Your puzzle answer was 230057040.
"""