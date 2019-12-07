from collections import defaultdict
from pprint import pprint


import sys

sys.setrecursionlimit(2000)

lines = """COM)B
B)C
C)D
D)E
E)F
B)G
G)H
D)I
E)J
J)K
K)L""".splitlines()

"""
        G - H       J - K - L
       /           /
COM - B - C - D - E - F
               \
                I
"""

with open('data/day06.txt') as f:
    lines = f.read().splitlines()

planets = defaultdict(list)
for line in lines:
    a, b = line.split(')')
    planets[a].append(b)


# pprint(planets)

class Tree:
    def __init__(self, name, children):
        self.name = name
        self.children = []
        self.parent = None
        for child_name in children:
            child = Tree(child_name, planets[child_name])
            child.parent = self
            self.children.append(child)

    def __str__(self):
        result = f"{self.name}"
        if self.children:
            kids = '(' + ', '.join([str(child) for child in self.children]) + ')'
        else:
            kids = ''
        return f"{result} {kids}"


root = Tree('COM', planets['COM'])

grand_total = 0

def count(current, total, previous):
    global grand_total 
    for child in current.children:
        total = 1 + previous
        grand_total += total
        # print(child.name, previous, total, grand_total) 
        count(child, total, total)
        
    return grand_total

print(count(root, 0, 0))

