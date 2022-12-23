data = open('input/day19.txt').read().splitlines()

blueprints = [[int(s) for s in line.split() if s.isdigit()] for line in data]
# join each pargaraph into a single string
# %%
# implement entire algorithm in numpy
from copy import deepcopy
from itertools import combinations
import math


def mining(state):
    state[0] += state[4]
    state[1] += state[5]
    state[2] += state[6]
    state[3] += state[7]
    return state


def is_state_better(state0, state1):
    """
    The is_state_better function takes two states as input and returns a boolean value.
    The function checks if the first state is better than the second state. The function
    returns True if the first state is better, False otherwise.

    :param state0: true if this state is better
    :param state1:
    :return: True if the state is better than the previous one
    :doc-author: nhannht
    """
    # print(f"State 0 is {state0}")
    result = [a - b for a, b in zip(state0, state1)]
    # print(f"State 1 is {result}")
    if result[4] == result[5] == result[6] == result[7] == 0:
        if result[0] >= 0 and result[1] >= 0 and result[2] >= 0 and result[3] >= 0:
            return True
        else:
            return False


def generate_all_next_state_of_state(state, blueprint):
    """
    The generate_all_next_state_of_state function takes in a state and the blueprint of the robot.
    It returns all possible next states that can be reached from this current state, given that we have already created one ore, clay or obsidian robot.


    :param state: Store the current state of the system
    :param blueprint: Determine the number of robots needed to create a geode
    :return: A list of all possible next states
    :doc-author: Trelent
    """
    max_ore_robot_needed = max([blueprint[0], blueprint[1], blueprint[2], blueprint[4]])
    max_clay_robot_needed = math.ceil(blueprint[3])
    max_obsidian_robot_needed = math.ceil(blueprint[5])
    next_states = []
    # current robot
    ore_robot = state[4]
    clay_robot = state[5]
    obsidian_robot = state[6]
    geode_robot = state[7]
    current_min = state[8]
    # current resource
    ore = state[0]
    clay = state[1]
    obsidian = state[2]

    # remain minute and predict what resource will be at min 24
    remain_min = 32 - current_min
    ore_til_the_end = ore + remain_min * ore_robot
    clay_til_the_end = clay + remain_min * clay_robot
    obsidian_til_the_end = obsidian + remain_min * obsidian_robot
    ore_is_waste = ore_til_the_end > (max_ore_robot_needed * remain_min)
    clay_is_waste = clay_til_the_end > (max_clay_robot_needed * remain_min)
    obsidian_is_waste = obsidian_til_the_end > (max_obsidian_robot_needed * remain_min)

    # state that create geode robot, return immediately if choose this path
    if ore >= blueprint[4] \
            and obsidian >= blueprint[5]:
        state_that_create__one_geode_robot = deepcopy(state)
        state_that_create__one_geode_robot[0] -= blueprint[4]
        state_that_create__one_geode_robot[2] -= blueprint[5]
        mining(state_that_create__one_geode_robot)
        state_that_create__one_geode_robot[7] += 1
        state_that_create__one_geode_robot[8] += 1
        next_states.append(state_that_create__one_geode_robot)
        return next_states

    # state that just mining
    state_that_not_create_anything = deepcopy(state)
    mining(state_that_not_create_anything)
    state_that_not_create_anything[8] += 1
    next_states.append(state_that_not_create_anything)

    # this path create obsidian bot, consider after fail to pick geode bot
    if ore < blueprint[2] or clay < blueprint[3] or obsidian_robot >= max_obsidian_robot_needed or obsidian_is_waste:
        pass
    # state that create obsidian robot
    else:
        state_that_create__one_obsidian_robot = deepcopy(state)
        state_that_create__one_obsidian_robot[0] -= blueprint[2]
        state_that_create__one_obsidian_robot[1] -= blueprint[3]
        mining(state_that_create__one_obsidian_robot)
        state_that_create__one_obsidian_robot[6] += 1
        state_that_create__one_obsidian_robot[8] += 1
        next_states.append(state_that_create__one_obsidian_robot)
        # return next_states

    if ore < blueprint[0] or ore_robot >= max_ore_robot_needed or ore_is_waste:
        pass
    # state that create  a ore robot
    # we don't create robot if we don't have enough resource
    else:
        state_that_create__one_ore_robot = deepcopy(state)
        state_that_create__one_ore_robot[0] -= blueprint[0]
        mining(state_that_create__one_ore_robot)
        state_that_create__one_ore_robot[4] += 1
        state_that_create__one_ore_robot[8] += 1
        next_states.append(state_that_create__one_ore_robot)
    if ore < blueprint[1] or clay_robot >= max_clay_robot_needed or clay_is_waste or obsidian_is_waste:
        pass
    # state that create clay robot
    else:
        state_that_create__one_clay_robot = deepcopy(state)
        state_that_create__one_clay_robot[0] -= blueprint[1]
        mining(state_that_create__one_clay_robot)
        state_that_create__one_clay_robot[5] += 1
        state_that_create__one_clay_robot[8] += 1
        next_states.append(state_that_create__one_clay_robot)

    return next_states


# %%
from timeit import default_timer as timer


#
start = timer()
#
#
def simmulate_each_blueprint(blueprint):
    """
    The simmulate_each_blueprint function simulates the blueprint and returns a list of all possible states.
    The function starts with a state that is 0,0,0,0, 1, 0 ,0 ,0 ,and 0. Then it generates all next states by
    combining each state in the current list of states with each other. The function then checks if one state is better than another
    state based on geode value and removes the worse one from the current list of states.

    :param blueprint: Represent the state of a blueprint
    :return: All the states that can be reached from a given state
    :doc-author: Trelent
    """
    states_0 = [0, 0, 0, 0, 1, 0, 0, 0, 0]
    states = [states_0]
    min_ = 0
    while min_ < 32:
        next_states = []
        for state in states:
            next_states.extend(generate_all_next_state_of_state(state, blueprint))

        pair_generator = combinations(next_states, 2)
        while True:
            try:
                pair = next(pair_generator)
                if is_state_better(pair[0], pair[1]):
                    if pair[1] in next_states:
                        next_states.remove(pair[1])
                elif is_state_better(pair[1], pair[0]):
                    if pair[0] in next_states:
                        next_states.remove(pair[0])
            except StopIteration:
                break

        # sort base on geode and get first 10k result
        states = next_states
        print(len(states))
        min_ += 1
        print(min_)
    return states


#
#
state_result = simmulate_each_blueprint(blueprints[2])
end = timer()
print(end - start)
# %%
# find states that have most geode
state_result.sort(key=lambda x: x[3], reverse=True)
print(state_result[0:5])

# %%
# point = 0
# for index, blueprint in enumerate(blueprints):
#     state_result = sorted(simmulate_each_blueprint(blueprint), key=lambda x: x[3], reverse=True)
#     # print(index, state_result[0:5])
#     best_state_geode = state_result[0][3]
#
#
#     point += best_state_geode * (index + 1)
#
# print(point)