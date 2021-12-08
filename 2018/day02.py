def main(part=1, data=None):
    if data is None:
        with open("2018/data/02.txt") as f:
            data = f.read().splitlines()
    elif isinstance(data, str):
        data = [data]
    if part == 1:
        twos = 0
        threes = 0
        for word in data:
            letters = set(word)
            if any(word.count(letter) == 2 for letter in letters):
                twos += 1
            if any(word.count(letter) == 3 for letter in letters):
                threes += 1
        return twos * threes
    else:
        data = sorted(data)
        for first, second in zip(data, data[1:] + data[:1]):
            if sum(f != s for (f, s) in zip(first, second)) == 1:
                return "".join([f for f, s in zip(first, second) if f == s])


if __name__ == "__main__":
    assert (
        main(data="abcdef") == 0
    )  # no letters that appear exactly two or three times.
    assert (
        main(data="bababc") == 1
    )  # contains two a and three b, so it counts for both.
    assert (
        main(data="abbcde") == 0
    )  # contains two b, but no letter appears exactly three times.
    assert (
        main(data="abcccd") == 0
    )  # contains three c, but no letter appears exactly two times.
    assert (
        main(data="aabcdd") == 0
    )  # contains two a and two d, but it only counts once.
    assert main(data="abcdee") == 0  # contains two e.
    assert (
        main(data="ababab") == 0
    )  # contains three a and three b, but it only counts once.
    assert (
        main(
            data=["abcdef", "bababc", "abbcde", "abcccd", "aabcdd", "abcdee", "ababab"]
        )
        == 12
    )
    print(main())
    assert (
        main(
            data=["abcde", "fghij", "klmno", "pqrst", "fguij", "axcye", "wvxyz"], part=2
        )
        == "fgij"
    )
    print(main(part=2))
