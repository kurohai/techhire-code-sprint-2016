#!/bin/python

import sys



test_cases = [
    ['blue'],
    ['red'],
    ['white'],
    ['white', 'blue'],
    ['white', 'white', 'blue'],
    ['white', 'white', 'white', 'blue'],
    ['white', 'white', 'white', 'white', 'blue'],
    ['white', 'red'],
    ['white', 'white', 'red'],
    ['white', 'white', 'white', 'red'],
    ['white', 'white', 'white', 'white', 'red'],
    ['red', 'white', 'blue'],
    ['red', 'white', 'white', 'blue'],
    ['blue', 'white', 'red'],
    ['blue', 'white', 'white', 'red'],
]

def this_happened_because_i_didnt_consider_starting_value(user_input):
    if user_input[0] == 'blue':
        return 0
    elif user_input[0] == 'red':
        return 1
    elif user_input[0] == 'white' and len(user_input) == 1:
        return 1

    for k, v in enumerate(user_input):
        if v != 'white':
            if k % 2 == 0 and v == 'red':
                return 1
            elif k % 2 == 0 and v == 'blue':
                # print 'failing test case'
                # print k, v
                return 0
            elif k % 2 != 0 and v == 'blue':
                return 1
            elif k % 2 != 0 and v == 'red':
                return 0


def fat_finger_user_input_gen(user_input):
    for c in user_input:
        yield c


def rain_man(color, card_count):
    if color is None:
        return card_count
    elif color == 'blue':
        card_count += 1
        return card_count
    elif color == 'red':
        card_count -= 1
        return card_count
    elif color == 'white' and card_count == 0:
        card_count += 1
        return card_count
    elif color == 'white' and card_count == 1:
        card_count -= 1
        # print 'this here card count', card_count
        return card_count
    return card_count


def main(user_input):
    # print 'start'
    card_count = this_happened_because_i_didnt_consider_starting_value(user_input)
    # print card_count
    gen = fat_finger_user_input_gen(user_input)
    color = next(gen, None)
    while color is not None:
        card_count = rain_man(color, card_count)
        # print card_count
        if card_count > 1 or card_count <= -1:
            print 'no'
            return
        if color is None:
            print 'yes'
            return
        color = next(gen, None)
    print 'yes'


if __name__ == '__main__':

    # n = int(raw_input().strip())
    # c = map(str,raw_input().strip().split(' '))
    # print type(c)
    for c in test_cases:
    # card_count = 0

        main(c)
