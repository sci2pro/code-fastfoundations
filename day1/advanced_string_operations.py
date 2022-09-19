import random
import shutil
import sys
import textwrap


def print_5s():
    sssss = "整理、 整頓、 清楚、 清潔、 しつけ"
    print(sssss)
    print(f"{len(sssss) = }")
    sssss_bytes = sssss.encode('utf-8')
    print(f"{len(sssss_bytes) = }")
    print(f"{sssss_bytes = }")
    my_name = "My name is Paul"
    print(f"{my_name = }")
    print(f"{my_name.encode('utf-8') = }")


def working_with_bytes():
    b_empty = bytes()
    print(f"{b_empty = }")
    print(f"{len(b_empty) = }")
    b_random = bytes(random.choices(range(256), k=10))
    print(f"{b_random = }")
    print(f"{ord(b'G') = }")
    b_chars = b'the moon is shining so bright'
    print(f"{b_chars = }")
    # not all byte sequences are encodeable
    s_random = b_random.decode('utf-8')
    # only allows 0..255
    b_fail = bytes([268])  # raises ValueError


def print_triple_quoted():
    string = """
    The Zen of Python, by Tim Peters

    'Beautiful' is better than 'ugly'.
    Explicit is better than implicit.
    "Simple is better than complex".
    Complex is better than complicated.
    Flat is better than nested.
    Sparse is better than dense.
    Readability counts.
    ..."""
    print(string)


def string_search(word, replace_with='fishcake'):
    sentence = "Be who you are and say what you feel, because those who mind don't matter, and those who matter don't mind."
    # count
    print(f"sentence has {sentence.count(word)} occurrences of '{word}'")
    # find, index
    start_index = sentence.find(word)
    print(f"location of '{word}': {start_index}")
    next_index = sentence.index(word, start_index + len(word))
    print(f"next location of '{word}': {next_index}")
    print(f"{sentence[start_index:start_index + len(word)] = }")
    print(f"{sentence[next_index:next_index + len(word)] = }")
    # replace
    print(f"{sentence.replace(word, replace_with)}")


def string_is_properties(string: str):
    # isalnum, isalpha, isprintable, isspace
    print(f"{string.isalnum() = }")
    print(f"{string.isalpha() = }")
    print(f"{string.isprintable() = }")
    print(f"{string.isspace() = }")
    # isdecimal, isdigit, isnumeric
    print(f"{string.isdigit() = }")
    print(f"{string.isdecimal() = }")
    print(f"{string.isnumeric() = }")
    # isascii, isidentifier
    print(f"{string.isascii() = }")
    print(f"{string.isidentifier() = }")
    # islower, istitle, isupper
    print(f"{string.islower() = }")
    print(f"{string.istitle() = }")
    print(f"{string.isupper() = }")


def slicing_and_dicing_strings(string, tail=" ><|()[]"):
    # strip
    print(f"{string.strip(tail) = }")
    # split
    sentence = "Be|the|change|that|you|wish|to|see|in|the|world."
    print(f"{sentence = }")
    split_sentence = sentence.split('|')
    print(f"{split_sentence = }")
    # partition
    print(f"{sentence.partition('you') = }")
    # join
    print(f"{' '.join(split_sentence) = }")


def string_method_formatting(string: str):
    width, height = shutil.get_terminal_size()
    print(f"terminal dimensions (w,h): {width, height}")
    # justification: rjust, center, ljust, zfill
    print(string.rjust(width))
    print(string.center(width))
    print(string.ljust(width))
    print(string.zfill(width))
    # case: capitalize, swapcase, upper, lower, title
    print(f"{string.capitalize() = }")
    print(f"{string.swapcase() = }")
    print(f"{string.upper().swapcase() = }")
    print(f"{string.upper() = }")
    print(f"{string.title() = }")
    print(f"{string.lower() = }")


def string_format_minilanguage():
    """String formatting using the minilanguage """
    width, height = shutil.get_terminal_size()
    address1 = "14 plowden road"
    address2 = "torquay"
    address3 = "devon"
    address4 = "tq6 1rs"
    address5 = "tel 0742 06538"
    date = "22 december 2007"
    to1 = "sfi centre for research training in genomics data science"
    to2 = "school of mathematics, statistics and applied mathematics"
    to3 = "national university of ireland, galway,"
    to4 = "ireland"
    ref = "application for post as administrator"
    salutation1 = "dear madam/sir"
    # the body is a list of lowercase strings
    body = [
        "lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.",
        "duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.",
        "excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."]
    # first, use map and capitalise each sentence in the list and join into a string separated by spaces
    proper_case_body_string = " ".join(map(lambda s: s.capitalize(), body))
    # use textwrap.wrap() to chop the string into a list of strings each at most 'width' long
    wrapped_body_list = textwrap.wrap(proper_case_body_string, width=width)
    # now join all shortened strings together adding a newline (\n) at the end of each
    # producing a wrapped body
    wrapped_body = "".join(map(lambda s: f"{s:<{width}}\n", wrapped_body_list))
    salutation2 = "yours sincerely"
    signature = "Abott F. Geraldine"
    print(f"""\
{address1.title():>{width}}
{address2.title():>{width}}
{address3.title():>{width}}
{address4.upper():>{width}}
{address5.capitalize():>{width}}
{to1.title():<60}{date.title():>20}
{to2.title():<{width}}
{to3.title():<{width}}
{to4.title():<{width}}

{salutation1.title():<{width}},

{ref.upper():^{width}}

{wrapped_body}

{salutation2.capitalize():<{width}}

{signature:<{width}}
""")


def main():
    # print_5s()
    # working_with_bytes()
    # print_triple_quoted()
    # string_search('who')
    # string_is_properties(input())
    # slicing_and_dicing_strings(input())
    # string_method_formatting(input())
    string_format_minilanguage()
    return 0


if __name__ == '__main__':
    sys.exit(main())
