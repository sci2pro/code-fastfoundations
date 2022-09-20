import sys


def calculate_geometric_series(a, r, n=10):
    """Calculate the sum of a geometric series"""
    if r == 1:
        return a * (n + 1)
    return a * (1 - r ** (n + 1)) / (1 - r)


def main():
    try:
        a = int(input("a: "))
    except ValueError:
        print(f"Invalid value for a; defaulting to a=1...", file=sys.stderr)
        a = 1
    r = float(input("r: "))
    try:
        n = int(input("n: "))
    except ValueError:
        print(f"Invalid value for n; defaulting to n=10...", file=sys.stderr)
    try:
        assert n >= 1
    except AssertionError:
        raise ValueError(f"Invalid value for n; please retry...")
    else:
        print(f"s_{n} = {calculate_geometric_series(a, r, n=n)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
