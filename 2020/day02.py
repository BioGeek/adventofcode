import re
from dataclasses import dataclass
from typing import Iterator, Tuple


@dataclass
class Policy:
    lower: int
    upper: int
    char: str


def is_valid_password(policy: Policy, password: str, part=1) -> bool:
    """Returns if a password is valid according to the policy."""
    if part == 1:
        return policy.lower <= password.count(policy.char) <= policy.upper
    else:
        return (
            sum(
                [
                    password[policy.lower - 1] == policy.char,
                    password[policy.upper - 1] == policy.char,
                ]
            )
            == 1
        )


def parse(data: str) -> Iterator[Tuple[Policy, str]]:
    """Parses the input data"""
    pattern = "(?P<lower>\d+)-(?P<upper>\d+) (?P<char>[a-z]): (?P<password>.*)"
    for match in re.finditer(pattern, data, re.MULTILINE):
        groupdict = match.groupdict()
        lower = int(groupdict["lower"])
        upper = int(groupdict["upper"])
        char = groupdict["char"]
        password = groupdict["password"]
        yield Policy(lower, upper, char), password


def main(part: int = 1):
    with open("data/day02.txt") as fh:
        data = fh.read()
    return sum(is_valid_password(policy, password, part) for policy, password in parse(data))


if __name__ == "__main__":
    assert is_valid_password(Policy(1, 3, "a"), "abcde")
    assert not is_valid_password(Policy(1, 3, "b"), "cdefg")
    assert is_valid_password(Policy(2, 9, "c"), "ccccccccc")

    print(main())

    assert is_valid_password(Policy(1, 3, "a"), "abcde", part=2)
    assert not is_valid_password(Policy(1, 3, "b"), "cdefg", part=2)
    assert not is_valid_password(Policy(2, 9, "c"), "ccccccccc", part=2)

    print(main(part=2))
