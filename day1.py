# %%
input = open("input/day1.txt", "r").read()
# %%
calo = []
split_group_base_on_empty_line = input.split("\n\n")
# %%
# Result
sum(sorted([sum([int(i) for i in group.splitlines()]) for group in split_group_base_on_empty_line])[-3:])

#%%
