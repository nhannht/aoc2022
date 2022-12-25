data = open('input/day25.txt').read().splitlines()
# %%
base_snafu_digit = {"2": 2, "1": 1, "0": 0, "-": -1, "=": -2}


# snafu
def convert_snafu_number_to_dec(snafu_number) -> int:
    snafu_number = snafu_number[::-1]
    dec_number = 0
    for i in range(len(snafu_number)):
        dec_number += base_snafu_digit[snafu_number[i]] * 5 ** i
    return dec_number

snafu_symbols = list(base_snafu_digit.keys())

def convert_dec_number_to_snafu(dec_number: int):
    five_exp = 0
    while True:
        if 2 * (5 ** five_exp) > dec_number:
            break
        five_exp += 1
    predict_result_len = five_exp+1
    result = ""
    learning_curve = 0
    for i in list(range(predict_result_len))[::-1]:
        future_forseen = [learning_curve + base_snafu_digit[symbol] * 5 ** i for symbol in snafu_symbols]
        min_distance = min(future_forseen, key=lambda x: abs(x - dec_number))
        index = future_forseen.index(min_distance)
        learning_curve = future_forseen[index]
        result += snafu_symbols[index]
    return result



# %%
part1_result = sum([convert_snafu_number_to_dec(snafu_number) for snafu_number in data])
# %%
print(convert_dec_number_to_snafu(part1_result))
#%%
#%%
# list(combinations_with_replacement(snafu_symbols, 3))
#%%
#%%
