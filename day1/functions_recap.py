import sys


def calculate_geometric_series(a, r, n=10):
    """Calculate the sum of a geometric series"""
    if r == 1:
        return a * (n + 1)
    return a * (1 - r ** (n + 1)) / (1 - r)


def get_max(input_list):
    # view the flowchart at: https://app.diagrams.net/?src=about#G1OO2JBthw0qURhTLd1vuFQKObgw1Kcxvj
    maximum = None
    first = False
    for value in input_list:
        if not first:  # if we have not seen the first
            maximum = value
            first = True  # we will never enter this if construct again
        if value > maximum:
            maximum = value  # set a new maximum
    return maximum


def main():
    # a = int(input("a: "))
    # r = float(input("r: "))
    # n = int(input("n: "))
    # print(f"s_n = {calculate_geometric_series(a, r, n)}")
    numbers = [1, 3, 9, 42, 16, 93]
    maximum = get_max(numbers)
    print(f"The maximum value from the list {numbers} is {maximum}.")
    numbers = []
    maximum = get_max(numbers)
    print(f"The maximum value from the list {numbers} is {maximum}.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
