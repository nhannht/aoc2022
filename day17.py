from typing import List

data = open('input/day17.txt').read()
data = [symbol for symbol in data]
# %%
chamber = [[0 for wide in range(7)] for high in range(2000*2 )]


# %%
def get_highest_height_of_rock_in_chamber():
    for index, line in enumerate(chamber):
        count_rock_in_current_height = line.count(1)
        count_rock_in_higher_height = chamber[index + 1].count(1)
        if index == 0 and count_rock_in_current_height == 0:
            return -1
        if count_rock_in_current_height > 0 and count_rock_in_higher_height == 0:
            return index


def model_the_block_fall(instruction: str):
    global block
    touch = False
    # block store x and y
    # of all atom in the block corresponding to the chamber
    # the tetris block is the horizon I line
    if instruction == '>':
        most_right = max([atom[1] for atom in block])
        if most_right < 6:
            if not any([chamber[atom[0]][atom[1] + 1] == 1 for atom in block]):
                for atom_ in block:
                    atom_[1] += 1
    if instruction == '<':
        most_left = min([atom[1] for atom in block])
        if most_left > 0:
            if not any([chamber[atom[0]][atom[1] - 1] == 1 for atom in block]):
                for atom_ in block:
                    atom_[1] -= 1
    # print(f"Block pos after {instruction} is {block}")
    # move down
    for atom_ in block:
        atom_[0] -= 1
    # check if block touch any rock
    if any([chamber[atom[0]][atom[1]] == 1 for atom in block]):
        touch = True
        # roll back the block
        for atom_ in block:
            atom_[0] += 1
            chamber[atom_[0]][atom_[1]] = 1
        return touch
    # check if block touch the bottom
    if any([atom[0] < 0 for atom in block]):
        touch = True
        # roll back the block
        for atom_ in block:
            atom_[0] += 1
            chamber[atom_[0]][atom_[1]] = 1
        return touch

    return touch


# %%
from itertools import cycle

blocks_num = cycle([1, 2, 3, 4, 5])
instructions = cycle(data)
# %%
block: list[List] = []
highest_height = 0


def move_block_until_touch(block_num):
    global count_block, block, highest_height
    highest_height = get_highest_height_of_rock_in_chamber() + 4
    # print(highest_height)

    if block_num == 1:
        block = [[highest_height, 2], [highest_height, 3], [highest_height, 4], [highest_height, 5]]
    # the tetris block is cross
    elif block_num == 2:
        block = [[highest_height + 2, 3],
                 [highest_height + 1, 2], [highest_height + 1, 3], [highest_height + 1, 4],
                 [highest_height, 3]]
    # the tetris block is the vertical mirrored L line
    elif block_num == 3:
        block = [[highest_height + 2, 4],
                 [highest_height + 1, 4],
                 [highest_height, 2], [highest_height, 3], [highest_height, 4]]
    # if block is vertical I
    elif block_num == 4:
        block = [[highest_height + 3, 2],
                 [highest_height + 2, 2],
                 [highest_height + 1, 2],
                 [highest_height, 2]]
    # if block is the square
    elif block_num == 5:
        block = [[highest_height + 1, 2], [highest_height + 1, 3],
                 [highest_height, 2], [highest_height, 3]]
    while True:
        if model_the_block_fall(next(instructions)):
            break


# %%
from pprint import pprint
output = []
count_block = 0
while True:
    count_block += 1
    next_block = next(blocks_num)
    # if count_block == 98:
    #     pprint(chamber[::-1])
    move_block_until_touch(next_block)
    # Debug chamber status
    # chammber_extract = chamber[:highest_height + 1]
    # pprint(chammber_extract[::-1])
    #
    # print('\n')
    height = get_highest_height_of_rock_in_chamber()+1
    output.append([count_block,block,height])
    if count_block == 2300:
        break
#%%
# from pandas import DataFrame
# df = DataFrame(output,columns=['block','block_pos','height'])


#%%
# use sklearn to  predict height from block number
# from sklearn.linear_model import LinearRegression,LogisticRegression
# from sklearn.model_selection import train_test_split
# from sklearn.metrics import mean_squared_error
# from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error
# X =  df['block'].values.reshape(-1,1)
# y = df['height']
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
# model = LinearRegression()