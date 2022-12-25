data = open('input/day11_small.txt').read().split('\n\n')
#%%
import re
monkeys = []
for index,paragraph in enumerate(data):
    print(f"Paragraph {index}")
    lines = paragraph.splitlines()
    monkey = int(lines[0].replace('Monkey ', '').replace(':', '').strip())
    starting_items = list(map(int,lines[1].strip().replace('Starting items: ', '').strip().split(', ')))
    # extract operator and second operand in form old * 7
    operator, operant = re.search(r"old (\*|\+) (.*)",lines[2].replace("Operation: new = ","")).groups()
    if operant == "old":
        operator = lambda x: x*x
    if operator == '*':
        operator = lambda x: x * int(operant)
    elif operator == '+':
        operator = lambda x: x + int(operant)
    test_digit = int(lines[3].strip().replace('Test: divisible by ', ''))
    test = lambda x: x % test_digit == 0
    next_monkeys = [int(lines[4].strip().replace("If true: throw to monkey ", '').strip())
                    ,
                    int(lines[5].strip().replace("If false: throw to monkey ", '').strip())]
    monkeys.append([ monkey, starting_items,operator, test, next_monkeys ])

def proper_round(num, dec=0):
    num = str(num)[:str(num).index('.')+dec+2]
    if num[-1]>='5':
        return float(num[:-2-(not dec)]+str(int(num[-2-(not dec)])+1))
    return float(num[:-1])
#%%
# Monkey 0:
#   Starting items: 89, 95, 92, 64, 87, 68
#   Operation: new = old * 11
#   Test: divisible by 2
#     If true: throw to monkey 7
#     If false: throw to monkey 4
#
# Monkey 1:
#   Starting items: 87, 67
#   Operation: new = old + 1
#   Test: divisible by 13
#     If true: throw to monkey 3
#     If false: throw to monkey 6
#
# Monkey 2:
#   Starting items: 95, 79, 92, 82, 60
#   Operation: new = old + 6
#   Test: divisible by 3
#     If true: throw to monkey 1
#     If false: throw to monkey 6
#
# Monkey 3:
#   Starting items: 67, 97, 56
#   Operation: new = old * old
#   Test: divisible by 17
#     If true: throw to monkey 7
#     If false: throw to monkey 0
#
# Monkey 4:
#   Starting items: 80, 68, 87, 94, 61, 59, 50, 68
#   Operation: new = old * 7
#   Test: divisible by 19
#     If true: throw to monkey 5
#     If false: throw to monkey 2
#
# Monkey 5:
#   Starting items: 73, 51, 76, 59
#   Operation: new = old + 8
#   Test: divisible by 7
#     If true: throw to monkey 2
#     If false: throw to monkey 1
#
# Monkey 6:
#   Starting items: 92
#   Operation: new = old + 5
#   Test: divisible by 11
#     If true: throw to monkey 3
#     If false: throw to monkey 0
#
# Monkey 7:
#   Starting items: 99, 76, 78, 76, 79, 90, 89
#   Operation: new = old + 7
#   Test: divisible by 5
#     If true: throw to monkey 4
#     If false: throw to monkey 5
# import math


from copy import deepcopy
monkey_balls_track = [deepcopy(monkey[1]) for monkey in monkeys]
monkey_inspect = [0 for _ in range(len(monkey_balls_track))]
# monkey 0
def monkey_0():
    while monkey_balls_track[0]:
        ball = monkey_balls_track[0].pop()
        worry  = (ball * 11)//3
        monkey_inspect[0] += 1
        if worry % 2 == 0:
            monkey_balls_track[7].append(worry)
        else:
            monkey_balls_track[4].append(worry)

def monkey_1():
    while monkey_balls_track[1]:
        ball = monkey_balls_track[1].pop()
        worry  = (ball + 1)//3
        monkey_inspect[1] += 1
        if worry % 13 == 0:
            monkey_balls_track[3].append(worry)
        else:
            monkey_balls_track[6].append(worry)

def monkey_2():
    while monkey_balls_track[2]:
        ball = monkey_balls_track[2].pop()
        worry  = (ball + 6)//3
        monkey_inspect[2] += 1
        if worry % 3 == 0:
            monkey_balls_track[1].append(worry)
        else:
            monkey_balls_track[6].append(worry)

def monkey_3():
    while monkey_balls_track[3]:
        ball = monkey_balls_track[3].pop()
        worry  = (ball * ball)//3
        monkey_inspect[3] += 1
        if worry % 17 == 0:
            monkey_balls_track[7].append(worry)
        else:
            monkey_balls_track[0].append(worry)

def monkey_4():
    while monkey_balls_track[4]:
        ball = monkey_balls_track[4].pop()
        worry  = (ball * 7)//3
        monkey_inspect[4] += 1
        if worry % 19 == 0:
            monkey_balls_track[5].append(worry)
        else:
            monkey_balls_track[2].append(worry)

