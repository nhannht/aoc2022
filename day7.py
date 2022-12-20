# %% nOT FINISHED YET!.
import copy
import re

data = open("input/day7.txt").read().splitlines()

# %%
dirs = list(set([line.split()[2] for line in data if re.match(r'^\$ cd \w+$', line)]))


# %%
def calculate_size_of_dir(name, sub_data):
    print(f"name is: {name}")
    dir_size: int = 0
    line_contain_name = [l for l in sub_data if re.match(r'^\$ cd {}$'.format(name), l)][0]
    print(f"line_contain_name is: {line_contain_name}")
    count_index_next_line = 1
    while True:
        try:
            next_line = sub_data[sub_data.index(line_contain_name) + count_index_next_line]
            new_data = sub_data[sub_data.index(next_line):]
        except IndexError:
            break
        print(f"next_line is: {next_line}")
        if re.match(r'^\$ cd \w+$', next_line):
            print("next_line is a command")
            print("size is: {}".format(dir_size))
            break
        elif re.match(r'^ ls$', next_line):
            count_index_next_line += 1
            continue
        else:
            if next_line.split()[0].isdigit():
                dir_size += int(next_line.split()[0])
                print("size is: {}".format(dir_size))
            elif next_line.split()[0] == 'dir':
                child = next_line.split()[1]
                dir_size += calculate_size_of_dir(child, new_data)
                print("size is: {}".format(dir_size))
            count_index_next_line += 1
    print("Total size of {} is: {}".format(name, dir_size))
    return dir_size


# %%
dirs_size = [calculate_size_of_dir(dir, data) for dir in dirs]
# %%
dirs_size = [size for size in dirs_size if size <= 100000]
dirs_size = sorted(dirs_size)

# %%

# %%
from itertools import combinations
real_max = 0
for i in range(1, len(dirs_size) + 1):
    e = [s for s
         in [sum(s) for s in list(combinations(dirs_size, i))] if s <= 100000 and s >= 95000]
    if len(e) > 0:
        m = max(e)
    if m > real_max:
        real_max = m

# %%
