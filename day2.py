# A is rock, B is paper, C is Scissors
# X is rock, Y is paper, Z is Scissors
pointDict = {}
pointDict["A X"] = 1 + 3 # we draw + 4
pointDict["A Y"] = 2 + 6 # we win + 8
pointDict["A Z"] = 3 + 0 # we lose + 3
pointDict["B X"] = 1 + 0 # we lose + 1
pointDict["B Y"] = 2 + 3 # we draw + 5
pointDict["B Z"] = 3 + 6 # we win + 9
pointDict["C X"] = 1 + 6 # we win + 7
pointDict["C Y"] = 2 + 0 # we lose + 2
pointDict["C Z"] = 3 + 3 # we draw + 6

input = open("input/day2.txt", "r")
input = input.read().splitlines()
#%%
demand = ["lose" if i[2] == "X" else "draw" if i[2] == "Y" else "win" for i in input]
#%%
result = 0
for index,match in enumerate(input):
    if match[0] == "A":
        if demand[index] == "win":
            result += 8
        elif demand[index] == "draw":
            result += 4
        elif demand[index] == "lose":
            result += 3
    elif match[0] == "B":
        if demand[index] == "win":
            result += 9
        elif demand[index] == "draw":
            result += 5
        elif demand[index] == "lose":
            result += 1
    elif match[0] == "C":
        if demand[index] == "win":
            result += 7
        elif demand[index] == "draw":
            result += 6
        elif demand[index] == "lose":
            result += 2
