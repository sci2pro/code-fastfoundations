import random
import sys


def double_number(n):
    return 2 * n


def using_map():
    """Double the given number"""
    random_numbers = random.choices(range(200), k=10)
    print(f"{random_numbers = }")
    print(f"{map(double_number, random_numbers) = }")


def using_map_and_lambda():
    """Using map with a lambda"""
    random_numbers = random.choices(range(200), k=10)
    print(f"{random_numbers = }")
    print(f"{map(lambda r: 2 * r, random_numbers) = }")


def using_filter():
    """Filter out words that are in the wrong case"""
    words = ["shock", "brink", "limited", "admission", "demonstration", "alive", "pen", "reactor", "ban", "sentence", ]
    print(f"{words = }")
    print(f"{filter(lambda w: len(w) > 7, words) = }")


def square_dict(input_dict):
    output_dict = dict()
    for key, value in input_dict.items():
        output_dict[key] = value * value
    return output_dict


def main():
    # using_map()
    # using_map_and_lambda()
    # using_filter()
    input_dict = {
        'one': 1,
        'two': 2,
        'four': 4,
        'eight': 8,
        'nine': 9,
        'sixteen': 16
    }
    print(f"{input_dict = }")
    squared_values = square_dict(input_dict)
    print(f"{squared_values = }")
    print("using map instead:")
    # a bit complex
    # kv is a tuple of (key, value) because we use input_dict.items()
    # the lambda also returns a tuple with:
    # kv[0] is key
    # kv[1] is value
    # we can cast the result to a dict
    squared_by_map = dict(map(lambda kv: (kv[0], kv[1] * kv[1]), input_dict.items()))
    print(f"{squared_by_map = }")
    # now for filter
    # we use the double comparison: a < x < b
    filtered_values = dict(filter(lambda kv: 70 < kv[1] < 100, squared_values.items()))
    print(f"{filtered_values = }")
    return 0


if __name__ == '__main__':
    sys.exit(main())
