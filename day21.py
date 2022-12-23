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

#%%
analyze_monkey_yell('root')


#%%
