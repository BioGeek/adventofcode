import math
from typing import Dict, List, Tuple

COLORS = ("red", "green", "blue")


def parse(game: str) -> Tuple[int, List[Dict[str, int]]]:
    game_str, cubesets = game.split(":")
    game_nr = int(game_str.split()[-1])
    all_cubes = []
    for cubeset in cubesets.split(";"):
        cubes = {}
        for cube in cubeset.split(","):
            count, color = cube.split()
            cubes[color] = int(count)
        all_cubes.append(cubes)
    return game_nr, all_cubes


def possible_game(cube: Dict[str, int]) -> bool:
    # only 12 red cubes, 13 green cubes, and 14 blue cubes
    limit = {"red": 12, "green": 13, "blue": 14}
    return all(limit[color] >= cube[color] for color in cube)


def possible_games(games: str) -> int:
    total = 0
    for game in games.splitlines():
        game_nr, cubes = parse(game)
        if all(possible_game(cube) for cube in cubes):
            total += game_nr
    return total


def fewest_number_of_cubes_of_each_color(cubes: List[Dict[str, int]]) -> Dict[str, int]:
    return {color: max(cube.get(color, 0) for cube in cubes) for color in COLORS}


def power(cubes: List[Dict[str, int]]) -> int:
    return math.prod(
        fewest_number_of_cubes_of_each_color(cubes)[color] for color in COLORS
    )


def powersum(games: str) -> int:
    total = 0
    for game in games.splitlines():
        _, cubes = parse(game)
        total += power(cubes)
    return total


def main(part: int = 1) -> int:
    with open("2023/data/day02.txt") as f:
        games = f.read()
    if part == 1:
        return possible_games(games)
    else:
        return powersum(games)


if __name__ == "__main__":
    games = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
 Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
 Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
 Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
 Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"""

    _, cubes = parse("Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green")
    assert all(possible_game(cube) for cube in cubes)
    _, cubes = parse("Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue")
    assert all(possible_game(cube) for cube in cubes)
    _, cubes = parse(
        "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red"
    )
    assert not all(possible_game(cube) for cube in cubes)
    _, cubes = parse(
        "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red"
    )
    assert not all(possible_game(cube) for cube in cubes)
    _, cubes = parse("Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green")
    assert all(possible_game(cube) for cube in cubes)

    assert possible_games(games) == 8

    print(main())

    _, cubes = parse("Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green")
    assert fewest_number_of_cubes_of_each_color(cubes) == {
        "red": 4,
        "green": 2,
        "blue": 6,
    }
    assert power(cubes) == 48
    _, cubes = parse("Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue")
    assert fewest_number_of_cubes_of_each_color(cubes) == {
        "red": 1,
        "green": 3,
        "blue": 4,
    }
    assert power(cubes) == 12
    _, cubes = parse(
        "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red"
    )
    assert fewest_number_of_cubes_of_each_color(cubes) == {
        "red": 20,
        "green": 13,
        "blue": 6,
    }
    assert power(cubes) == 1560
    _, cubes = parse(
        "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red"
    )
    assert fewest_number_of_cubes_of_each_color(cubes) == {
        "red": 14,
        "green": 3,
        "blue": 15,
    }
    assert power(cubes) == 630
    _, cubes = parse("Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green")
    assert fewest_number_of_cubes_of_each_color(cubes) == {
        "red": 6,
        "green": 3,
        "blue": 2,
    }
    assert power(cubes) == 36

    assert powersum(games) == 2286

    print(main(part=2))
