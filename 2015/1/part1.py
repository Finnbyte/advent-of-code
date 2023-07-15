floor = 0

with open("input.txt", "r") as f:
    contents = f.readline()
    for i, paren in enumerate(contents):
        if paren == "(":
            floor += 1
        if paren == ")":
            floor -= 1

print(floor)
