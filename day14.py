# preprocessing data
data = open("input/day14.txt").read().splitlines()
data = [line.split("->") for line in data]
data = [[x.strip().split(",") for x in line] for line in data]
data = [[[int(num) for num in pair] for pair in line] for line in data]
balance_x = 450
data = [[[pair[0] - balance_x, pair[1]] for pair in line] for line in data]
# %% With small sample
# data = open("input/day14_small.txt").read().splitlines()
# data = [line.split("->") for line in data]
# data = [[x.strip().split(",") for x in line] for line in data]
# data = [[[int(num) for num in pair] for pair in line] for line in data]
# balance_x = 490
# data = [[[pair[0] - balance_x, pair[1]] for pair in line] for line in data]
# %%

# flatten data
only_x = [item for line in data for pair in line for item in pair[:1]]
only_y = [item for line in data for pair in line for item in pair[1:]]
min_x, max_x = min(only_x), max(only_x)
min_y, max_y = min(only_y), max(only_y)
# %%
def create_wall_of_rock(ins):
    global table
    for index in range(len(ins)):
        if index == len(ins) - 1:
            break
        first = ins[index]
        next_ = ins[index + 1]
        if first[1] == next_[1]:
            # all point between with the same y
            for x in range(min(first[0], next_[0]), max(first[0], next_[0]) + 1):
                table[first[1]][x] = 1
        if first[0] == next_[0]:
            for y in range(min(first[1], next_[1]), max(first[1], next_[1]) + 1):
                table[y][first[0]] = 1


# %%  part 1
table = [[0 for x in range(max_x + 2)] for y in range(max_y + 2)]
for instruction in data:
    create_wall_of_rock(instruction)
# %%
from copy import deepcopy

drop_point = [500 - balance_x, 0]
void_deep = max_y + 1
count_sand_before_go_void = 0


def model_sand_drop():
    global table, drop_point, void_deep, count_sand_before_go_void
    current = deepcopy(drop_point)
    while True:
        x_current = current[0]
        y_current = current[1]
        # if below still empty, continue drop down
        if y_current >= void_deep:
            break
        if table[y_current + 1][x_current] == 0:
            current[1] += 1
        else:
            # if below is wall, check the left first
            if table[y_current + 1][x_current - 1] == 0:
                current[0] -= 1
                current[1] += 1
            else:
                # if the left is wall, check the right
                if table[y_current + 1][x_current + 1] == 0:
                    current[0] += 1
                    current[1] += 1
                else:
                    # if both left and right are wall, stop
                    count_sand_before_go_void += 1
                    break
    # return if this sand go to the void
    table[current[1]][current[0]] = 2
    # print(current)
    return current[1] >= void_deep


# %%
while True:
    if model_sand_drop():
        break
# %% part 2
from copy import deepcopy

drop_point = [500 - balance_x, 0]
real_void_deep = max_y + 2


def model_sand_drop2():
    global table, drop_point, void_deep
    current = deepcopy(drop_point)
    while True:
        x_current = current[0]
        y_current = current[1]
        # if below still empty, continue drop down
        if table[drop_point[1]][drop_point[0]] == 2:
            break
        if current[1] == real_void_deep - 1:
            break
        if table[y_current + 1][x_current] == 0:
            current[1] += 1
        else:
            # if below is wall, check the left first
            if table[y_current + 1][x_current - 1] == 0:
                current[0] -= 1
                current[1] += 1
            else:
                # if the left is wall, check the right
                if table[y_current + 1][x_current + 1] == 0:
                    current[0] += 1
                    current[1] += 1
                else:
                    # if both left and right are wall, stop
                    break
    table[current[1]][current[0]] = 2


# %% prepare table, the bottom maximum length is 2x of the (max_y + 1)
table = [[0 for x in range(2*(max_y + 2) + 1)] for y in range(max_y + 2)]
for instruction in data:
    create_wall_of_rock(instruction)
#%%
while True:
    if table[drop_point[1]][drop_point[0]] == 2:
        break
    model_sand_drop2()
#%%
sum([line.count(2) for line in table])
# %%
from pandas import DataFrame
import seaborn as sns

df = DataFrame(table)
sns.heatmap(df)
# %%
