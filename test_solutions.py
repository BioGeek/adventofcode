import importlib
import json

import pytest


@pytest.fixture(scope="session", params=list(range(2017, 2022)))
def year(request):
    return request.param


@pytest.fixture(scope="session", params=list(range(1, 26)))
def day(request):
    return request.param


@pytest.fixture(scope="session", params=(1, 2))
def part(request):
    return request.param


@pytest.fixture(scope="session")
def solution(year, day, part):
    known_incomplete_solutions = {
        2017: {10: [1, 2], 25: [1, 2]},
        2018: {1: [2], 5: [1, 2], 6: [1, 2], 12: [1, 2]},
        2019: {6: [1, 2], 7: [2]},
        2020: {10: [1, 2], 11: [1, 2], 12: [1, 2]},
        2021: {6: [2]},
    }
    if part in known_incomplete_solutions.get(year, {}).get(day, []):
        pytest.skip(
            f"Known incomplete solution for year: {year}, day: {day}, part: {part}"
        )
    try:
        module = importlib.import_module(f"{year}.day{day:02}")
        return module.main(part=part)
    except ModuleNotFoundError:
        pytest.skip(f"No solution found for year: {year}, day: {day}, part: {part}")


@pytest.fixture(scope="session")
def expected(year, day, part):
    with open("expected.json") as f:
        results = json.load(f)
    try:
        return results[str(year)][str(day)][str(part)]
    except KeyError:
        pytest.skip(
            f"No expected output found for year: {year}, day: {day}, part: {part}"
        )


@pytest.mark.timeout(60)
def test_solution(solution, expected):
    if expected is None:
        pytest.skip("No output")

    assert solution == expected
