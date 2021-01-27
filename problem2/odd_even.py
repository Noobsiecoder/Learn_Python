def check_odd(num):
    """ Function to check if a number is even or odd """
    return "even" if (num % 2) == 0 else "odd"


if __name__ == "__main__":
    print(f'2 is an {check_odd(2)} number')     # 2 is an even number
    print(f'23 is an {check_odd(23)} number')   # 23 is an odd number
