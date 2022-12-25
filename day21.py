data = open('input/day21.txt').read().splitlines()
monkeys = {}
for line in data:
    monkey, yell = line.split(':')
    if len(yell.split()) == 1:
        monkeys[monkey] = int(yell)
    else:
        monkeys[monkey] = [yell.split()[0], yell.split()[1], yell.split()[2]]


#%%
def analyze_monkey_yell(monkey_):
    yell_ = monkeys[monkey_]
    if type(yell_) == int:
        return yell_
    elif len(yell_) == 3:
        first_monkey = yell_[0]
        second_monkey = yell_[2]
        operator = yell_[1]
        decrypt_first_monkey = analyze_monkey_yell(first_monkey)
        decrypt_second_monkey = analyze_monkey_yell(second_monkey)
        if operator == '+':
            return decrypt_first_monkey + decrypt_second_monkey
        elif operator == '-':
            return decrypt_first_monkey - decrypt_second_monkey
        elif operator == '*':
            return decrypt_first_monkey * decrypt_second_monkey
        elif operator == '/':
            return decrypt_first_monkey / decrypt_second_monkey

# %% part1 solution here
# analyze_monkey_yell('root')


# %% part 2

def analyze_monkey_yell_2(monkey_,monkeys_):
    yell_ = monkeys_[monkey_]
    if type(yell_) == int:
        return yell_
    elif len(yell_) == 3:
        first_monkey = yell_[0]
        second_monkey = yell_[2]
        operator = yell_[1]
        decrypt_first_monkey = analyze_monkey_yell_2(first_monkey,monkeys_)
        decrypt_second_monkey = analyze_monkey_yell_2(second_monkey,monkeys_)
        if operator == '+':
            return decrypt_first_monkey + decrypt_second_monkey
        elif operator == '-':
            return decrypt_first_monkey - decrypt_second_monkey
        elif operator == '*':
            return decrypt_first_monkey * decrypt_second_monkey
        elif operator == '=':
            return decrypt_first_monkey == decrypt_second_monkey

        elif operator == '/':
            return decrypt_first_monkey / decrypt_second_monkey
#%%
# from copy import deepcopy
# monkeys_copy = deepcopy(monkeys)
# monkeys_copy['root'][1]= '='
# start = 0
# while not analyze_monkey_yell_2('root',monkeys_copy):
#     start += 1
#     monkeys_copy['humn'] = start
#
# print(start)
#%%
# monkeys["root"]
#%%
# analyze_monkey_yell_2(monkeys['root'][2],monkeys)

#%%

def recursive_check_humn_in_child_of_monkeys_branchs(monkey_,monkeys_):
    if monkey_ == 'humn':
        return True
    else:
        if type(monkeys_[monkey_]) in [int,float]:
            return False
        else:
            return recursive_check_humn_in_child_of_monkeys_branchs(monkeys_[monkey_][0],monkeys_)\
                or recursive_check_humn_in_child_of_monkeys_branchs(monkeys_[monkey_][2],monkeys_)



#%%
from copy import deepcopy
monkeys_copy2 = deepcopy(monkeys)
# calculated all monkey that not related to humn, they value are constant
for monkey in monkeys_copy2:
    if not recursive_check_humn_in_child_of_monkeys_branchs(monkey,monkeys_copy2):
        monkeys_copy2[monkey] =  analyze_monkey_yell(monkey)
#%%
def convert_symbols_to_operator(monkey_,monkeys_):
    if monkey_ == 'humn':
        return monkey_
    else:
        if type(monkeys_[monkey_]) in [int,float]:
            return monkey_
        else:
            return "( " + convert_symbols_to_operator(monkeys_[monkey_][0],monkeys_)\
                + " " + monkeys_[monkey_][1] + " " + convert_symbols_to_operator(monkeys_[monkey_][2],monkeys_) + " )"
#%%
monkeys_copy2['root'][1] = '='
monkeys_copy2['root'] # => lvvf and rqgq
recursive_check_humn_in_child_of_monkeys_branchs('lvvf',monkeys_copy2)
recursive_check_humn_in_child_of_monkeys_branchs('rqgq',monkeys_copy2) # False

humn_equation  = convert_symbols_to_operator('lvvf',monkeys_copy2)
for i,e in enumerate(humn_equation.split()):
    if e == 'humn':
        pass
    elif e in ['+','-','*','/',")","("]:
        pass
    else:
        humn_equation = humn_equation.replace(e,str(monkeys_copy2[e]))
#%%
from sympy import symbols, solve,sympify,Eq
humn = symbols('humn')
# find humn in humn_equation
solve(Eq(sympify(humn_equation),monkeys_copy2['rqgq']),humn)
#%%

#%%
