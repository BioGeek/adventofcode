from typing import Any, Dict, List, Tuple


def make_adaptors(data: str) -> List[int]:
    return [int(adaptor) for adaptor in data.splitlines()]


def device_joltage(adaptors: List[int]) -> int:
    return max(adaptors) + 3


def make_graph(adaptors: List[int]) -> Dict[int, List[int]]:
    start = 0
    end = device_joltage(adaptors)
    all_adaptors = sorted([start, end] + adaptors)
    graph = {}
    for adaptor in all_adaptors:
        graph[adaptor] = [
            a for a in all_adaptors if a in range(adaptor + 1, adaptor + 4)
        ]
    return graph


def longest_path(graph, start, path=None):
    # adapted from https://stackoverflow.com/a/14512531/50065
    nodes = {}
    if path is None:
        path = []
    path = path + [start]
    for node in graph[start]:
        if node not in path:
            deepest_node, max_depth, max_path = longest_path(graph, node, path)
            print(deepest_node, max_depth, max_path)
            nodes[node] = (deepest_node, max_depth, max_path)
    max_depth = -1
    deepest_node = start
    max_path = []
    for _k, v in nodes.items():
        if v[1] > max_depth:
            deepest_node = v[0]
            max_depth = v[1]
            max_path = v[2]
    return deepest_node, max_depth + 1, max_path + [start]


def dict_to_tuple(d: Dict) -> Tuple[Tuple[Any, Any], ...]:
    return tuple((k, d[k]) for k in sorted(d.keys()))


def use_all_adapters(adaptors: List[int]) -> int:
    graph = make_graph(adaptors)
    _, _, path = longest_path(dict_to_tuple(graph), 0)
    diffs = [(a - b) for a, b in zip(path, path[1:])]
    return diffs.count(1) * diffs.count(3)


def main(part: int = 1) -> int:
    with open("2020/data/day10.txt") as fh:
        data = fh.read()

    adapters = make_adaptors(data)
    return use_all_adapters(adapters)


if __name__ == "__main__":
    ADAPTERS = """16
10
15
5
1
11
7
19
6
12
4"""

    LARGER = """28
33
18
42
31
14
46
20
48
47
24
23
49
45
19
38
39
11
1
32
25
35
8
17
7
9
4
2
34
10
3"""

    # assert device_joltage(make_adaptors(ADAPTERS)) == 22
    # assert use_all_adapters(make_adaptors(ADAPTERS)) == 35

    # assert device_joltage(make_adaptors(LARGER)) == 52
    # assert use_all_adapters(make_adaptors(LARGER)) == 220

    print(main())
