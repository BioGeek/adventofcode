def total_distance(locations):
    rows = (map(int, loc.split()) for loc in locations.splitlines())
    columns = map(sorted, zip(*rows))
    diffs = (abs(a-b) for (a, b) in zip(*columns))
    return sum(diffs)

def similarity_score(locations):
    rows = (map(int, loc.split()) for loc in locations.splitlines())
    left_column, right_column = zip(*rows)
    return sum(number * right_column.count(number) for number in left_column)
        
def main(part: int = 1) -> int:
    with open("2024/data/day01.txt") as f:
        locations = f.read()
    if part ==1:
        return total_distance(locations)
    else:
        return similarity_score(locations)
    
if __name__ == '__main__':
    locations = """3   4
4   3
2   5
1   3
3   9
3   3"""

    assert total_distance(locations) == 11

    print(main())

    assert similarity_score(locations) == 31

    print(main(part=2))

