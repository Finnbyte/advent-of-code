def count_chars(s: str) -> int:
    count = 0
    i = 1
    while i < len(s)-1:
        count += 1
        if s[i] == "\\":
            match s[i+1]:
                case "\"" | "\\":
                    i += 2
                case "x":
                    i += 4
        else:
            i += 1

    return count


with open("input.txt", "r") as f:
    lines = f.readlines()

    raws = sum([len(s.strip()) for s in lines])
    non_raws = sum([count_chars(s.strip()) for s in lines])

    print(raws - non_raws)
