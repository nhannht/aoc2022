data = open("input/day10.txt").read().splitlines()
# data = open("input/day10.txt").read().splitlines()
data = [int(line.split()[1]) if len(line.split()) > 1 else "noop" for line in data]
# %% part 1
cycles = 0
point = 1
track_point = []
for line in data:
    if line == 'noop':
        cycles += 1
        if cycles in [20, 60, 100, 140, 180, 220]:
            track_point.append(point * cycles)
    else:
        cycles += 1
        if cycles in [20, 60, 100, 140, 180, 220]:
            track_point.append(point * cycles)
        cycles += 1
        if cycles in [20, 60, 100, 140, 180, 220]:
            track_point.append(point * cycles)
        point += line
# %%
sum(track_point)
# %% part 2
cycles = 0
point = 1
picture = []
row = []
current_drawing = 0
spire_position = [point - 1, point, point + 1]


def draw():
    global current_drawing,cycles,picture,row,point,spire_position
    if current_drawing in spire_position:
        row.append('#')
    else:
        row.append('.')
    current_drawing += 1


for line in data:
    if line == 'noop':
        cycles += 1
        draw()
        if cycles % 40 == 0:
            picture.append(row)
            row,current_drawing = [],0

    else:
        cycles += 1
        draw()
        if cycles % 40 == 0:
            picture.append(row)
            row,current_drawing = [],0

        cycles += 1
        draw()
        if cycles % 40 == 0:
            picture.append(row)
            row,current_drawing = [],0
        point += line
        spire_position = [point - 1, point, point + 1]

#%%
# from pandas import DataFrame
# df = DataFrame(picture)

#%%
# from seaborn import heatmap
# heatmap(df)
#%%
# for line in picture:
#     print(''.join([str(i) for i in line]))

#%%
