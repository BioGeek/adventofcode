from itertools import chain, cycle, dropwhile


def lanternfish_timer(start_at: int):
    if start_at == 8:
        return chain([8, 7], cycle(range(6, -1, -1)))
    return dropwhile(lambda x: x > start_at, cycle(range(6, -1, -1)))


def spawn(ages: str, days: int) -> int:
    start_times = map(int, ages.split(","))
    internal_timers = [lanternfish_timer(start_time) for start_time in start_times]

    for i in range(days + 1):
        print(f"{i = }")
        day = [next(internal_timer) for internal_timer in internal_timers]
        # print(day)
        print(f"{day.count(0) = }")
        print(f"{len(day) = }")
        for _offspring in range(day.count(0)):
            internal_timers.append(lanternfish_timer(8))
    return len(day)


def main(days: int = 80, part: int = 1) -> int:
    with open("2021/data/day06.txt") as f:
        ages = f.read()
    return spawn(ages, days)


if __name__ == "__main__":
    ages = "3,4,3,1,2"

    internal_timer = lanternfish_timer(3)
    assert [next(internal_timer) for _ in range(10)] == [3, 2, 1, 0, 6, 5, 4, 3, 2, 1]

    internal_timer = lanternfish_timer(8)
    assert [next(internal_timer) for _ in range(20)] == [
        8,
        7,
        6,
        5,
        4,
        3,
        2,
        1,
        0,
        6,
        5,
        4,
        3,
        2,
        1,
        0,
        6,
        5,
        4,
        3,
    ]

    assert spawn(ages, 18) == 26
    assert spawn(ages, 80) == 5934

    print(main())

    assert spawn(ages, 256) == 26984457539
