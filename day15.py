data = open("input/day15.txt").read().splitlines()
data = [line.replace("Sensor at x=", "").replace(", y=", "|").replace(": closest beacon is at x=", "|").replace(", y=",
                                                                                                                "|").split(
    "|") for line in data]
data = [[int(x), int(y), int(x1), int(y1)] for x, y, x1, y1 in data]


# %%
def find_half_diag_ofthe_square(signal_: dict[str, int], beacon_: dict[str, int]) -> int:
    "This function not return  include the signal itself"
    if signal_["x"] == beacon_["x"] and signal_["y"] == beacon_["y"]:
        return 0
    elif signal_["x"] == beacon_["x"]:
        return abs(signal_["y"] - beacon_["y"])
    elif signal_["y"] == beacon_["y"]:
        return abs(signal_["x"] - beacon_["x"])
    else:
        return abs(signal_["x"] - beacon_["x"]) + abs(signal_["y"] - beacon_["y"])


# #%%
# find_half_diag_ofthe_square(signal, beacon)
# %%
# max([value for row in data for value in row])
# min([value for row in data for value in row])
# %% part 1
# all_range = []
#
# def determine_cross_between_square_and_y_2000000(signal_: dict[str, int], beacon_: dict[str, int]):
#     global all_range
#     half_diag = find_half_diag_ofthe_square(signal_, beacon_)
#     # print(f"Diag is {half_diag}")
#     upper_apex: dict[str, int] = {"x": signal_["x"], "y": signal_["y"] - half_diag}
#     # print(f"Upper apex is {upper_apex}")
#     lower_apex: dict[str, int] = {"x": signal_["x"], "y": signal_["y"] + half_diag}
#     # print(f"Lower apex is {lower_apex}")
#     left_apex = {"x": signal_["x"] - half_diag, "y": signal_["y"]}
#     # print(f"Left apex is {left_apex}")
#     right_apex = {"x": signal_["x"] + half_diag, "y": signal_["y"]}
#     # print(f"Right apex is {right_apex}")
#     # if y =2000000 stay between upper and lower apex
#     if upper_apex["y"] < 2000000 < lower_apex["y"]:
#         d = abs(2000000 - signal_["y"])
#         # print(f"Distance is {d}")
#         left_x = left_apex["x"] + d
#         # print(f"Left x is {left_x}")
#         right_x = left_x + abs(signal_["x"] - left_x) * 2
#         # print(f"Right x is {right_x}")
#         all_range.append([left_x, right_x])
#
#
#     elif upper_apex["y"] == 2000000:
#         all_range.append([upper_apex["x"], upper_apex["x"]])
#         # print(f"Upper apex is {upper_apex}")
#     elif lower_apex["y"] == 2000000:
#         all_range.append([lower_apex["x"], lower_apex["x"]])
#         # print(f"Lower apex is {lower_apex}")
#     elif lower_apex["y"] < 2000000 or upper_apex["y"] > 2000000:
#         pass
#
#
# for line in data:
#     determine_cross_between_square_and_y_2000000(signal_={"x": line[0], "y": line[1]},
#                                                  beacon_={"x": line[2], "y": line[3]})


# %%
# for line in data:
#     if line[3] == 2000000:
#         core_line[line[2]] = 2
# %%
# len(core_line)
# %%
# import Counter
# from collections import Counter
# Counter(core_line.values())
# remove all element in corelen2 where key < 0
# %% part 2
all_range = []