def monkey_5():
    while monkey_balls_track[5]:
        ball = monkey_balls_track[5].pop()
        worry  = (ball + 8)//3
        monkey_inspect[5] += 1
        if worry % 7 == 0:
            monkey_balls_track[2].append(worry)
        else:
            monkey_balls_track[1].append(worry)

def monkey_6():
    while monkey_balls_track[6]:
        ball = monkey_balls_track[6].pop()
        worry  = (ball + 5)//3
        monkey_inspect[6] += 1
        if worry % 11 == 0:
            monkey_balls_track[3].append(worry)
        else:
            monkey_balls_track[0].append(worry)

def monkey_7():
    while monkey_balls_track[7]:
        ball = monkey_balls_track[7].pop()
        worry  = (ball + 7)//3
        monkey_inspect[7] += 1
        if worry % 5 == 0:
            monkey_balls_track[4].append(worry)
        else:
            monkey_balls_track[5].append(worry)

r = 0
while True:
    r += 1
    monkey_0()
    monkey_1()
    monkey_2()
    monkey_3()
    monkey_4()
    monkey_5()
    monkey_6()
    monkey_7()
    if r  == 20:
        print(r, monkey_inspect)
        break
#%%
# Monkey 0:
#   Starting items: 79, 98
#   Operation: new = old * 19
#   Test: divisible by 23
#     If true: throw to monkey 2
#     If false: throw to monkey 3
#
# Monkey 1:
#   Starting items: 54, 65, 75, 74
#   Operation: new = old + 6
#   Test: divisible by 19
#     If true: throw to monkey 2
#     If false: throw to monkey 0
#
# Monkey 2:
#   Starting items: 79, 60, 97
#   Operation: new = old * old
#   Test: divisible by 13
#     If true: throw to monkey 1
#     If false: throw to monkey 3
#
# Monkey 3:
#   Starting items: 74
#   Operation: new = old + 3
#   Test: divisible by 17
#     If true: throw to monkey 0
#     If false: throw to monkey 1
# from copy import deepcopy
# monkey_balls_track = [deepcopy(monkey[1]) for monkey in monkeys]
# monkey_inspect = [0 for _ in range(len(monkey_balls_track))]
# def monkey_0():
#     while monkey_balls_track[0]:
#         ball = monkey_balls_track[0].pop()
#         worry  = (ball * 19)//3
#         monkey_inspect[0] += 1
#         if worry % 23 == 0:
#             monkey_balls_track[2].append(worry)
#         else:
#             monkey_balls_track[3].append(worry)
#
# def monkey_1():
#     while monkey_balls_track[1]:
#         ball = monkey_balls_track[1].pop()
#         worry  = (ball + 6)//3
#         monkey_inspect[1] += 1
#         if worry % 19 == 0:
#             monkey_balls_track[2].append(worry)
#         else:
#             monkey_balls_track[0].append(worry)
#
# def monkey_2():
#     while monkey_balls_track[2]:
#         ball = monkey_balls_track[2].pop()
#         worry  = (ball * ball)//3
#         monkey_inspect[2] += 1
#         if worry % 13 == 0:
#             monkey_balls_track[1].append(worry)
#         else:
#             monkey_balls_track[3].append(worry)
#
# def monkey_3():
#     while monkey_balls_track[3]:
#         ball = monkey_balls_track[3].pop()
#         worry  = (ball + 3)//3
#         monkey_inspect[3] += 1
#         if worry % 17 == 0:
#             monkey_balls_track[0].append(worry)
#         else:
#             monkey_balls_track[1].append(worry)
r = 0
while True:
    r += 1
    monkey_0()
    monkey_1()
    monkey_2()
    monkey_3()
    if r  == 20:
        print(r, monkey_inspect)
        break
