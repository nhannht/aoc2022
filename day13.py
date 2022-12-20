#%%
# data = open('input/day13_small.txt').read().splitlines()
data = open('input/day13.txt').read().splitlines()
#%%
false = 0

def recursive_compare(list1, list2):
    global false
    if len(list1) == 0:
        return
    if len(list2) == 0:
        false += 1
        return
    first_l1 = list1[0]
    first_l2 = list2[ 0 ]
    if type(first_l1) == type(first_l2) == int:
        if first_l1 > first_l2:
            false += 1
            return
        elif first_l1 < first_l2:
            return
        elif first_l1 == first_l2:
            recursive_compare(list1[1:], list2[1:])
    elif type(first_l1) == type(first_l2) == list:
        recursive_compare(first_l1, first_l2)
    elif type(first_l1) == int and type(first_l2) == list:
        first_l1 = [first_l1]
        recursive_compare(first_l1, first_l2)
    elif type(first_l1) == list and type(first_l2) == int:
        first_l2 = [first_l2]
        recursive_compare(first_l1, first_l2)
#%% test recursive_compare
# p1 = ast.literal_eval(data[0])
# p2 = ast.literal_eval(data[1])
# recursive_compare(p1, p2)

# %% part 1
import ast

false = 0
true_count = 0
indice = 1
indices = []
for index, line in enumerate(data):
    if index % 3 == 0:
        first = ast.literal_eval(line)
    if index % 3 == 1:
        second = ast.literal_eval(line)
    if index % 3 == 2 or index == len(data) - 1:
        false = 0
        recursive_compare(first, second)
        if false == 0:
            true_count += indice
            indices.append(indice)
            # print(f"{first} and {second} ")
            print(f"{indice} is indice of right order pair")
        indice += 1

# %% part 2

new_data = [line for line in data if line.strip() != ""]
new_data.append("[[2]]")
new_data.append("[[6]]")
new_data = [ast.literal_eval(line) for line in new_data]

# %%
import functools
def recursive_compare_wrapper(list1, list2):
    global false
    false = 0
    recursive_compare(list1, list2)
    if false == 0:
        return -1
    elif false > 0:
        return 1
    return 0

sorted_new_data = sorted(new_data, key=functools.cmp_to_key(recursive_compare_wrapper),
                         reverse=False)
# %%
part2_result = (sorted_new_data.index([[2]]) +1)  * (sorted_new_data.index([[6]]) + 1)
