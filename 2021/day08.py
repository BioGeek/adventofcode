from collections import Counter, defaultdict
from typing import Dict, List

digit_to_segments: Dict[int, str] = {
    0: "abcefg",
    1: "cf",
    2: "acdeg",
    3: "acdfg",
    4: "bcdf",
    5: "abdfg",
    6: "abdefg",
    7: "acf",
    8: "abcdefg",
    9: "abcdfg",
}

segments_length_to_digits: Dict[int, List[int]] = defaultdict(list)
for digit, segments in digit_to_segments.items():
    segments_length_to_digits[len(segments)].append(digit)

segment_used_in_digits: Dict[str, List[int]] = defaultdict(list)
for digit, segments in digit_to_segments.items():
    for segment in segments:
        segment_used_in_digits[segment].append(digit)

score_to_digit: Dict[int, int] = {
    sum(len(segment_used_in_digits[segment]) for segment in segments): digit
    for digit, segments in digit_to_segments.items()
}


def parse(entries: str) -> List[List[List[str]]]:
    return [
        [part.split() for part in entry.split(" | ")] for entry in entries.splitlines()
    ]


def solve(entries: str, part: int = 1) -> int:
    # Part 2 uses the method described here:
    # https://www.reddit.com/r/adventofcode/comments/rc5s3z/2021_day_8_part_2_a_simple_fast_and_deterministic
    if part == 1:
        return sum(
            1
            for _, output_values in parse(entries)
            for val in output_values
            if len(segments_length_to_digits[len(val)]) == 1
        )
    else:
        result = []
        for signal_patterns, output_values in parse(entries):
            line = []
            scores = Counter("".join(signal_patterns))
            for segments in output_values:
                output_score = sum(scores[segment] for segment in segments)
                line.append(score_to_digit[output_score])
            result.append(int("".join(map(str, line))))
        return sum(result)


def main(part: int = 1) -> int:
    with open("2021/data/day08.txt") as f:
        entries = f.read()
    return solve(entries, part)


if __name__ == "__main__":
    assert all(val == "".join(sorted(val)) for val in digit_to_segments.values())

    entries = """be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe
edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc
fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg
fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb
aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea
fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb
dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe
bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef
egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb
gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce"""

    single_line = "acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf"
    assert parse(single_line) == [
        [
            [
                "acedgfb",
                "cdfbe",
                "gcdfa",
                "fbcad",
                "dab",
                "cefabd",
                "cdfgeb",
                "eafb",
                "cagedb",
                "ab",
            ],
            ["cdfeb", "fcadb", "cdfeb", "cdbaf"],
        ]
    ]

    assert solve(entries) == 26

    print(main())

    assert solve(single_line, part=2) == 5353
    assert solve(entries, part=2) == 61229

    print(main(part=2))
