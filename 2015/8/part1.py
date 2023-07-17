def strip_escapes(s: str):
    new_s = []
    i = 0
    while i < len(s):
        match s[i]:
            case "\"" | "\'":
                i += 1
            case "\\":
                if s[i+1] != "x":
                    new_s.append(s[i+1])
                    i += 2
                else:
                    new_s.append("Ä")
                    i += 4
            case _:
                new_s.append(s[i])
                i += 1

    return ''.join(new_s)


with open("input.txt", "r") as f:
    lines = f.readlines()
    raws = sum([len(s.strip()) for s in lines])
    non_raws = sum([len(strip_escapes(s.strip())) for s in lines])

    print(raws - non_raws)
