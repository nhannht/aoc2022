import string

data = open("input/day3.txt").read().splitlines()
#%%
# generate a list of character from a to z
points = dict(zip(string.ascii_lowercase, range(1,27))) | dict(zip(string.ascii_uppercase, range(27,53)))
#%%
# split each string to half in data
pairs = [[line[:len(line)//2],line[len(line)//2:]] for line in data]
#%%
group_of_3 = [[data[i],data[i+1],data[i+2]] for i in range(0,len(data),3)]
#%%
def find_common_in_3_strings(string1:str,string2:str,string3:str):
    first_version = [char for char in string1 if char in string2 and char in string3]
    remove_dupplicate = list(set(first_version))
    return remove_dupplicate
#%%
point2 = 0
for case in [find_common_in_3_strings(*group) for group in group_of_3]:
    for c in case:
        point2 += points[c]

#%%
# dupplicate chars in each pair in pairs
def find_duplicate_chars(pair1:str,pair2:str):
    first_version =  [char for char in pair1 if char in pair2]
    remove_dupplicate = list(set(first_version))
    return remove_dupplicate
#%%
dups = [find_duplicate_chars(pair[0],pair[1]) for pair in pairs]
#%%
point = 0
for dup in dups:
    for char in dup:
        point += points[char]

