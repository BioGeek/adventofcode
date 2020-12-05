class BoardingPass:
    def __init__(self, raw: str) -> None:
        self.raw = raw

    def to_binary(self, raw: str, one: str) -> str:
        return "".join("1" if char == one else "0" for char in raw)

    def get_column(self) -> int:
        return int(self.to_binary(self.raw[-3:], "R"), 2)

    def get_row(self) -> int:
        return int(self.to_binary(self.raw[:7], "B"), 2)

    def get_seat_id(self):
        return self.get_row() * 8 + self.get_column()


def main(part: int = 1) -> int:
    with open("2020/data/day05.txt") as fh:
        data = fh.read().splitlines()

    seat_ids = [BoardingPass(line).get_seat_id() for line in data]
    max_seat_id = max(seat_ids)
    if part == 1:
        return max_seat_id
    else:
        front_seat_ids = set(range(12))
        return next(iter(set(range(max_seat_id)) - front_seat_ids - set(seat_ids)))


if __name__ == "__main__":
    assert BoardingPass("BFFFBBFRRR").get_row() == 70
    assert BoardingPass("FFFBBBFRRR").get_row() == 14
    assert BoardingPass("BBFFBBFRLL").get_row() == 102

    assert BoardingPass("BFFFBBFRRR").get_column() == 7
    assert BoardingPass("FFFBBBFRRR").get_column() == 7
    assert BoardingPass("BBFFBBFRLL").get_column() == 4

    assert BoardingPass("BFFFBBFRRR").get_seat_id() == 567
    assert BoardingPass("FFFBBBFRRR").get_seat_id() == 119
    assert BoardingPass("BBFFBBFRLL").get_seat_id() == 820

    print(main())
    print(main(part=2))
