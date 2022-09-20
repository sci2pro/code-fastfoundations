import sys


def importing_modules():
    import exceptions

    a = int(input("a: "))
    r = float(input("r: "))
    n = int(input("n: "))
    s_n = exceptions.calculate_geometric_series(a, r, n)
    print(f"s_n = {s_n}")


def importing_packages():
    n = int(input("n: "))

    import pkg1
    print(f"L_{n} = {pkg1.my_module.calculate_lucas_numbers(n)}")

    import pkg1 as lucas_package
    print(f"L_{n} = {lucas_package.my_module.calculate_lucas_numbers(n)}")

    from pkg1 import my_module
    print(f"L_{n} = {my_module.calculate_lucas_numbers(n)}")

    from pkg1 import my_module as lucas_module
    print(f"L_{n} = {lucas_module.calculate_lucas_numbers(n)}")


def task():
    from pkg1.new_pkg import calc
    discriminant = calc.calculate_discriminant(5, 7, 12)
    print(f"{discriminant = }")


def main():
    # importing_modules()
    # importing_packages()
    task()
    return 0


if __name__ == '__main__':
    sys.exit(main())
