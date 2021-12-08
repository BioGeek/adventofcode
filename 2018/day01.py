# https://adventofcode.com/2018/day/1

import time
from collections import defaultdict
from itertools import accumulate, cycle


def main(part, lines=None):
    start = time.time()
    if lines is None:
        with open("2018/data/01.txt") as f:
            lines = f.read().splitlines()
    numbers = (int(line) for line in lines)
    if part == 1:
        return sum(numbers)
    else:
        numbers = cycle(numbers)
        seen = []
        frequency = 0
        for number in numbers:
            frequency += number
            if frequency in seen:
                print("elapsed time: {}s".format(time.time() - start))
                return frequency
            seen.append(frequency)
            print(
                "number: {}, frequency: {}, seen: {}".format(
                    number, frequency, len(seen)
                )
            )


def main2(part):
    # https://www.reddit.com/r/adventofcode/comments/a20646/2018_day_1_solutions/eauapmb/
    start = time.time()
    changes = [int(n) for n in open("2018/data/01.txt").read().splitlines()]
    if part == 1:
        return sum(changes)
    else:
        seen = set(0)
        result = next(f for f in accumulate(cycle(changes)) if f in seen or seen.add(f))
        print("elapsed time: {}s".format(time.time() - start))
        return result


def main3(part, data=None):
    if data is None:
        data = open("2018/data/01.txt").read().splitlines()
    changes = [int(n) for n in data]
    if part == 1:
        return sum(changes)
    else:
        sums = [0] + list(accumulate(changes))

        # check if the repetition occurs in the first iteration
        sum_set = set()
        for s in sums:
            if s in sum_set:
                return s
            sum_set.add(s)

        # find the final sum after performing one iteration
        final_sum = sums[-1]
        if final_sum == 0:
            return 0  # if the shift is 0, then the first repetition is 0
        print(final_sum)

        sums = sums[
            :-1
        ]  # Remove the last element as it belongs to iteration 2, not iteration 1.
        print(sums)

        # populate a dictionary of all the groups where the value is the list of frequencies in the group
        groups = defaultdict(list)
        for i, s in enumerate(sums):
            groups[s % final_sum].append(
                (i, s)
            )  # each value will be a tuple of the index and the frequency

        return groups


if __name__ == "__main__":
    print(main2(1))
    print(main(False, ["+1", "-2", "+3", "+1"]))
    print(main3(2, [1, 1, 10, -9]))
