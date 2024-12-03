def safe_count(reports, part=1):
    if part == 1:
        return sum(
            is_safe(list(map(int, report.split()))) for report in reports.splitlines()
        )
    else:
        safe_lines = 0
        for report in reports.splitlines():
            report = list(map(int, report.split()))
            if is_safe(report):
                safe_lines += 1
            else:
                # brute force
                safe_lines += any(
                    is_safe(report[:i] + report[i + 1 :]) for i in range(len(report))
                )
        return safe_lines


def is_safe(report):
    return (
        is_all_increasing(report) or is_all_decreasing(report)
    ) and is_gradually_chaging(report)


def is_all_increasing(report):
    return all(a < b for (a, b) in zip(report, report[1:]))


def is_all_decreasing(report):
    return all(a > b for (a, b) in zip(report, report[1:]))


def is_gradually_chaging(report):
    return all(1 <= abs(a - b) <= 3 for (a, b) in zip(report, report[1:]))


def main(part: int = 1) -> int:
    with open("2024/data/day02.txt") as f:
        reports = f.read()
    return safe_count(reports, part)


if __name__ == "__main__":
    reports = """7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9"""

    assert safe_count(reports) == 2

    print(main())

    assert safe_count(reports, part=2) == 4

    print(main(part=2))
