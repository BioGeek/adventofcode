from collections import defaultdict
from typing import Dict, Tuple, List, Union
from pprint import pprint
from functools import reduce


Coordinates = Dict[Tuple[int, int], int]

def manhattan_distance(x: int, y: int, origin_x: int = 0, origin_y: int = 0) -> int:
    """Returns the sum of the absolute difference of cartesian coordinates"""
    return abs(x - origin_x) + abs(y - origin_y)

def create_coords(wire: str) -> Coordinates:
    """For each coordinate that is passes, increase the count by 1."""
    coordinates = {} # type: Coordinates
    x, y = 0, 0
    length = 0
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
            length += 1
            coordinates[(x, y)] = length 
    return coordinates

def get_data() -> List[str]:
    """Read in the data."""
    with open('data/day03.txt') as f:
        wires = f.read().splitlines()
    return wires

def find_crossing_wires(wires: List[str] ) -> int :
    """Return the shortest distance where the wires cross."""
    coords_1, coords_2 = [set(create_coords(wire).keys()) for wire in wires]
    common_coordinates = coords_1.intersection(coords_2)
    return min(manhattan_distance(*coords) for coords in common_coordinates)

def find_minimal_delay(wires: List[str]) -> int:
    """Calculate the number of steps each wire takes to reach each intersection; 
    choose the intersection where the sum of both wires' steps is lowest."""
    coords_1, coords_2 = [create_coords(wire) for wire in wires]
    common_coords = set(coords_1.keys()).intersection(set(coords_2.keys()))
    return min(coords_1[c] + coords_2[c] for c in common_coords)


def draw(wires):
    wire1, wire2 = [set(create_coords(wire).keys()) for wire in wires]
    common_coordinates = wire1.intersection(wire2)
    all_coordinates = wire1.union(wire2)

    xs = [c[0] for c in all_coordinates]
    ys = [c[1] for c in all_coordinates]
    min_x = min(min(xs), 0)
    min_y = min(min(ys), 0)
    max_x = max(max(xs), 0)
    max_y = max(max(ys), 0)
    
    for y in range(max_y+1, min_y-2, -1):
        for x in range(min_x-1, max_x+2):
            if (x, y) == (0, 0):
                print('o', end = '')
            elif (x,y) in all_coordinates:
                if (x, y) in common_coordinates:
                    print('X', end = '')
                else:
                    print('+', end = '')
            else:
                print('.', end= '')
        print() 

def main(part=1) -> int:
    wires = get_data()
    if part == 1:
        return find_crossing_wires(wires)
    else:
        return find_minimal_delay(wires)

if __name__ == '__main__':
    wires_1 = ["R8,U5,L5,D3", "U7,R6,D4,L4"]
    assert find_crossing_wires(wires_1) == 6
    # draw(wires)

    wires_2 = ["R75,D30,R83,U83,L12,D49,R71,U7,L72",
               "U62,R66,U55,R34,D71,R55,D58,R83"]
    assert find_crossing_wires(wires_2) == 159

    wires_3 = ["R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51",
               "U98,R91,D20,R16,D67,R40,U7,R15,U6,R7"]
    assert find_crossing_wires(wires_3) == 135

    print(main(part=1))

    assert find_minimal_delay(wires_1) == 30
    assert find_minimal_delay(wires_2) == 610
    assert find_minimal_delay(wires_3) == 410

    print(main(part=2))
    # print(main(part=2))
