import itertools
import re

with open("input.txt", "r") as f:
    dest = dict()
    cities = set()
    for line in f.readlines():
        (city1, city2, dst) = re.split(" to | = ", line.strip())
        dest[(city1, city2)] = int(dst); dest[(city2, city1)] = int(dst)
        cities.add(city1); cities.add(city2)

    best = 0
    for route in itertools.permutations(list(cities)):
        cost = 0
        for city1, city2 in zip(route[:-1], route[1:]):
            cost += dest[(city1, city2)]
        best = cost if best < cost else best

    print(best)
