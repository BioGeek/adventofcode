from __future__ import annotations
from typing import Dict, List, NamedTuple, Tuple


class Seat(NamedTuple):
    x: int
    y: int
    value: str

class Layout:

    def __init__(self, data: str) -> None:
        self.grid = [[Seat(x, y, value) for x, value in enumerate(row)]
                    for y, row in enumerate(data.splitlines())]
        self.width = len(self.grid[0])
        self.height = len(self.grid)
                    
    
    def one_round(self) -> List[List[Seat]] :
        new_grid = []
        for y in range(self.height):
            row = []
            for x in range(self.width):
                seat = self.grid[x][y]
                new_seat = self.apply_rule(seat)
                row.append(new_seat)
            new_grid.append(row)
        self.grid =  new_grid
                
    def apply_rule(self, seat: Seat) -> Seat:
        if self.is_empty(seat) and not self.occupied_neighbour_seats(seat):
            return Seat(seat.x, seat.y, '#')
        elif self.is_occupied(seat) and self.occupied_neighbour_seats(seat) >= 4:
            return Seat(seat.x, seat.y, 'L')
        else:
            return seat

    def is_empty(self, seat: Seat) -> bool:
        return seat.value == 'L'

    def is_occupied(self, seat: Seat) -> bool:
        return seat.value == '#'
        
    def occupied_neighbour_seats(self, seat: Seat) -> int:
        return sum(1 for neighbour in self.neighbours(seat) if self.is_occupied(neighbour))

    def neighbours(self, seat: Seat) -> List[Seat]:
        x, y = seat.x, seat.y
        for (new_x, new_y) in ((x+1, y), (x-1, y), (x, y+1), (x, y-1),
            (x+1, y+1), (x-1, y-1), (x+1, y-1), (x-1, y+1)):
            if 0 <= new_x <= self.width and 0 <= new_y <= self.height:
                yield Seat(new_x, new_y, seat.value)

    def plot(self) -> str:
        return '\n'.join(''.join([seat.value for seat in row]) for row in self.grid)




    

"""
class Location:

    def __init__(self, value: str) -> None:
        self.value = value


def neighbors(location: Location) -> Tuple[Tuple[int, int]]: 
    "The eight neighbors (with diagonals)."
    x, y = location.x, location.y
    return ((x+1, y), (x-1, y), (x, y+1), (x, y-1),
            (x+1, y+1), (x-1, y-1), (x+1, y-1), (x-1, y+1))

def make_layout(data: str) -> Dict[Tuple[int, int], Location]:
    layout = {}
    for y, row in enumerate(data.splitlines()):
        for x, value in enumerate(row):
            layout[(x, y)] = Location(value)
    return layout
"""


if __name__ == '__main__':
    LAYOUT = """L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL"""

    layout = Layout(LAYOUT)
    # first_seat = layout.grid[0][0]
    # print(list(layout.neighbours(first_seat)))
    # print(layout.occupied_neighbour_seats(first_seat))
    layout.one_round()
    print(layout.plot())
