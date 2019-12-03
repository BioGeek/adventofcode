from collections import defaultdict
from typing import DefaultDict, Tuple, List, Union
from pprint import pprint

Coordinates = DefaultDict[Tuple[int, int], int]

def manhattan_distance(x: int, y: int, origin_x: int = 0, origin_y: int = 0) -> int:
    """Returns the sum of the absolute difference of cartesian coordinates"""
    return abs(x - origin_x) + abs(y - origin_y)

def create_coords(wires: List[str]) -> Coordinates:
    """For each coordinate that is passes, increase the count by 1."""
    coordinates = defaultdict(list) # type: Coordinates
    for i, wire in enumerate(wires):
        x, y = 0, 0
        for instruction in wire.split(','):
            direction, distance = instruction[0], int(instruction[1:])
            for step in range(distance):
                if direction == 'R':
                    x += 1
                elif direction == 'L':
                    x -= 1
                elif direction == 'U':
                    y += 1
                elif direction == 'D':
                    y -= 1
                else:
                    raise RuntimeError(f"Unrecognized direction: {direction}")
                coordinates[(x, y)].append(i)
    return coordinates

def get_data() -> List[str]:
    """Read in the data."""
    with open('data/day03.txt') as f:
        wires = f.read().splitlines()
    return wires

def find_crossing_wires(coordinates: Coordinates) -> int :
    """Return the shortest distance where hte wires cross."""
    shortest_distance = 1_000_000
    for coords in coordinates:
        if sorted(coordinates[coords]) == [0, 1] and coords != (0, 0):
            if manhattan_distance(*coords) < shortest_distance:
                shortest_distance = manhattan_distance(*coords)
    return shortest_distance

def draw(coordinates):
    crossing_coordinates = {k: manhattan_distance(*k) for (k, v) in coordinates.items() if sorted(v) == [0, 1]}
    pprint(crossing_coordinates)
    xs = [c[0] for c in coordinates.keys()]
    ys = [c[1] for c in coordinates.keys()]
    min_x = min(min(xs), 0)
    min_y = min(min(ys), 0)
    max_x = max(max(xs), 0)
    max_y = max(max(ys), 0)
    
    for y in range(max_y+1, min_y-2, -1):
        for x in range(min_x-1, max_x+2):
            if (x, y) == (0, 0):
                print('o', end = '')
            elif (x,y) in coordinates:
                if sorted(coordinates[(x, y)]) == [1, 2]:
                    print('X', end = '')
                else:
                    print('+', end = '')
            else:
                print('.', end= '')
        print() 

def main() -> int:
    wires = get_data()
    coordinates = create_coords(wires)
    return find_crossing_wires(coordinates)


if __name__ == '__main__':
    wires = ["R8,U5,L5,D3", "U7,R6,D4,L4"]
    assert find_crossing_wires(create_coords(wires)) == 6
    # draw(create_coords(wires))

    wires = ["R75,D30,R83,U83,L12,D49,R71,U7,L72",
             "U62,R66,U55,R34,D71,R55,D58,R83"]
    assert find_crossing_wires(create_coords(wires)) == 159

    wires = ["R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51",
             "U98,R91,D20,R16,D67,R40,U7,R15,U6,R7"]
    assert find_crossing_wires(create_coords(wires)) == 135

    print(main())
