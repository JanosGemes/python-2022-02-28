def is_even(number: int) -> bool:

    print("calling is_even function")
    return number % 2 == 0


result = is_even(100)
print(result)
print(is_even(101))