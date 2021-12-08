import re
from collections import defaultdict
from itertools import groupby


def main(part=1, data=None):  # noqa: C901
    if data is None:
        with open("2018/data/04.txt") as f:
            data = f.read()
    data = data.splitlines()
    dicts = []
    for line in data:
        m = re.match(
            r"\[1518-(?P<month>\d{2})-(?P<day>\d{2}) (?P<hour>\d{2}):(?P<mins>\d{2})\] (?P<line>.*)",
            line,
        )
        if m:
            dicts.append(m.groupdict())
    dicts = sorted(dicts, key=lambda d: (d["month"], d["day"], d["hour"], d["mins"]))
    sleeping = defaultdict(int)
    overlapping = {}
    for key, group in groupby(dicts, key=lambda d: "Guard" in d["line"]):
        if key:
            g = re.match(r"Guard #(\d+) begins shift", list(group)[0]["line"])
            guard = g.group(1)
            # print(guard)
        else:
            for asleep, wakesup in zip(group, group):
                assert "asleep" in asleep["line"]
                assert "wakes up" in wakesup["line"]
                mins_sleeping = int(wakesup["mins"]) - int(asleep["mins"])
                hours_sleeping = int(wakesup["hour"]) - int(asleep["hour"])
                # print('mins', mins_sleeping)
                # print('hours', hours_sleeping)
                sleeping[guard] += (hours_sleeping) * 60 + mins_sleeping
                # print(sleeping)

                if guard in overlapping:
                    minutes = overlapping[guard]
                else:
                    minutes = defaultdict(int)
                for minute in range(int(asleep["mins"]), int(wakesup["mins"])):
                    minutes[minute] += 1
                overlapping[guard] = minutes
                # print(overlapping)

    if part == 1:
        guard_most_asleep = max(sleeping, key=lambda k: sleeping[k])
        most_overlapping_minute = max(
            overlapping[guard_most_asleep],
            key=lambda k: overlapping[guard_most_asleep][k],
        )
        return int(guard_most_asleep) * most_overlapping_minute
    else:

        minute_most_frequently_asleep = 0
        guard_most_frequently_asleep = None
        times_appeared = 0

        for guard in overlapping:
            minutes = overlapping[guard]

            m = max(minutes.values())
            if m > times_appeared:
                times_appeared = m
                minute_most_frequently_asleep = max(minutes, key=lambda k: minutes[k])
                guard_most_frequently_asleep = guard
                # print('minute_most_frequently_asleep', minute_most_frequently_asleep, 'times_appeared', times_appeared, 'guard', guard)

        return minute_most_frequently_asleep * int(guard_most_frequently_asleep)


if __name__ == "__main__":
    data = """
[1518-11-01 00:00] Guard #10 begins shift
[1518-11-01 00:05] falls asleep
[1518-11-01 00:25] wakes up
[1518-11-01 00:30] falls asleep
[1518-11-01 00:55] wakes up
[1518-11-01 23:58] Guard #99 begins shift
[1518-11-02 00:40] falls asleep
[1518-11-02 00:50] wakes up
[1518-11-03 00:05] Guard #10 begins shift
[1518-11-03 00:24] falls asleep
[1518-11-03 00:29] wakes up
[1518-11-04 00:02] Guard #99 begins shift
[1518-11-04 00:36] falls asleep
[1518-11-04 00:46] wakes up
[1518-11-05 00:03] Guard #99 begins shift
[1518-11-05 00:45] falls asleep
[1518-11-05 00:55] wakes up
"""
    assert main(data=data) == 240
    print(main())

    assert main(part=2, data=data) == 4455
    print(main(part=2))
