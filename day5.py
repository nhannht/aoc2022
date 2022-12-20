data = open("input/day5.txt").read().splitlines()
data = [line if len(line) == 35 else line + " " * (35 - len(line)) for line in data]
#%%
cargos = data[:8]
cargos = [[line[i] for i in [1, 5, 9, 13, 17, 21, 25, 29, 33]] for line in cargos]
# %% invert the cargo

# %%
# Transpose the cargos
cargos = list(map(list, zip(*cargos)))
# %%  rotate the cargos
cargos = [cargo[::-1] for cargo in cargos]
#%%
cargos = [[slot for slot in cargo if slot != " "] for cargo in cargos]
# %%
instructions = data[10:]
# %%
import re
instructions = [list(re.search(r"move (\d+) from (\d+) to (\d+)", instruct).groups()) for instruct in instructions]
#%% part 1:
for instruct in instructions:
    move, from_, to = instruct
    move, from_, to = int(move), int(from_), int(to)
    cargos[to-1] += cargos[from_-1][-move:][::-1]
    cargos[from_-1] = cargos[from_-1][:-move]
#%% part2:  reuse except last block in part 1
for instruct in instructions:
    move, from_, to = instruct
    move, from_, to = int(move), int(from_), int(to)
    cargos[to-1] += cargos[from_-1][-move:]
    cargos[from_-1] = cargos[from_-1][:-move]

#%%
"".join([cargo[-1] for cargo in cargos])
#%% check with day5_small
data_ = open("input/day5_small.txt").read().splitlines()
#%%
data_ = [line if len(line) == 11 else line + " " * (11 - len(line)) for line in data_]
#%%
cargos_ = data_[:3]
cargos_ = [[line[i] for i in [1, 5, 9]] for line in cargos_]
# %%
# Transpose the cargos
cargos_ = list(map(list, zip(*cargos_)))
# %%  rotate the cargos
cargos_ = [cargo[::-1] for cargo in cargos_]
#%%
cargos_ = [[slot for slot in cargo if slot != " "] for cargo in cargos_]
# %%
instructions_ = data_[5:]
# %%
import re
instructions_ = [list(re.search(r"move (\d+) from (\d+) to (\d+)", instruct).groups()) for instruct in instructions_]
#%%
for instruct in instructions_:
    move, from_, to = instruct
    move, from_, to = int(move), int(from_), int(to)
    print(f"move {cargos_[from_-1][-move:]} from {from_} to {to}")

    cargos_[to-1] += cargos_[from_-1][-move:][::-1]
    cargos_[from_-1] = cargos_[from_-1][:-move]
    print(cargos_)

#%%
a = [1,2,3,4,5,6]
a[:-2]