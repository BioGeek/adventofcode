from math import floor


def calculate_fuel(mass: int) -> int:
    """
    To find the fuel required for a module, take its mass,
     divide by three, round down, and subtract 2.
    """
    return floor(mass / 3) - 2


def calculate_fuel_better(mass: int) -> int:
    """
    For each module mass, calculate its fuel and add it to
    the total. Then, treat the fuel amount you just calculated
    as the input mass and repeat the process, continuing until
    a fuel requirement is zero or negative.
    """
    fuel = calculate_fuel(mass)
    total_fuel = 0
    while fuel > 0:
        total_fuel += fuel
        fuel = calculate_fuel(fuel)
    return total_fuel


def main(part: int = 1) -> int:
    """
    What is the sum of the fuel requirements for all of
    the modules on your spacecraft?
    """
    with open("2019/data/day01.txt") as fh:
        masses = map(int, fh.read().splitlines())
    if part == 1:
        func = calculate_fuel
    else:
        func = calculate_fuel_better

    return sum(func(mass) for mass in masses)


if __name__ == "__main__":
    assert calculate_fuel(12) == 2
    assert calculate_fuel(14) == 2
    assert calculate_fuel(1969) == 654
    assert calculate_fuel(100756) == 33583

    print(main())

    assert calculate_fuel_better(14) == 2
    assert calculate_fuel_better(1969) == 966
    assert calculate_fuel_better(100756) == 50346

    print(main(part=2))
