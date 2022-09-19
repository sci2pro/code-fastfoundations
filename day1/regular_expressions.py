import re
import sys

# this string is globally visible; main block
string = """Is it true that Jonathan's (Joramson) phone number is +353-8320-209-138? I have been calling him for ages!
Do you happen to have his email? What? jonathan@joramson.com! I should have tried that ages ago!!!
"""


def get_match_object():
    """When a match occurs re.search() returns a re.Match object"""
    result = re.search(r"phone", string)  # r-strings are literal strings; no escaping required
    print(f"{result.group()}")
    # result is a re.Match object
    # if we have a match then it evaluates to True
    if result:
        print(f"{result.group() = }")
        print(f"{result.group(0) = }")
        print(f"{result.groups() = }")
        print(f"{result.start() = }")
        print(f"{result.end() = }")
        print(f"{result.span() = }")
        print(f"{result.pos = }")
        print(f"{result.endpos = }")
        print(f"{result.re = }")
        print(f"{result.string = }")
    else:
        print("No match!")


def character_classes():
    print(string)
    regex = r"."
    result = re.search(regex, string)  # . matches any except \n
    print(f"{regex:<30}: {result.group()}")
    regex = r"\w"
    result = re.search(regex, string)  # \w matches any unicode character
    print(f"{regex:<30}: {result.group()}")
    regex = r"\d"
    result = re.search(regex, string)  # \d matches any single numeral 0-9
    print(f"{regex:<30}: {result.group()}")
    regex = r"\s"
    result = re.search(regex, string)  # \s matches whitespace ' ', '\t'
    print(f"{regex:<30}: {result.group()}")
    # conversely
    regex = r"\W"
    result = re.search(regex, string)  # \W equivalent of 'not \w'
    print(f"{regex:<30}: {result.group()}")
    regex = r"\D"
    result = re.search(regex, string)  # \D matches any non-digit
    print(f"{regex:<30}: {result.group()}")
    regex = r"\S"
    result = re.search(regex, string)  # \S matches any non-whitespace
    print(f"{regex:<30}: {result.group()}")


def positional_anchors():
    print(string, len(string))
    # ^ - match to the beginning of the string
    regex = r"^\d"
    result = re.search(regex, string)
    print(f"{regex:<30}: {result}")
    # $ - match to the end of the string
    regex = r"\W$"
    result = re.search(regex, string)
    print(f"{regex:<30}: {result.group()}")


def quantifiers():
    """Combining character classes with quantifiers"""
    lines = string.split('\n')  # split at the \n
    first_line = lines[0]
    print(first_line)
    print(len(first_line))
    # any character
    regex = r".*"
    result = re.search(regex, string)  # * means 0 or more
    print(f"{regex:<30}: {result.group()}")
    regex = r".+"
    result = re.search(regex, string)  # + means 1 or more
    print(f"{regex:<30}: {result.group()}")
    regex = r".?"
    result = re.search(regex, string)  # ? means 0 or 1
    print(f"{regex:<30}: {result.group()}")
    # \w
    regex = r"\w*"
    result = re.search(regex, string)
    print(f"{regex:<30}: {result.group()}")
    # combine .* with a character class and quantifier
    regex = r".*\d+"
    result = re.search(regex, string)  # *, +, ? are greedy
    print(f"{regex:<30}: {result.group()}")
    regex = r".*?\d+"
    result = re.search(regex, string)  # *?, +?, ?? are non-greedy
    print(f"{regex:<30}: {result.group()}")
    regex = r"\d{2}"
    result = re.search(regex, string)  # specify the size of the match
    print(f"{regex:<30}: {result.group()}")


def custom_classes_and_escaping_sequences():
    # create your own character class
    regex = r"[\w\d]"
    result = re.search(regex, string)  # combine word and digits to match any
    print(f"{regex:<30}: {result.group()}")
    regex = r"[\w\d]+"
    result = re.search(regex, string)  # add quantifiers
    print(f"{regex:<30}: {result.group()}")
    regex = r"[-+\w\d]{6,}"  # six or more long
    result = re.search(regex, string)  # add more characters
    print(f"{regex:<30}: {result.group()}")
    # negating
    regex = r"[^\w\d]+$"
    result = re.search(regex, string)  # neither word not digits at the end
    print(f"{regex:<30}: {result.group()}")
    # group using parentheses ()
    regex = r"[(]\w+[)]"  # surname
    result = re.search(regex, string)  # combine word and digits to match any
    print(f"{regex:<30}: {result.group()}")
    # how to match regex literal characters?
    regex = r"\d{3}[?]"
    result = re.search(regex, string)  # make it a group
    print(f"{regex:<30}: {result.group()}")


def grouping_and_capturing_regexes():
    regex = r"[-+\d]+"  # phone number
    result = re.search(regex, string)  # combine word and digits to match any
    print(f"{regex:<30}: {result.group()}")
    # print(f"{regex:<30}: {result.group(1)}") # IndexError
    regex = r"([-+\d]+)"
    result = re.search(regex, string)  # make it a group
    print(f"{regex:<30}: {result.group(1)}")
    regex = r"([-+\d]+).*?(\w{7})"
    result = re.search(regex, string)  # combine with another group
    print(f"{regex:<30}: {result.group(1)}")
    print(f"{regex:<30}: {result.group(2)}")
    regex = r"(\w{3}|\d{3})"  # match one of many using |
    result = re.search(regex, string)  # make it a group
    print(f"{regex:<30}: {result.group(1)}")
    regex = r"(?P<phone_number>[-+\d]+)"  # give the variable a name
    result = re.search(regex, string)
    print(f"{regex:<30}: {result.group('phone_number')}")


def control_flags():
    regex = r"(\s(\w+)[?])+"
    result = re.search(regex, string, re.DOTALL)
    print(f"{regex:<30}: {result.group()}")
    regex = r"(j.+?)\s.*?(j.+?)\s.*?(j.+?)\s"
    result = re.search(regex, string, re.DOTALL | re.IGNORECASE)
    print(f"{regex:<30}: {result.groups()}")
    regex = r".{6}$"
    result = re.search(regex, string, re.DOTALL)
    print(f"{regex:<30}: {result.group()}")
    regex = r".{6}$"
    result = re.search(regex, string, re.DOTALL | re.MULTILINE)
    print(f"{regex:<30}: {result.group()}")


def main():
    # get_match_object()
    # character_classes()
    # positional_anchors()
    quantifiers()
    # custom_classes_and_escaping_sequences()
    # grouping_and_capturing_regexes()
    # control_flags()
    return 0


if __name__ == '__main__':
    sys.exit(main())
