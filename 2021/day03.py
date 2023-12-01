from collections import Counter
from typing import List


def power_consumption(binary_numbers: List[str]) -> int:
    γ = gamma_rate(binary_numbers)
    ε = epsilon_rate(binary_numbers)
    return γ * ε


def get_rate(binary_numbers: List[str], common: int) -> int:
    binary = "".join(
        Counter(bits).most_common()[common][0] for bits in zip(*binary_numbers)
    )
    return int(binary, 2)


def epsilon_rate(binary_numbers: List[str]) -> int:
    """The epsilon rate can be determined by finding the most common bit in the
    corresponding position of all numbers in the diagnostic report"""
    return get_rate(binary_numbers, common=-1)


def gamma_rate(binary_numbers: List[str]) -> int:
    """The gamma rate can be determined by finding the most common bit in the
    corresponding position of all numbers in the diagnostic report"""
    return get_rate(binary_numbers, common=0)


def life_support_rating(binary_numbers: List[str]) -> int:
    o = oxygen_generator_rating(binary_numbers)
    c = CO2_scrubber_rating(binary_numbers)
    return o * c


def bit_criteria(
    binary_numbers: List[str], common: int, keep: str, position: int = 0
) -> int:
    bits = list(zip(*binary_numbers))
    bits_at_position = Counter(bits[position])
    if bits_at_position["1"] == bits_at_position["0"]:
        value = keep
    else:
        value = bits_at_position.most_common()[common][0]
    remaining = [number for number in binary_numbers if number[position] == value]
    if len(remaining) == 1:
        return int(remaining[0], 2)
    position += 1
    return bit_criteria(
        binary_numbers=remaining, common=common, keep=keep, position=position
    )


def oxygen_generator_rating(binary_numbers: List[str]) -> int:
    """To find oxygen generator rating, determine the most common value (0 or 1) in the
    current bit position, and keep only numbers with that bit in that position. If 0 and
    1 are equally common, keep values with a 1 in the position being considered."""
    return bit_criteria(binary_numbers, common=0, keep="1")


def CO2_scrubber_rating(binary_numbers: List[str]) -> int:
    """To find CO2 scrubber rating, determine the least common value (0 or 1) in the
    current bit position, and keep only numbers with that bit in that position. If 0 and
    1 are equally common, keep values with a 0 in the position being considered."""
    return bit_criteria(binary_numbers, common=-1, keep="0")


def binary_numbers(report: str) -> List[str]:
    return report.splitlines()


def main(part: int = 1) -> int:
    with open("2021/data/day03.txt") as f:
        report = f.read()
    if part == 1:
        return power_consumption(binary_numbers(report))
    return life_support_rating(binary_numbers(report))


if __name__ == "__main__":
    report = """00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010"""
    assert power_consumption(binary_numbers(report)) == 198
    assert life_support_rating(binary_numbers(report)) == 230

    print(main())
    print(main(part=2))
