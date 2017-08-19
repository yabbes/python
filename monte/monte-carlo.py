#! /usr/bin/env python3
# Monte Carlo simulation / inspiration yt:Socratica

import random


def random_walk(n):
    """Return coordinates after 'n' block random walk."""
    x = 0
    y = 0
    for i in range(n):
        step = random.choice(['N', 'S', 'E', 'W'])
        if step == 'N':
            y = y + 1
        elif step == 'E':
            y = y - 1
        elif step == 'E':
            x = x + 1
        else:
            x = x - 1
    return (x, y)

n = 2
dis = 0

for i in range(n):
    walk = random_walk(10)
    print(walk, "Distance from home = ",
          abs(walk[0]) + abs(walk[1]))
    dis += abs(walk[0]) + abs(walk[1])
mean = dis / n
print("mean: {}".format(mean))
