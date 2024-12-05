from collections import defaultdict


def parse(protocol):
    top, bottom = protocol.split("\n\n")
    ordering_rules = defaultdict(set)
    for line in top.splitlines():
        key, value = map(int, line.split("|"))
        ordering_rules[key].add(value)
    updates = [list(map(int, line.split(","))) for line in bottom.splitlines()]
    return ordering_rules, updates


def in_right_order(update, ordering_rules):
    for i in range(len(update)):
        number, *rest = update[i:]
        if not set(rest).issubset(ordering_rules[number]):
            return False
    return True


def order(update, ordering_rules):
    print(update)
    for n in update:
        print(n, ordering_rules[n])
    return sorted(update, key=lambda n: len(ordering_rules[n]), reverse=True)


def middle_page_number(protocol, part=1):
    total = 0
    ordering_rules, updates = parse(protocol)
    for update in updates:
        is_in_right_order = in_right_order(update, ordering_rules)
        if is_in_right_order and part == 1:
            idx = len(update) // 2
            total += update[idx]
        if not is_in_right_order and part == 2:
            new_update = order(update, ordering_rules)
            idx = len(new_update) // 2
            total += new_update[idx]
    return total


def main(part: int = 1) -> int:
    with open("2024/data/day05.txt") as f:
        protocol = f.read()
    return middle_page_number(protocol, part)


if __name__ == "__main__":
    protocol = """47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47"""

    assert middle_page_number(protocol) == 143

    print(main())

    assert middle_page_number(protocol, part=2) == 123

    print(main(part=2))
