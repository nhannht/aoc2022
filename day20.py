
# data= open('input/day20_small.txt').read().splitlines()
data= open('input/day20.txt').read().splitlines()
data = [int(d) for d in data]
#%%
from typing import List
def move_digit_base_on_it_value(digit,current_digit_pos:int,list_:List):

    if digit == 0:
        return list_
    else:
        new_pos = (current_digit_pos + digit) % len(list_)
        # if new pos stay between 0 and len(list_) -1
        # 0######new_pos######current_digit_pos######len(list_) -1
        if 0 <= new_pos <= current_digit_pos:
            return list[:new_pos]\
                + [list_[current_digit_pos]]\
                + list_[new_pos:current_digit_pos]\
                + list_[current_digit_pos+1:]
        # if new pos stay between current_digit_pos and len(list_) -1
        # 0#########current_digit_pos#########new_pos#########len(list_) -1
        elif current_digit_pos <= new_pos <= len(list_) -1:
            return list_[:current_digit_pos] + list_[current_digit_pos+1:new_pos+1] + [list_[current_digit_pos]] + list_[new_pos+1:]

#%%
from copy import deepcopy
list_copy = deepcopy(data)
move_digit_base_on_it_value(-2,1,[4, -2, 5, 6, 7, 8, 9])
move_digit_base_on_it_value(1,3,[4, 5, 6, 1, 7, 8, 9])
#%%
from collections import Counter
# extract all number appear more than 2 time in Counter(data)


#%%
