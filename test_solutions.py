import importlib
import json

import pytest


@pytest.fixture(scope="session", params=list(range(2017, 2024)))
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
    with open("tests/known_incomplete_solutions.json") as f:
        known_incomplete_solutions = json.load(f)
    if part in known_incomplete_solutions.get(str(year), {}).get(str(day), []):
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
    with open("tests/expected.json") as f:
        results = json.load(f)
    try:
        return results[str(year)][str(day)][str(part)]
    except KeyError:
        pytest.skip(
            f"No expected output found for year: {year}, day: {day}, part: {part}"
        )


@pytest.mark.timeout(60)
def test_solution(solution, expected):
    assert solution == expected
