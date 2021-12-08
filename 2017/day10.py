def knot(numbers, current_position, skip_size, lengths):
    # before, current, after = numbers[:current_position], numbers[current_position], numbers[current_position+1:]
    # print(' '.join(map(str, list(before) + [f"[{current}]"] + list(after))))
    numbers = list(numbers)
    for length in lengths:
        if current_position + length < len(numbers):
            print("smaller")
            before, selected, after = (
                numbers[:current_position],
                numbers[current_position : current_position + length],
                numbers[current_position + length :],
            )
            print("before, selected, after:", before, selected, after)
            numbers = before + selected[::-1] + after
            print("new numbers", numbers)
        else:
            print("wraparound")
            left = current_position + length - len(numbers)
            selected_1, middle, selected_2 = (
                numbers[:left],
                numbers[left:current_position],
                numbers[current_position:],
            )
            print("selected_1, middle, selected_2", selected_1, middle, selected_2)
            selected = selected_2 + selected_1
            print("selected", selected)
            selected = selected[::-1]
            print("reversed", selected)
            if not middle:
                numbers = selected[-left:] + selected[:-left]
            else:
                numbers = selected[left:] + middle + selected[:left]
            print("new numbers", numbers)

        current_position = (current_position + length + skip_size) % len(numbers)
        print(
            "current_position",
            current_position,
            "item there:",
            numbers[current_position],
        )
        skip_size += 1
        print("skip_size", skip_size)
        print("current_position + length", current_position + length)

    return numbers[0] * numbers[1]


def main(part: int = 1) -> int:
    with open("2017/data/day10.txt") as f:
        lengths = map(int, f.read().split(","))
    numbers = range(256)
    current_position = 0
    skip_size = 0
    return knot(numbers, current_position, skip_size, lengths)


if __name__ == "__main__":
    numbers = range(5)
    current_position = 0
    skip_size = 0
    lengths = [3, 4, 1, 5]

    assert knot(numbers, current_position, skip_size, lengths) == 12

    print(main())