#%%
def determine_cross_between_square_and_y_line(signal_: dict[str, int], beacon_: dict[str, int]
                                              , y_line: int
                                              , all_range_num: int = 0):
    global all_range1, all_range2, all_range3, all_range4, all_range
    if all_range_num == 1:
        all_range = all_range1
    elif all_range_num == 2:
        all_range = all_range2
    elif all_range_num == 3:
        all_range = all_range3
    elif all_range_num == 4:
        all_range = all_range4
    half_diag = find_half_diag_ofthe_square(signal_, beacon_)
    # print(f"Diag is {half_diag}")
    upper_apex: dict[str, int] = {"x": signal_["x"], "y": signal_["y"] - half_diag}
    # print(f"Upper apex is {upper_apex}")
    lower_apex: dict[str, int] = {"x": signal_["x"], "y": signal_["y"] + half_diag}
    # print(f"Lower apex is {lower_apex}")
    left_apex = {"x": signal_["x"] - half_diag, "y": signal_["y"]}
    # print(f"Left apex is {left_apex}")
    right_apex = {"x": signal_["x"] + half_diag, "y": signal_["y"]}
    # print(f"Right apex is {right_apex}")
    # if y =2000000 stay between upper and lower apex
    if upper_apex["y"] < y_line < lower_apex["y"]:
        d = abs(y_line - signal_["y"])
        # print(f"Distance is {d}")
        left_x = left_apex["x"] + d
        # print(f"Left x is {left_x}")
        right_x = left_x + abs(signal_["x"] - left_x) * 2
        # print(f"Right x is {right_x}")
        if left_x < 0:
            left_x = 0
        if right_x > 4000000:
            right_x = 4000000
        all_range.append([left_x, right_x])


    elif upper_apex["y"] == y_line:
        if upper_apex["x"] < 0:
            upper_apex["x"] = 0
        if upper_apex["x"] > 4000000:
            upper_apex["x"] = 3999999
        all_range.append([upper_apex["x"], upper_apex["x"] + 1])
        # print(f"Upper apex is {upper_apex}")
    elif lower_apex["y"] == y_line:
        if lower_apex["x"] < 0:
            lower_apex["x"] = 0
        if lower_apex["x"] > 4000000:
            lower_apex["x"] = 3999999
        all_range.append([lower_apex["x"], lower_apex["x"] + 1])
        # print(f"Lower apex is {lower_apex}")
    elif lower_apex["y"] < y_line or upper_apex["y"] > y_line:
        pass


# %%
from timeit import default_timer as timer
from multiprocessing import Process

start = timer()
all_range1 = []
all_range2 = []
all_range3 = []
all_range4 = []
procs = []
import intervaltree


def subprocess_1():
    global all_range1
    for y in range(0, 1000000):
        all_range1 = []
        for line in data:
            determine_cross_between_square_and_y_line(signal_={"x": line[0], "y": line[1]},
                                                      beacon_={"x": line[2], "y": line[3]},
                                                      y_line=y
                                                      , all_range_num=1)
        tree = intervaltree.IntervalTree.from_tuples(all_range1)
        tree.merge_overlaps(strict=False)

        if len(tree.all_intervals) > 1 or len(tree.all_intervals) == 0:
            print(f"y is {y}")
            print(tree.all_intervals)
            break


proc = Process(target=subprocess_1)
procs.append(proc)
proc.start()

#%%
def subprocess_2():
    global all_range2
    for y in range(1000000, 2000000):
        all_range2 = []
        for line in data:
            determine_cross_between_square_and_y_line(signal_={"x": line[0], "y": line[1]},
                                                      beacon_={"x": line[2], "y": line[3]},
                                                      y_line=y
                                                      , all_range_num=2)
        tree = intervaltree.IntervalTree.from_tuples(all_range2)
        tree.merge_overlaps(strict=False)

        if len(tree.all_intervals) > 1 or len(tree.all_intervals) == 0:
            print(f"y is {y}")
            print(tree.all_intervals)
            break


proc = Process(target=subprocess_2)
procs.append(proc)
proc.start()
#%%
def subprocess_3():
    global all_range3
    for y in range(2000000, 3000000):
        all_range3 = []
        for line in data:
            determine_cross_between_square_and_y_line(signal_={"x": line[0], "y": line[1]},
                                                      beacon_={"x": line[2], "y": line[3]},
                                                      y_line=y
                                                      , all_range_num=3)
        tree = intervaltree.IntervalTree.from_tuples(all_range3)
        tree.merge_overlaps(strict=False)

        if len(tree.all_intervals) > 1 or len(tree.all_intervals) == 0:
            print(f"y is {y}")
            print(tree.all_intervals)
            break


proc = Process(target=subprocess_3)
procs.append(proc)
proc.start()
#%%
def subprocess_4():
    global all_range4
    for y in range(3000000, 400000):
        all_range4 = []
        for line in data:
            determine_cross_between_square_and_y_line(signal_={"x": line[0], "y": line[1]},
                                                      beacon_={"x": line[2], "y": line[3]},
                                                      y_line=y
                                                      , all_range_num=4)
        tree = intervaltree.IntervalTree.from_tuples(all_range4)
        tree.merge_overlaps(strict=False)

        if len(tree.all_intervals) > 1 or len(tree.all_intervals) == 0:
            print(f"y is {y}")
            print(tree.all_intervals)
            break


proc = Process(target=subprocess_4)
procs.append(proc)
proc.start()
#%%
for proc in procs:
    proc.join()

end = timer()
print(end - start)
