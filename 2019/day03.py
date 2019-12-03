from collections import defaultdict
from typing import DefaultDict, Tuple, List, Union

Coordinates = DefaultDict[Tuple[int, int], int]

def manhattan_distance(x: int, y: int) -> int:
    return abs(x) + abs(y)

def create_coords(wires: List[str]) -> Coordinates:
    coordinates = defaultdict(int) # type: Coordinates
    for wire in wires:
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
                coordinates[(x, y)] += 1
    return coordinates

def get_data() -> List[str]:
    with open('data/day03.txt') as f:
        wires = f.read().splitlines()
    return wires

def find_crossing_wires(coordinates: Coordinates) -> int :
    shortest_distance = 1_000_000
    for coords in coordinates:
        if coordinates[coords] > 1 and coords != (0, 0):
            # print(coords)
            if manhattan_distance(*coords) < shortest_distance:
                shortest_distance = manhattan_distance(*coords)
    return shortest_distance

def main() -> int:
    wires = get_data()
    coordinates = create_coords(wires)
    return find_crossing_wires(coordinates)


if __name__ == '__main__':
    # print(crossing_wires())

    wires = ["R8,U5,L5,D3", "U7,R6,D4,L4"]
    assert find_crossing_wires(create_coords(wires)) == 6

    wires = ["R75,D30,R83,U83,L12,D49,R71,U7,L72",
             "U62,R66,U55,R34,D71,R55,D58,R83"]
    assert find_crossing_wires(create_coords(wires)) == 159

    wires = ["R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51",
             "U98,R91,D20,R16,D67,R40,U7,R15,U6,R7"]
    assert find_crossing_wires(create_coords(wires)) == 135

    print(main())
    

