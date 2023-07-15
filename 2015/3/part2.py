visited = {}
visited_houses = 0
santa = {"x": 0, "y": 0}
robo_santa = {"x": 0, "y": 0}

with open("input.txt", "r") as f:
    contents = f.readline()
    for i, arrow in enumerate(contents):
        s = santa if i % 2 == 0 else robo_santa
        axis = "x" if arrow in "<>" else "y"
        s[axis] += 1 if arrow in ">^" else -1

        if visited.get((s["x"], s["y"])) is None:
            visited_houses += 1
            visited[(s["x"], s["y"])] = True

print(visited_houses)
