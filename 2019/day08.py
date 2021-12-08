from typing import List

WIDTH = 25
HEIGHT = 6


def main(
    data: str = "",
    width: int = WIDTH,
    height: int = HEIGHT,
    part: int = 1,
) -> int | str:
    if not data:
        with open("2019/data/day08.txt") as f:
            data = f.read().strip()
    layers = make_layers(data, width, height)
    if part == 1:
        zeros = float("inf")
        chosen = ""
        for layer in layers:
            if layer.count("0") < zeros:
                zeros = layer.count("0")
                chosen = layer
        return chosen.count("1") * chosen.count("2")
    else:
        # 0 is black, 1 is white, and 2 is transparent.
        image = []
        colors = {"0": "█", "1": " "}
        transposed = list(zip(*layers))
        for stack in transposed:
            while stack[0] == "2":
                stack = stack[1:]
            image.append(colors[stack[0]])

        result = "\n".join(
            ["".join(image[i : i + width]) for i in range(0, len(image), width)]
        )
        return result


def make_layers(data: str, width: int = WIDTH, height: int = HEIGHT) -> List[str]:
    length = width * height
    return [data[i : i + length] for i in range(0, len(data), length)]


if __name__ == "__main__":
    data = "123456789012"
    assert main(data=data, width=3, height=2) == 1

    print(main())

    data = "0222112222120000"
    assert main(data=data, width=2, height=2, part=2) == "█ \n █"

    print(main(part=2))
