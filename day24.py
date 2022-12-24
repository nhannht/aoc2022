data = open('input/day24.txt').read().splitlines()
# %%
rocks = []
blizzards = []
for i, line in enumerate(data):
    for j, char in enumerate(line):
        if char == '#':
            rocks.append((i, j))
        if char in ['>', '<', '^', 'v']:
            if char == '>':
                blizzards.append((i, j, 'E'))
            elif char == '<':
                blizzards.append((i, j, 'W'))
            elif char == '^':
                blizzards.append((i, j, 'N'))
            elif char == 'v':
                blizzards.append((i, j, 'S'))


# %%
def blizzards_move(blizzards_, rocks_):
    new_blizzards = []
    for blizzard in blizzards_:
        row, col, direction = blizzard
        if direction == 'E':
            if (row, col + 1) not in rocks_:
                new_blizzards.append((row, col + 1, direction))
            else:
                new_blizzards.append((row, 1, 'E'))
        elif direction == 'W':
            if (row, col - 1) not in rocks_:
                new_blizzards.append((row, col - 1, direction))
            else:
                new_blizzards.append((row, len(data[0]) - 2, 'W'))
        elif direction == 'N':
            if (row - 1, col) not in rocks_:
                new_blizzards.append((row - 1, col, direction))
            else:
                new_blizzards.append((len(data) - 2, col, 'N'))
        elif direction == 'S':
            if (row + 1, col) not in rocks_:
                new_blizzards.append((row + 1, col, direction))
            else:
                new_blizzards.append((1, col, 'S'))
    return new_blizzards


# %%
# new_blizzards = blizzards_move(blizzards, rocks)


# %%
def is_in_blizzards(position, blizzards_):
    for blizzard in blizzards_:
        if position == blizzard[:2]:
            return True
    return False
def my_positions_each_min(position: tuple, blizzards_, rocks_, my_positions_):
    # have 5 options, move up,dowm,left,right, stay
    x, y = position
    if (x,y) not in rocks_ and not is_in_blizzards((x,y), blizzards_):
        my_positions_.add((x,y))
    up = (x - 1, y)
    down = (x + 1, y)
    left = (x, y - 1)
    right = (x, y + 1)
    if up not in rocks_ and not is_in_blizzards(up, blizzards_)and up[0] > 0:
        my_positions_.add(up)
    if down not in rocks_ and not is_in_blizzards(down, blizzards_) and down[0] < len(data):
        my_positions_.add(down)
    if left not in rocks_ and not is_in_blizzards(left, blizzards_) and left[1] > 0:
        my_positions_.add(left)
    if right not in rocks_ and not is_in_blizzards(right, blizzards_) and right[1] < len(data[0]):
        my_positions_.add(right)
    return my_positions_


# %%
from copy import deepcopy
my_positions = set()
start = (0, 1)
out = (len(data) - 1, len(data[0]) - 2)
my_positions.add(start)
min = 0
new_blizzards = deepcopy(blizzards)
while True:
    new_positions = set()

    min += 1
    new_blizzards = blizzards_move(new_blizzards, rocks)
    for position in my_positions:
        my_positions_each_min(position, new_blizzards, rocks,new_positions)

    my_positions=new_positions
    if out in my_positions:
        print(min)
        break
    # if min == 4:
    #     break

# %%
