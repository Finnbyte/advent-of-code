import re


def is_nice(s: str):
    return (re.search(r"(..).*\1", s) and
            re.search(r"(.).\1", s))


with open("input.txt", "r") as f:
    strings: list[str] = f.readlines()
    nice_strings: int = len(list(filter(lambda s: is_nice(s), strings)))
    print(nice_strings)
