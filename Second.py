import re 

text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
pattern = r" \d+\.\d+ "

def  generator_numbers(out_string):
    numbers_list = re.findall(pattern, out_string)

    for number in numbers_list:
        float_number = float(number)
        yield float_number


def sum_profit(out_string, func):
    generator = func(out_string)
    return sum(generator)
   

total = sum_profit(text, generator_numbers)
print(total)




