data = open("input/day8.txt").read().splitlines()
# %%
data = [[int(char) for char in line] for line in data]
# %% stage 1
def visible_in_one_direction(current,l):
    for tree in l:
        if tree >= current:
            return False
    return True
count = 0
for row in range(len(data)):
    for col in range(len(data[row])):
        # print("Current is " + str(data[row][col]))
        if row == 0 or col == 0 or row == len(data) - 1 or col == len(data[row]) - 1:
            count += 1
            # print(f"{data[row][col]} is on the edge")
        else:
            all_lefts = [data[row][i] for i in range(0, col)]
            all_rights = [data[row][i] for i in range(col + 1, len(data[row]))]
            all_ups = [data[i][col] for i in range(0, row)]
            all_downs = [data[i][col] for i in range(row + 1, len(data))]
            if visible_in_one_direction(data[row][col], all_lefts)\
                    or visible_in_one_direction(data[row][col], all_rights)\
                    or visible_in_one_direction(data[row][col], all_ups)\
                    or visible_in_one_direction(data[row][col], all_downs):
                count += 1
                print(f"{data[row][col]} is visible")
            else:
                print(f"{data[row][col]} is not visible")
                continue

# %% stage 2
max = 0
def count_tree_can_see_in_direction(current,trees):
    c = 0
    for tree in trees:
        if current > tree:
            c += 1
        else:
            c+=1
            break
    return c

for row in range(len(data)):
    for col in range(len(data[row])):
        # print("Current is " + str(data[row][col]))
        if row == 0 or col == 0 or row == len(data) - 1 or col == len(data[row]) - 1:
            continue
            # print(f"{data[row][col]} is on the edge")
        else:
            all_lefts = [data[row][i] for i in range(0, col)][::-1]
            all_rights = [data[row][i] for i in range(col + 1, len(data[row]))]
            all_ups = [data[i][col] for i in range(0, row)][::-1]
            all_downs = [data[i][col] for i in range(row + 1, len(data))]
            point_left = count_tree_can_see_in_direction(data[row][col], all_lefts)
            point_right = count_tree_can_see_in_direction(data[row][col], all_rights)
            point_up = count_tree_can_see_in_direction(data[row][col], all_ups)
            point_down = count_tree_can_see_in_direction(data[row][col], all_downs)
            scenic_score = point_left * point_right * point_up * point_down
            if scenic_score > max:
                max = scenic_score
                print(f"New max is {max}")


#%%
