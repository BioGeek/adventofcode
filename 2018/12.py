def main(part=1, data=None):
    lines = data.splitlines()
    initial = lines[0].split(": ")[1]
    rules = dict(tuple(line.split(" => ")) for line in lines[2:])

    start = 0

    for _ in range(20):
        if not initial.startswith(".."):
            initial = ".." + initial
            start += 2
        initial += ".."

        first_pot = initial.find("#")
        new = initial[:first_pot]
        for i in range(first_pot, len(initial) - 2):
            part = initial[i - 2 : i + 3]
            # current = part[2]
            # print(part, current)
            if part in rules:
                new += rules[part]
            else:
                new += "."  # current
            # print(initial)
            # print(new)
            # print(part, part in rules)
            # print()
        print(_, start, new)
        initial = new


if __name__ == "__main__":
    data = """initial state: #..#.#..##......###...###

...## => #
..#.. => #
.#... => #
.#.#. => #
.#.## => #
.##.. => #
.#### => #
#.#.# => #
#.### => #
##.#. => #
##.## => #
###.. => #
###.# => #
####. => #"""
    print(main(data=data))
