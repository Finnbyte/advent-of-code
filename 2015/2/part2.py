def required_paper(length: int, width: int, height: int):
    return 2*length*width + 2*width*height + 2*height*length


def extra_paper(length: int, width: int, height: int):
    return min(length*width, width*height, height*length)


def required_ribbon(length: int, width: int, height: int) -> int:
    sorted_params = sorted([length, width, height])
    return sorted_params[0]*2 + sorted_params[1]*2


def extra_ribbon(length: int, width: int, height: int):
    return length*width*height


papers = []
ribbons = []
with open("input.txt", "r") as f:
    for line in f.readlines():
        (length, width, height) = line.split("x")

        papers.append(
            required_paper(int(length), int(width), int(height)) +
            extra_paper(int(length), int(width), int(height)))
        ribbons.append(
            required_ribbon(int(length), int(width), int(height)) +
            extra_ribbon(int(length), int(width), int(height)))

print("Papers:", sum(papers))
print("Ribbons:", sum(ribbons))
