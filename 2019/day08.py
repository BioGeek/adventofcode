from typing import List

WIDTH = 25
HEIGHT = 6


def get_data() -> str:
    with open("data/day08.txt") as f:
        data = f.read()
    return data


def main(data: str, width: int = WIDTH, height: int = HEIGHT, part: int = 1) -> int:
    layers = make_layers(data, width, height)

    if part == 1:
        zeros = float("inf")
        chosen = ""
        for layer in layers:
            if layer.count("0") < zeros:
                zeros = layer.count("0")
                chosen = layer
        result = chosen.count("1") * chosen.count("2")

    return result


def make_layers(data: str, width: int = WIDTH, height: int = HEIGHT) -> List[str]:
    length = width * height
    return [data[i : i + length] for i in range(0, len(data), length)]


if __name__ == "__main__":
    data = "123456789012"
    assert main(data, width=3, height=2) == 1

    print(main(get_data()))
