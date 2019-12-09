from typing import List

WIDTH = 25
HEIGHT = 6


def get_data() -> str:
    with open("data/day08.txt") as f:
        data = f.read()
    return data


def main1(data: str, width: int = WIDTH, height: int = HEIGHT) -> int:
    layers = make_layers(data, width, height)

    zeros = float("inf")
    chosen = ""
    for layer in layers:
        if layer.count("0") < zeros:
            zeros = layer.count("0")
            chosen = layer
    return chosen.count("1") * chosen.count("2")


def main2(data: str, width: int = WIDTH, height: int = HEIGHT) -> str:
    layers = make_layers(data, width, height)

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
    assert main1(data, width=3, height=2) == 1

    # print(main(get_data()))

    data = "0222112222120000"
    assert main2(data, width=2, height=2) == "█ \n █"

    print(main2(get_data()))