#%%
#%% part 2 Using chinese remainder theorem to reduce the ball worry before throwing to other monkey
# from copy import deepcopy
# monkey_balls_track = [deepcopy(monkey[1]) for monkey in monkeys]
# monkey_inspect = [0 for _ in range(len(monkey_balls_track))]
# # monkey 0
# def monkey_0():
#     while monkey_balls_track[0]:
#         ball = monkey_balls_track[0].pop()
#         worry  = (ball * 11)
#         monkey_inspect[0] += 1
#         if worry % 2 == 0:
#             worry = worry % (2 * 5)
#             monkey_balls_track[7].append(worry)
#         else:
#             monkey_balls_track[4].append(worry)
#
# def monkey_1():
#     while monkey_balls_track[1]:
#         ball = monkey_balls_track[1].pop()
#         worry  = (ball + 1)
#         monkey_inspect[1] += 1
#         if worry % 13 == 0:
#             worry = worry % (13 * 17)
#             monkey_balls_track[3].append(worry)
#         else:
#             monkey_balls_track[6].append(worry)
#
# def monkey_2():
#     while monkey_balls_track[2]:
#         ball = monkey_balls_track[2].pop()
#         worry  = (ball + 6)
#         monkey_inspect[2] += 1
#         if worry % 3 == 0:
#             worry = worry % (3 * 13)
#             monkey_balls_track[1].append(worry)
#         else:
#             monkey_balls_track[6].append(worry)
#
# def monkey_3():
#     while monkey_balls_track[3]:
#         ball = monkey_balls_track[3].pop()
#         worry  = (ball * ball)
#         monkey_inspect[3] += 1
#         if worry % 17 == 0:
#             worry = worry % (17 * 5)
#             monkey_balls_track[7].append(worry)
#         else:
#             monkey_balls_track[0].append(worry)
#
# def monkey_4():
#     while monkey_balls_track[4]:
#         ball = monkey_balls_track[4].pop()
#         worry  = (ball * 7)
#         monkey_inspect[4] += 1
#         if worry % 19 == 0:
#             worry = worry % (19 * 7)
#             monkey_balls_track[5].append(worry)
#         else:
#             monkey_balls_track[2].append(worry)
#
# def monkey_5():
#     while monkey_balls_track[5]:
#         ball = monkey_balls_track[5].pop()
#         worry  = (ball + 8)
#         monkey_inspect[5] += 1
#         if worry % 7 == 0:
#             worry = worry % (7 * 3)
#             monkey_balls_track[2].append(worry)
#         else:
#             monkey_balls_track[1].append(worry)
#
# def monkey_6():
#     while monkey_balls_track[6]:
#         ball = monkey_balls_track[6].pop()
#         worry  = (ball + 5)
#         monkey_inspect[6] += 1
#         if worry % 11 == 0:
#             monkey_balls_track[3].append(worry)
#         else:
#             monkey_balls_track[0].append(worry)
#
# def monkey_7():
#     while monkey_balls_track[7]:
#         ball = monkey_balls_track[7].pop()
#         worry  = (ball + 7)
#         monkey_inspect[7] += 1
#         if worry % 5 == 0:
#             monkey_balls_track[4].append(worry)
#         else:
#             monkey_balls_track[5].append(worry)
#
# r = 0
# while True:
#     r += 1
#     monkey_0()
#     monkey_1()
#     monkey_2()
#     monkey_3()
#     monkey_4()
#     monkey_5()
#     monkey_6()
#     monkey_7()
#     if r  == 1000:
#         print(r, monkey_inspect)
#         break
#

#%%
from copy import deepcopy
monkey_balls_track = [deepcopy(monkey[1]) for monkey in monkeys]
monkey_inspect = [0 for _ in range(len(monkey_balls_track))]
def monkey_0():
    while monkey_balls_track[0]:
        ball = monkey_balls_track[0].pop()
        worry  = (ball * 19)//3
        monkey_inspect[0] += 1
        if worry % 23 == 0:
            # worry = worry % (23 * 13)
            monkey_balls_track[2].append(worry)
        else:
            monkey_balls_track[3].append(worry)

def monkey_1():
    while monkey_balls_track[1]:
        ball = monkey_balls_track[1].pop()
        worry  = (ball + 6)//3
        monkey_inspect[1] += 1
        if worry % 19 == 0:
            # worry = worry % (19 * 13)
            monkey_balls_track[2].append(worry)
        else:
            monkey_balls_track[0].append(worry)

def monkey_2():
    while monkey_balls_track[2]:
        ball = monkey_balls_track[2].pop()
        worry  = (ball * ball)//3
        monkey_inspect[2] += 1
        if worry % 13 == 0:
            # worry = worry % (13 * 19)
            monkey_balls_track[1].append(worry)
        else:
            monkey_balls_track[3].append(worry)

def monkey_3():
    while monkey_balls_track[3]:
        ball = monkey_balls_track[3].pop()
        worry  = (ball + 3)//3
        monkey_inspect[3] += 1
        if worry % 17 == 0:
            # worry = worry % (17 * 23)
            monkey_balls_track[0].append(worry)
        else:
            monkey_balls_track[1].append(worry)
r = 0
while True:
    r += 1
    monkey_0()
    monkey_1()
    monkey_2()
    monkey_3()
    # module all the ball worry in each monkey by their divisor every 20 round
    if r % 20 == 0:
        monkey_balls_track = [[ball % (17 * 13 * 19 * 23)
                               for ball in monkey
                               ] for monkey in monkey_balls_track]
    if r  == 1000 :
        print(r, monkey_inspect)
        break

#%%
