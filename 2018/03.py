import re
from collections import defaultdict


def main(data=None, part=1):
    if data is None:
        with open("data/03.txt") as f:
            data = f.read()
    fabric = defaultdict(list)
    m = re.findall(r"#(\d+) @ (\d+),(\d+): (\d+)x(\d+).*", data)
    if m:
        for line in m:
            id_, left_edge, top_edge, width, height = map(int, line)
            # fabric[(left_edge, top_edge)].append(id_)
            for col in range(left_edge, left_edge + width):
                for row in range(top_edge, top_edge + height):
                    fabric[(row, col)].append(id_)
                    # print((row, col), id_)
            # print(dict((k, v) for k, v in fabric.items() if len(v) > 1))
    if part == 1:
        return sum(1 for v in fabric.values() if len(v) > 1)
    else:
        overlap = [v for v in fabric.values() if len(v) > 1]
        overlap = list(sorted(set([elem for sublst in overlap for elem in sublst])))
        # https://stackoverflow.com/a/20718334/50065
        max_id = int(m[-1][0])
        return sum(range(overlap[0], max_id + 1)) - sum(overlap)


if __name__ == "__main__":
    data = """#1 @ 1,3: 4x4
#2 @ 3,1: 4x4
#3 @ 5,5: 2x2"""
    assert main(data=data) == 4
    # print(main())
    assert main(data=data, part=2) == 3
    print(main(part=2))
