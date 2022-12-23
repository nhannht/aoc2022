# day 22
data = open('input/day22_small.txt').read().splitlines()
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
                if field[row_next][col_next] == ' ':
                    col_next += 1
                    break
            # if next pos is a walk, return to the original pos
            if field[row_next][col_next] == '#':
                current_direction = "left"
                row_next,col_next = move_one_step()
        if field[row_next][col_next] == ' ':
            while True:
                col_next -= 1
                if field[row_next][col_next] == ' ':
                    col_next += 1
                    break
            if field[row_next][col_next] == '#':
                current_direction = "left"
                row_next, col_next = move_one_step()

        if field[row_next][col_next] == '#':
            current_direction = "left"
            row_next, col_next = move_one_step()

    elif current_direction == "left":
        col_next = current_pos[1] - 1
        row_next = current_pos[0]
        # if next pos is outsize the field, wrap around other size
        if col_next < 0:
            while True:
                col_next += 1
                if field[row_next][col_next] == ' ':
                    col_next -= 1
                    break
            if field[row_next][col_next] == '#':
                current_direction = "right"
                row_next, col_next = move_one_step()
        if field[row_next][col_next] == ' ':
            while True:
                col_next += 1
                if field[row_next][col_next] == ' ':
                    col_next -= 1
                    break
            if field[row_next][col_next] == '#':
                current_direction = "right"
                row_next,col_next = move_one_step()

        if field[row_next][col_next] == '#':
            current_direction = "right"
            row_next, col_next = move_one_step()

    elif current_direction == "up":
        col_next = current_pos[1]
        row_next = current_pos[0] - 1
        # if next pos is outsize the field, wrap around other size
        if row_next < 0:
            while True:
                row_next += 1
                if field[row_next][col_next] == ' ':
                    row_next -= 1
                    break
            if field[row_next][col_next] == '#':
                current_direction = "down"
                row_next, col_next = move_one_step()
        if field[row_next][col_next] == ' ':
            while True:
                row_next += 1
                if field[row_next][col_next] == ' ':
                    row_next -= 1
                    break
            if field[row_next][col_next] == '#':
                current_direction = "down"
                row_next, col_next = move_one_step()

        if field[row_next][col_next] == '#':
            current_direction = "down"
            row_next,col_next = move_one_step()

    elif current_direction == "down":
        col_next = current_pos[1]
        row_next = current_pos[0] + 1
        # if next pos is outsize the field, wrap around other size
        if row_next >= len(field):
            while True:
                row_next -= 1
                if field[row_next][col_next] == ' ':
                    row_next += 1
                    break
            if field[row_next][col_next] == '#':
                current_direction = "up"
                row_next,col_next = move_one_step()
        if field[row_next][col_next] == ' ':
            while True:
                row_next -= 1
                if field[row_next][col_next] == ' ':
                    row_next += 1
                    break
            if field[row_next][col_next] == '#':
                current_direction = "up"
                row_next, col_next = move_one_step()

        if field[row_next][col_next] == '#':
            current_direction = "up"
            row_next, col_next = move_one_step()



    return row_next, col_next


# %%
current_pos = [0, field[0].index('.')]
current_direction = "right"
for instruct in instructions:

    print(f"current pos: {current_pos}")
    if instruct.isdigit():
        for i in range(int(instruct)):
            current_pos = move_one_step()
            if current_direction == "right":
                field[current_pos[0]][current_pos[1]] = '>'
            elif current_direction == "left":
                field[current_pos[0]][current_pos[1]] = '<'
            elif current_direction == "up":
                field[current_pos[0]][current_pos[1]] = '^'
            elif current_direction == "down":
                field[current_pos[0]][current_pos[1]] = 'v'

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
field[current_pos[0]][current_pos[1]] = 'X'
# %%
for row in field:
    print(''.join(row))
# %%
current_pos = [0, field[0].index('.')]
current_direction = "right"
# %%
current_pos = move_one_step()
