# day 22
data = open('input/day22.txt').read().splitlines()
field = data[:-2]
import re

instructions = [e for e in re.split(r'(\d+)', data[-1]) if e not in ['', ' ']]

max_len = max([len(line) for line in field])
# append blank space to make all lines the same length
field = [line + ' ' * (max_len - len(line)) for line in field]
field = [[col for col in line] for line in field]


# %%
# current_pos = [0, field[0].index('.')]
# current_direction = "right"


def move_one_step():
    global current_direction, current_pos
    row_next, col_next = None, None
    if current_direction == "right":
        col_next = current_pos[1] + 1
        row_next = current_pos[0]
        # if next pos is outsize the field, wrap around other size
        if col_next >= len(field[0]):
            while True:
                col_next -= 1
                if col_next == -1:
                    col_next = 0
                    break
                elif field[row_next][col_next] == ' ':
                    col_next += 1
                    break
            # if next pos is a walk, return to the original pos
            if field[row_next][col_next] == '#':
                return current_pos[0], current_pos[1]
        elif field[row_next][col_next] == ' ':
            while True:
                col_next -= 1
                if col_next == -1:
                    col_next = 0
                    break
                elif field[row_next][col_next] == ' ':
                    col_next += 1
                    break
            # if next pos is a walk, return to the original pos
            if field[row_next][col_next] == '#':
                return current_pos[0], current_pos[1]

        elif field[row_next][col_next] == '#':
            return current_pos[0], current_pos[1]


    elif current_direction == "left":
        col_next = current_pos[1] - 1
        row_next = current_pos[0]
        # if next pos is outsize the field, wrap around other size
        if col_next < 0:
            while True:
                col_next += 1
                if col_next == len(field[0]):
                    col_next = len(field[0]) - 1
                    break
                elif field[row_next][col_next] == ' ':
                    col_next -= 1
                    break
            # if next pos is a walk, return to the original pos
            if field[row_next][col_next] == '#':
                return current_pos[0], current_pos[1]
        elif field[row_next][col_next] == ' ':
            while True:
                col_next += 1
                if col_next == len(field[0]):
                    col_next = len(field[0]) - 1
                    break
                elif field[row_next][col_next] == ' ':
                    col_next -= 1
                    break
            # if next pos is a walk, return to the original pos
            if field[row_next][col_next] == '#':
                return current_pos[0], current_pos[1]

        elif field[row_next][col_next] == '#':
            return current_pos[0], current_pos[1]

    elif current_direction == "up":
        col_next = current_pos[1]
        row_next = current_pos[0] - 1
        # if next pos is outsize the field, wrap around other size
        if row_next < 0:
            while True:
                row_next += 1
                if row_next == len(field):
                    row_next = len(field) - 1
                    break
                elif field[row_next][col_next] == ' ':
                    row_next -= 1
                    break
            # if next pos is a walk, return to the original pos
            if field[row_next][col_next] == '#':
                return current_pos[0], current_pos[1]
        elif field[row_next][col_next] == ' ':
            while True:
                row_next += 1
                if row_next == len(field):
                    row_next = len(field) - 1
                    break
                elif field[row_next][col_next] == ' ':
                    row_next -= 1
                    break
            # if next pos is a walk, return to the original pos
            if field[row_next][col_next] == '#':
                return current_pos[0], current_pos[1]

        elif field[row_next][col_next] == '#':
            return current_pos[0], current_pos[1]

    elif current_direction == "down":
        col_next = current_pos[1]
        row_next = current_pos[0] + 1
        # if next pos is outsize the field, wrap around other size
        if row_next >= len(field):
            while True:
                row_next -= 1
                if row_next == -1:
                    row_next = 0
                    break
                elif field[row_next][col_next] == ' ':
                    row_next += 1
                    break
            # if next pos is a walk, return to the original pos
            if field[row_next][col_next] == '#':
                return current_pos[0], current_pos[1]
        elif field[row_next][col_next] == ' ':
            while True:
                row_next -= 1
                if row_next == -1:
                    row_next = 0
                    break
                elif field[row_next][col_next] == ' ':
                    row_next += 1
                    break
            # if next pos is a walk, return to the original pos
            if field[row_next][col_next] == '#':
                return current_pos[0], current_pos[1]

        elif field[row_next][col_next] == '#':
            return current_pos[0], current_pos[1]



    return row_next, col_next


# %%
from copy import deepcopy

current_pos = [0, field[0].index('.')]
field_clone = deepcopy(field)
current_direction = "right"
instruct_debug = None
step_debug = None
for instruct in instructions:
    instruct_debug = instruct
    # print(f"current pos: {current_pos}")
    if instruct.isdigit():
        for i in range(int(instruct)):
            step_debug = i
            current_pos = move_one_step()
            if current_direction == "right":
                field_clone[current_pos[0]][current_pos[1]] = '>'
            elif current_direction == "left":
                field_clone[current_pos[0]][current_pos[1]] = '<'
            elif current_direction == "up":
                field_clone[current_pos[0]][current_pos[1]] = '^'
            elif current_direction == "down":
                field_clone[current_pos[0]][current_pos[1]] = 'v'
    if instruct == 'R':
        if current_direction == "right":
            current_direction = "down"
        elif current_direction == "left":
            current_direction = "up"
        elif current_direction == "up":
            current_direction = "right"
        elif current_direction == "down":
            current_direction = "left"
    if instruct == 'L':
        if current_direction == "right":
            current_direction = "up"
        elif current_direction == "left":
            current_direction = "down"
        elif current_direction == "up":
            current_direction = "left"
        elif current_direction == "down":
            current_direction = "right"

# mark last position
field_clone[current_pos[0]][current_pos[1]] = 'X'
print(f"current pos: {current_pos}")
print(f"current direction: {current_direction}")
result_of_part_1 = 0
if current_direction == "right":
    result_of_part_1 = (current_pos[0] + 1) * 1000 + 4 * (current_pos[1] + 1) + 0
elif current_direction == "down":
    result_of_part_1 = (current_pos[0] + 1) * 1000 + 4 * (current_pos[1] + 1) + 1
elif current_direction == "left":
    result_of_part_1 = (current_pos[0] + 1) * 1000 + 4 * (current_pos[1] + 1) + 2
elif current_direction == "up":
    result_of_part_1 = (current_pos[0] + 1) * 1000 + 4 * (current_pos[1] + 1) + 3
# %%
with open('output/day22.out', 'w+') as f:
    for row in field_clone:
        f.write(''.join(row))
        f.write('\n')
# %%
# %%
