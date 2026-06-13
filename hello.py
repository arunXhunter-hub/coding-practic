def check_even_odd(number):
    if number % 2 == 0:
        return f"{number} is Even"
    else:
        return f"{number} is Odd"


print(check_even_odd(7))
print(check_even_odd(10))
