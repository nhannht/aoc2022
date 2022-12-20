from itertools import count

data = open("input/day4.txt").read()
# %%
pairs = [[pair for pair in line.split(",")] for line in data.splitlines()]

#%%
def is_contain(pair1: str, pair2: str):
    pair1_start, pair1_end = pair1.split("-")
    pair2_start, pair2_end = pair2.split("-")
    pair1_contain_pair2 = int(pair1_start) <= int(pair2_start) and int(pair1_end) >= int(pair2_end)
    pair2_contain_pair1 = int(pair2_start) <= int(pair1_start) and int(pair2_end) >= int(pair1_end)
    return pair1_contain_pair2 or pair2_contain_pair1
#%%
[is_contain(pair[0],pair[1]) for pair in pairs ].count(True)
#%%
from collections import Counter
def is_overlaps(pair1:str,pair2:str):
    list1 = list(range(int(pair1.split("-")[0]),int(pair1.split("-")[1])+1))
    list2 = list(range(int(pair2.split("-")[0]),int(pair2.split("-")[1])+1))
    return list(Counter(list1+list2).values()).count(2) > 0
#%%
first_pair = pairs[0]
print(is_overlaps(first_pair[0],first_pair[1]))
#%%
[is_overlaps(pair[0],pair[1]) for pair in pairs ].count(True)
