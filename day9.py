data = open("input/day9.txt").read().splitlines()
# %%
data = [[direction, int(distance)] for direction, distance in [line.split() for line in data]]


# %%
# def move_head(direction: str):
#     global head
#     if direction == "U":
#         head["y"] += 1
#     elif direction == "D":
#         head["y"] -= 1
#     elif direction == "R":
#         head["x"] += 1
#     elif direction == "L":
#         head["x"] -= 1
#     else:
#         raise ValueError("Direction not in U,D,R,L")


# %% move tail with trying to keep up with head
# def move_tail():
#     global tail, head
#     x_tail = tail["x"]
#     y_tail = tail["y"]
#     x_head = head["x"]
#     y_head = head["y"]
#     if head["x"] in range(x_tail - 1, x_tail + 2) and head["y"] in range(y_tail - 1, y_tail + 2):
#         return
#     elif head["x"] == tail["x"]:
#         if head["y"] - tail["y"] == 2:
#             tail["y"] += 1
#         elif head["y"] - tail["y"] == -2:
#             tail["y"] -= 1
#     elif head["y"] == tail["y"]:
#         if head["x"] - tail["x"] == 2:
#             tail["x"] += 1
#         elif head["x"] - tail["x"] == -2:
#             tail["x"] -= 1
#     elif abs(head["x"] - tail["x"]) == 2 or abs(head["y"] - tail["y"]) == 2:
#         if (x_head - x_tail == 2 and y_head - y_tail == 1) \
#                 or (x_head - x_tail == 1 and y_head - y_tail == 2):
#             tail["x"] += 1
#             tail["y"] += 1
#         elif (x_head - x_tail == 2 and y_head - y_tail == -1) \
#                 or (x_head - x_tail == 1 and y_head - y_tail == -2):
#             tail["x"] += 1
#             tail["y"] -= 1
#         elif (x_head - x_tail == -2 and y_head - y_tail == 1) \
#                 or (x_head - x_tail == -1 and y_head - y_tail == 2):
#             tail["x"] -= 1
#             tail["y"] += 1
#         elif (x_head - x_tail == -2 and y_head - y_tail == -1) \
#                 or (x_head - x_tail == -1 and y_head - y_tail == -2):
#             tail["x"] -= 1
#             tail["y"] -= 1
#     else:
#         print(f" value of head is {head}")
#         print(f" value of tail is {tail}")
#         raise ValueError("Something went wrong")


# %%
# old_position = set()
# head = {"x": 0, "y": 0}
# tail = {"x": 0, "y": 0}
# for direction, distance in data:
#     for i in range(distance):
#         move_head(direction)
#         move_tail()
#         old_position.add((tail["x"], tail["y"]))
#         print(f"Head is {head}")
#         print(f"Tail is {tail}")
#         print(f"Distance is {abs(head['x']) + abs(head['y'])}")
# %%
# %%
def update_base_on_front(current, front):
    x_current = current["x"]
    y_current = current["y"]
    x_front = front["x"]
    y_front = front["y"]
    if front["x"] in range(x_current - 1, x_current + 2) and front["y"] in range(y_current - 1, y_current + 2):
        return
    elif front["x"] == current["x"]:
        if front["y"] - current["y"] == 2:
            current["y"] += 1
        elif front["y"] - current["y"] == -2:
            current["y"] -= 1
    elif front["y"] == current["y"]:
        if front["x"] - current["x"] == 2:
            current["x"] += 1
        elif front["x"] - current["x"] == -2:
            current["x"] -= 1
    elif abs(front["x"] - current["x"]) == 2 or abs(front["y"] - current["y"]) == 2:
        if (x_front - x_current == 2 and y_front - y_current == 1) \
                or (x_front - x_current == 1 and y_front - y_current == 2):
            current["x"] += 1
            current["y"] += 1
        elif (x_front - x_current == 2 and y_front - y_current == -1) \
                or (x_front - x_current == 1 and y_front - y_current == -2):
            current["x"] += 1
            current["y"] -= 1
        elif (x_front - x_current == -2 and y_front - y_current == 1) \
                or (x_front - x_current == -1 and y_front - y_current == 2):
            current["x"] -= 1
            current["y"] += 1
        elif (x_front - x_current == -2 and y_front - y_current == -1) \
                or (x_front - x_current == -1 and y_front - y_current == -2):
            current["x"] -= 1
            current["y"] -= 1
        elif (x_front - x_current == 2 and y_front - y_current == 2):
            current["x"] += 1
            current["y"] += 1
        elif (x_front - x_current == 2 and y_front - y_current == -2):
            current["x"] += 1
            current["y"] -= 1
        elif (x_front - x_current == -2 and y_front - y_current == 2):
            current["x"] -= 1
            current["y"] += 1
        elif (x_front - x_current == -2 and y_front - y_current == -2):
            current["x"] -= 1
            current["y"] -= 1
    else:
        print(f" value of front is {front}")
        print(f" value of current is {current}")
        raise ValueError("Something went wrong")


# %%
def move_head_2(first_knot, direction: str):
    if direction == "U":
        first_knot["y"] += 1
    elif direction == "D":
        first_knot["y"] -= 1
    elif direction == "R":
        first_knot["x"] += 1
    elif direction == "L":
        first_knot["x"] -= 1
    else:
        raise ValueError("Direction not in U,D,R,L")


# %%

snake = [{"x": 0, "y": 0} for i in range(10)]
old_tail_position = set()
for direction, distance in data:
    print(f"Direction is {direction} and distance is {distance}")
    for i in range(distance):
        move_head_2(snake[0], direction)
        update_base_on_front(snake[1], snake[0])
        update_base_on_front(snake[2], snake[1])
        update_base_on_front(snake[3], snake[2])
        update_base_on_front(snake[4], snake[3])
        update_base_on_front(snake[5], snake[4])
        update_base_on_front(snake[6], snake[5])
        update_base_on_front(snake[7], snake[6])
        update_base_on_front(snake[8], snake[7])
        update_base_on_front(snake[9], snake[8])
        old_tail_position.add((snake[9]["x"], snake[9]["y"]))

#%%
