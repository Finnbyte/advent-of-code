def required_paper(length: int, width: int, height: int):
    return 2*length*width + 2*width*height + 2*height*length


def extra_paper(length: int, width: int, height: int):
    return min(length*width, width*height, height*length)


papers = []
with open("input.txt", "r") as f:
    for line in f.readlines():
        (length, width, height) = line.split("x")

        papers.append(
            required_paper(int(length), int(width), int(height)) +
            extra_paper(int(length), int(width), int(height)))

print("Papers:", sum(papers))
