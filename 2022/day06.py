def find_marker(buffer: str, n: int) -> int:
    for i in range(n, len(buffer)):
        if len(set(buffer[i - n : i])) == n:
            return i
    return -1


def main(part: int = 1):
    with open("2022/data/day06.txt") as f:
        buffer = f.read()
    if part == 1:
        return find_marker(buffer, 4)
    return find_marker(buffer, 14)


if __name__ == "__main__":
    assert find_marker("mjqjpqmgbljsphdztnvjfqwrcgsmlb", 4) == 7
    assert find_marker("bvwbjplbgvbhsrlpgdmjqwftvncz", 4) == 5
    assert find_marker("nppdvjthqldpwncqszvftbrmjlhg", 4) == 6
    assert find_marker("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", 4) == 10
    assert find_marker("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", 4) == 11

    assert find_marker("mjqjpqmgbljsphdztnvjfqwrcgsmlb", 14) == 19
    assert find_marker("bvwbjplbgvbhsrlpgdmjqwftvncz", 14) == 23
    assert find_marker("nppdvjthqldpwncqszvftbrmjlhg", 14) == 23
    assert find_marker("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", 14) == 29
    assert find_marker("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", 14) == 26

    print(main())
    print(main(part=2))
