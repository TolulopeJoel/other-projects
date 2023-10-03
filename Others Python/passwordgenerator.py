import random

amount_of_lowercase_letters = int(input('how many small letters do you want ?? '))
amount_of_uppercase_letters = int(input('how many capital letters do you want ?? '))
amount_of_symbols = int(input('how many symbols do you want ?? '))
amount_of_numbers = int(input('how many numbers do you want ?? '))

lowercase_letters = [i for i in random.sample(list("abcdefghijklmnopqrstuvwxy"), amount_of_lowercase_letters)]
uppercase_letters = [j for j in random.sample(list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"), amount_of_uppercase_letters)]
symbols = [k for k in random.sample(('~', '!', '@', '#', '$', '%', '^', '&', '*', '+', '_'), amount_of_symbols)]
numbers = [str(m) for m in random.sample(range(0,10), amount_of_numbers)]

aggregated_information = set(lowercase_letters + uppercase_letters + symbols + numbers)

password = "".join(aggregated_information)
print(password)

