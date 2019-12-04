def password(i: int) -> bool:
    n = str(i)
    return len(n) == 6 and two_adjecent_digits(n) and never_decreases(n)

def two_adjecent_digits(n: str) -> bool:
    return any(i == j for i, j in zip(n, n[1:]))

def never_decreases(n: str) -> bool:
    return all(i <= j for i, j in zip(n, n[1:]))

def main(low: int, high: int) -> int:
    return sum(password(n) for n in range(low, high))

if __name__ == '__main__':
    assert never_decreases("111123")
    assert never_decreases("135679")
    assert two_adjecent_digits("122345")
    assert password(111111)
    assert not password(223450)
    assert not password(123789)

    low = 265275
    high = 781584
    print(main(low, high))