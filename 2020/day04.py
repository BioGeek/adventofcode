import re
from typing import List


class Passport:
    def __init__(self, data: str, part: int = 1) -> None:
        # see https://github.com/python/mypy/issues/7558
        self.fields = dict(  # type: ignore
            pair.split(":") for line in data.splitlines() for pair in line.split()
        )
        self.part = part
        self.required = {
            "byr": self.check_birth_year,
            "iyr": self.check_issue_year,
            "eyr": self.check_expiration_year,
            "hgt": self.check_height,
            "hcl": self.check_hair_color,
            "ecl": self.check_eye_color,
            "pid": self.check_passport_id,
        }

    def check_birth_year(self, value: str) -> bool:
        return 1920 <= int(value) <= 2002

    def check_issue_year(self, value: str) -> bool:
        return 2010 <= int(value) <= 2020

    def check_expiration_year(self, value: str) -> bool:
        return 2020 <= int(value) <= 2030

    def check_height(self, value: str) -> bool:
        if value[-2:] == "cm":
            return 150 <= int(value[:-2]) <= 193
        elif value[-2:] == "in":
            return 59 <= int(value[:-2]) <= 76
        else:
            return False

    def check_hair_color(self, value: str) -> bool:
        return re.match("^#[0-9a-f]{6}$", value) is not None

    def check_eye_color(self, value: str) -> bool:
        return value in {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}

    def check_passport_id(self, value: str) -> bool:
        return re.match("^[0-9]{9}$", value) is not None

    def is_valid(self) -> bool:
        """those that have all required fields. Treat cid as optional"""
        valid = not (self.fields.keys() ^ self.required) - {"cid"}
        if self.part == 1:
            return valid
        else:
            return valid and all(
                self.required[k](v) for k, v in self.fields.items() if k != "cid"
            )


def make_passports(data: str, part: int = 1) -> List[Passport]:
    return [Passport(lines, part) for lines in data.split("\n\n")]


def main(part: int = 1) -> int:
    with open("2020/data/day04.txt") as fh:
        data = fh.read()
    return sum(passport.is_valid() for passport in make_passports(data, part))


if __name__ == "__main__":
    VALID_1 = """ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
byr:1937 iyr:2017 cid:147 hgt:183cm

hcl:#ae17e1 iyr:2013
eyr:2024
ecl:brn pid:760753108 byr:1931
hgt:179cm"""

    INVALID_1 = """iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
hcl:#cfa07d byr:1929

hcl:#cfa07d eyr:2025 pid:166559648
iyr:2011 ecl:brn hgt:59in"""

    for passport in make_passports(VALID_1):
        assert passport.is_valid()

    for passport in make_passports(INVALID_1):
        assert not passport.is_valid()

    print(main())

    VALID_2 = """pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980
hcl:#623a2f

eyr:2029 ecl:blu cid:129 byr:1989
iyr:2014 pid:896056539 hcl:#a97842 hgt:165cm

hcl:#888785
hgt:164cm byr:2001 iyr:2015 cid:88
pid:545766238 ecl:hzl
eyr:2022

iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719"""

    INVALID_2 = """eyr:1972 cid:100
hcl:#18171d ecl:amb hgt:170 pid:186cm iyr:2018 byr:1926

iyr:2019
hcl:#602927 eyr:1967 hgt:170cm
ecl:grn pid:012533040 byr:1946

hcl:dab227 iyr:2012
ecl:brn hgt:182cm pid:021572410 eyr:2020 byr:1992 cid:277

hgt:59cm ecl:zzz
eyr:2038 hcl:74454a iyr:2023
pid:3556412378 byr:2007"""

    for passport in make_passports(VALID_2, part=2):
        assert passport.is_valid()

    for passport in make_passports(INVALID_2, part=2):
        assert not passport.is_valid()

    print(main(part=2))
