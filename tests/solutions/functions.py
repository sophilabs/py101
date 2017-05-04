def print_even(upper_bound):
    for number in range(upper_bound+1):
        if number % 2 == 0 and number > 1:
            print(number)
print_even(100)
