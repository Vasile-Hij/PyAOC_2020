#!/usr/bin/env python3
"""
https://adventofcode.com/2020/day/1
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


with open('./input/1.txt', 'r') as text_input:
    expenses = text_input.readlines()
nums = [int(line.strip()) for line in expenses]
text_input.close()


def part_1(num):
    """Find the distinct numbers that sum to 2020, and return their product"""
    for num_1 in num:
        num_2 = 2020 - num_1
        if num_2 in num:
            answer = num_1 * num_2
            return answer
            

def part_2(num):
    """Find the distinct numbers that sum to 2020, and return their product"""
    for num_1 in num:
        for num_2 in num:
            for num_3 in num:
                if num_1 + num_2 + num_3 == 2020:
                    answer = num_1 * num_2 * num_3
                    return answer
                    

def main():
    logger.info(f"Part 1 of {name} is {part_1(nums)}. Runtime {datetime.now()-run_time}")
    logger.info(f"Part 2 of {name} is {part_2(nums)}. Runtime {datetime.now()-run_time}")


if __name__ == '__main__':
    main()
