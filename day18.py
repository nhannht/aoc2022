#%%
import operator

data = open("input/day18.txt").read().splitlines()
data = [[int(num) for num in line.split(',')] for line in data]
#%%
side_expose = len(data) * 6
for cube_index in range(len(data)):
    cube_sub_result_list = []
    for other_cube in data[:cube_index] +  data[cube_index + 1:]:
        result_of_substract = list(map(int.__sub__,data[cube_index],other_cube))
        if result_of_substract.count(0) == 2:
            if result_of_substract.count(1) == 1 or result_of_substract.count(-1) == 1:
                side_expose -=1

#%% part 2
# model a space and find all the empty points in space
max_x = max([cube[0] for cube in data])
max_y = max([cube[1] for cube in data])
max_z = max([cube[2] for cube in data])

#%%
space = [[a,b,c] for a in range(0,max_x+1) for b in range(0,max_y+1) for c in range(0,max_z+1)]
space = [cube for cube in space if cube not in data]
#%%
# find all empty space using dfs, starting from [0,0,0]
visited = set()
# dfs in 3d space without recursion
def dfs(space,visited):
    todo = [space[0]]
    while todo:
        here = todo.pop()
        visited.add(tuple(here))
        upper = [here[0],here[1],here[2]+1]
        lower = [here[0],here[1],here[2]-1]
        left = [here[0],here[1]-1,here[2]]
        right = [here[0],here[1]+1,here[2]]
        front = [here[0]-1,here[1],here[2]]
        back = [here[0]+1,here[1],here[2]]
        for d in [upper,lower,left,right,front,back]:
            if tuple(d) not in visited and d in space :
                todo.append(d)

dfs(space,visited)

#%%
visited = [list(point) for point in visited]
#%%
blank_point_not_expose = [cube for cube in space if cube not in list(visited)]

#%%
for point in blank_point_not_expose:
    data.append(point)
#%%

side_expose_include_fake_cube = len(data) * 6
for cube_index in range(len(data)):
    cube_sub_result_list = []
    for other_cube in data[:cube_index] +  data[cube_index + 1:]:
        result_of_substract = list(map(int.__sub__,data[cube_index],other_cube))
        if result_of_substract.count(0) == 2:
            if result_of_substract.count(1) == 1 or result_of_substract.count(-1) == 1:
                side_expose_include_fake_cube -=1


#%%
# result_part_2 = side_expose - count_non_expose_empty_point*6
#
#
# #%%
# # visualize this space using ax.voxels
# import matplotlib.pyplot as plt
# from mpl_toolkits.mplot3d import Axes3D
# import numpy as np
# # create 3d matrix from space
# # extract all point from data in space
# x_data = [cube[0] for cube in data]
# y_data = [cube[1] for cube in data]
# z_data = [cube[2] for cube in data]
# # create a 3d matrix with 1 in data point and 0 in empty point
# c = np.zeros((max_x-min_x+5,max_y-min_y+5,max_z-min_z+5))
# c[x_data,y_data,z_data] = 1
# #%%
#
#
# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')
# ax.voxels(c,facecolors='w', edgecolor='k')
# plt.show()
# # export this fig to 3d model
#
# #%%
# N1 = 10
# N2 = 10
# N3 = 10
# ma = np.random.choice([0,1], size=(N1,N2,N3), p=[0.99, 0.01])
#%%
