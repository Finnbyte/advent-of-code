def count_encodings(s: str):
    count = 0
    i = 0
    while i < len(s):
        match s[i]:
            case "\"":
                count += 2
            case "\\":
                count += 2
            case _:
                count += 1
        i += 1
    return count + 2  # account for outer quotes


with open("input.txt", "r") as f:
    lines = f.readlines()
    raws = sum([len(s.strip()) for s in lines])
    rawer_raws = [count_encodings(s.strip()) for s in lines]

    print(sum(rawer_raws) - raws)
