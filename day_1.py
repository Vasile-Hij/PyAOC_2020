'''
https://adventofcode.com/2020/day/1
'''

with open('./files/day_1.txt', 'r') as textinput:
    expenses = textinput.readlines()

numbers = [int(line.strip()) for line in expenses]


def task1(list):
    for number_1 in list:
        number_2 = 2020 - number_1
        if number_2 in list:
            answer = number_1 * number_2
            print(answer)
            break

def task2(list):
    for number_1 in list:
        for number_2 in list:
            for number_3 in list:
                if number_1 + number_2 + number_3 == 2020:
                    answer = number_1 * number_2 * number_3
                    print(answer)
                    break

task1(numbers)
task2(numbers)

'''
Part one: Your puzzle answer was 969024.
Part two: Your puzzle answer was 230057040.
'''