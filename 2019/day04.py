from collections import Counter


def password(i: int, part: int = 1) -> bool:
    n = str(i)
    result = len(n) == 6 and two_adjecent_digits(n) and never_decreases(n)
    if part == 1:
        return result
    else:
        return result and not_part_of_larger_group(n)


def two_adjecent_digits(n: str) -> bool:
    return any(i == j for i, j in zip(n, n[1:]))


def never_decreases(n: str) -> bool:
    return all(i <= j for i, j in zip(n, n[1:]))


def not_part_of_larger_group(n: str) -> bool:
    c = Counter(n)
    if 2 in c.values():
        return True
    elif any(v > 2 for v in c.values()):
        return False
    else:
        return False


def main(low: int, high: int, part: int = 1) -> int:
    return sum(password(n, part) for n in range(low, high))


if __name__ == "__main__":
    assert never_decreases("111123")
    assert never_decreases("135679")
    assert two_adjecent_digits("122345")
    assert password(111111)
    assert not password(223450)
    assert not password(123789)

    low = 265275
    high = 781584
    print(main(low, high))

    assert not_part_of_larger_group("112233")
    assert not not_part_of_larger_group("123444")
    assert not_part_of_larger_group("111122")

    print(main(low, high, part=2))
