data = open("input/day6.txt").read()
l = len(data)
# %%
# %%
count = 0
while True:
    first_4_chars = data[:14]
    if len(set(first_4_chars)) != 14:
        count += 1
        data = data[1:]
    else:
        print(first_4_chars)
        break
# %%
count + 14
# %%
