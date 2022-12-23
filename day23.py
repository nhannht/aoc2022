input = open('input/day23.txt').read().splitlines()
# %%
from collections import deque

directions = deque(["N", "S", "W", "E"])

# %%
from copy import deepcopy


def expand_garden(garden_):
    """
    The create_new_garden function takes the garden list and adds 2 blank rows and columns to each side of the garden.
    The new_garden list is returned.

    Args:

    Returns:
        A new garden with an extra row and column of '

    Doc Author:
        Trelent
    """
    new_garden_ = [['.' for i in range(len(garden_[0]) + 2)]]
    for row in garden_:
        new_row = ['.']
        new_row.extend(row)
        new_row.append('.')
        new_garden_.append(new_row)
    new_garden_.append(['.' for i in range(len(garden_[0]) + 2)])
    return new_garden_


def locations_of_all_elves(garden_):
    global elves
    elves = []
    for i in range(len(garden_)):
        for j in range(len(garden_[0])):
            if garden_[i][j] == '#':
                elves.append([i, j, i, j])


# %%
def propose_new_location(elf, garden_):
    # if all 8 slot around is empty, not doing anything
    if garden_[elf[0] - 1][elf[1]] == '.' \
            and garden_[elf[0] + 1][elf[1]] == '.' \
            and garden_[elf[0]][elf[1] - 1] == '.' \
            and garden_[elf[0]][elf[1] + 1] == '.' \
            and garden_[elf[0] - 1][elf[1] - 1] == '.' \
            and garden_[elf[0] - 1][elf[1] + 1] == '.' \
            and garden_[elf[0] + 1][elf[1] - 1] == '.' \
            and garden_[elf[0] + 1][elf[1] + 1] == '.':
        return
    for direction in directions:
        if direction == 'N':
            # check all 3 squares above is empty or not
            if garden_[elf[0] - 1][elf[1]] == '.' and garden_[elf[0] - 1][elf[1] - 1] == '.' and \
                    garden_[elf[0] - 1][elf[1] + 1] == '.':
                elf[2] = elf[0] - 1
                elf[3] = elf[1]
                return
        elif direction == 'S':
            # check all 3 squares below is empty or not
            if garden_[elf[0] + 1][elf[1]] == '.' and garden_[elf[0] + 1][elf[1] - 1] == '.' and \
                    garden_[elf[0] + 1][elf[1] + 1] == '.':
                elf[2] = elf[0] + 1
                elf[3] = elf[1]
                return
        elif direction == 'W':
            # check all 3 squares left is empty or not
            if garden_[elf[0]][elf[1] - 1] == '.' and garden_[elf[0] - 1][elf[1] - 1] == '.' and \
                    garden_[elf[0] + 1][elf[1] - 1] == '.':
                elf[2] = elf[0]
                elf[3] = elf[1] - 1
                return
        elif direction == 'E':
            # check all 3 squares right is empty or not
            if garden_[elf[0]][elf[1] + 1] == '.' and garden_[elf[0] - 1][elf[1] + 1] == '.' and \
                    garden_[elf[0] + 1][elf[1] + 1] == '.':
                elf[2] = elf[0]
                elf[3] = elf[1] + 1
                return


def check_if_two_elf_propose_same_location():
    """if two elf propose same location, they will not move, change their propose location to their current location"""
    global elves
    for i in range(len(elves)):
        for j in range(i + 1, len(elves)):
            if elves[i][2] == elves[j][2] and elves[i][3] == elves[j][3]:
                elves[i][2] = elves[i][0]
                elves[i][3] = elves[i][1]
                elves[j][2] = elves[j][0]
                elves[j][3] = elves[j][1]


# %%
# %%
# check round 1
def each_round(garden_):
    """Update all location for each elf in elves list and return new garden"""
    global directions
    # first half of round
    global elves
    for elf in elves:
        propose_new_location(elf, garden_)
    # second half of round
    check_if_two_elf_propose_same_location()
    for elf in elves:
        garden_[elf[0]][elf[1]] = '.'
        garden_[elf[2]][elf[3]] = '#'
    # rotate direction
    directions.rotate(-1)
    return garden_


# %% Now, repeat in 10 rows
# elves = []
# garden = [[i for i in line] for line in input]
# for round_ in range(10):
#     garden = expand_garden(garden)
#     locations_of_all_elves(garden)
#     garden = each_round(garden)
#%% get the smallest retangle with include all elves
# def get_smallest_rectangle(garden_):
#     """return the smallest rectangle with include all elves"""
#     min_row = 100
#     max_row = 0
#     min_col = 100
#     max_col = 0
#     for i in range(len(garden_)):
#         for j in range(len(garden_[0])):
#             if garden_[i][j] == '#':
#                 if i < min_row:
#                     min_row = i
#                 if i > max_row:
#                     max_row = i
#                 if j < min_col:
#                     min_col = j
#                 if j > max_col:
#                     max_col = j
#     return min_row, max_row, min_col, max_col
# x_min, x_max, y_min, y_max = get_smallest_rectangle(garden)
# blank_in_rectangle = 0
# for i in range(x_min, x_max + 1):
#     for j in range(y_min, y_max + 1):
#         if garden[i][j] == '.':
#             blank_in_rectangle += 1
# %%
# with open('output/day23.out', 'w') as f:
#     for row in garden :
#         f.write(''.join(row))
#         f.write('\n')
# %% part 2
from copy import deepcopy
elves = []
result_part_2=0
garden = [[i for i in line] for line in input]
round_ = 0
while True:
    round_ += 1
    print(round_)
    garden = expand_garden(garden)
    locations_of_all_elves(garden)
    garden = each_round(garden)
    if all([elf[0] == elf[2] and elf[1] == elf[3] for elf in elves]):
        result_part_2 = round_
        break
print(result_part_2)
#%%
