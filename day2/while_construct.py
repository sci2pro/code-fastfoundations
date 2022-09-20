import sys


def plain_while():
    i = 0
    while i < 10:
        print(f"{i = }")
        i += 1


def complex_while():
    from my_functions import calculate_geometric_series

    while True:  # loop forever!
        a = int(input("a: "))
        r = float(input("r: "))
        n = int(input("n: "))
        s_n = calculate_geometric_series(a, r, n)
        print(f"{s_n = }")
        quit_ = input("to quit enter 'q': ")  # why do we use 'quit_' instead of 'quit'
        if quit_ == 'q':
            break


def loop_over_file():
    with open("paradoxical.txt") as f:
        while line := f.readline():
            print(f"{line = }")


def reverse_while():
    i = 9
    while i > -1:  # i != 0, i >= 0
        print(f"{i = }")
        i -= 1  # i = i - 1


def funny_sum():
    i = -12
    sum_ = 0
    while True:
        if sum_ > 1000:
            sum -= i
            break
        i += 1
        sum_ += i
    print(f"{sum_ = }")


def main():
    # plain_while()
    # complex_while()
    # loop_over_file()
    # reverse_while()
    funny_sum()
    return 0


if __name__ == '__main__':
    sys.exit(main())
