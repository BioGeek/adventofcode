def is_invalid_id(product_id):
    """any ID which is made only of some sequence of digits repeated twice. So, 55 (5 twice),
    6464 (64 twice), and 123123 (123 twice) would all be invalid IDs."""
    if len(product_id) % 2 != 0:
        return False
    half = len(product_id) // 2
    return product_id[:half] == product_id[half:]


def is_more_invalid(product_id):
    """an ID is invalid if it is made only of some sequence of digits repeated at least twice. So,
    12341234 (1234 two times), 123123123 (123 three times), 1212121212 (12 five times), and
    1111111 (1 seven times) are all invalid IDs."""
    for i in range(2, len(product_id) + 1):
        split = len(product_id) // i
        if product_id[:split] * i == product_id:
            return True
    return False


def invalid_product_ids(product_range):
    start, end = product_range.split("-")
    return [
        product_id
        for product_id in range(int(start), int(end) + 1)
        if is_invalid_id(str(product_id))
    ]


def more_invalid_product_ids(product_range):
    start, end = product_range.split("-")
    return [
        product_id
        for product_id in range(int(start), int(end) + 1)
        if is_more_invalid(str(product_id))
    ]


def sum_invalid_product_ids(product_ids):
    return sum(
        product_id
        for product_range in product_ids.split(",")
        for product_id in invalid_product_ids(product_range)
    )


def sum_more_invalid_product_ids(product_ids):
    return sum(
        product_id
        for product_range in product_ids.split(",")
        for product_id in more_invalid_product_ids(product_range)
    )


def main(part: int = 1):
    with open("2025/data/day02.txt") as f:
        data = f.read()
    if part == 1:
        return sum_invalid_product_ids(data)
    else:
        return sum_more_invalid_product_ids(data)


if __name__ == "__main__":
    product_ids = """11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"""

    assert is_invalid_id("55")
    assert is_invalid_id("6464")
    assert is_invalid_id("123123")

    assert invalid_product_ids("11-22") == [11, 22]
    assert invalid_product_ids("95-115") == [99]
    assert invalid_product_ids("998-1012") == [1010]
    assert invalid_product_ids("1188511880-1188511890") == [1188511885]
    assert invalid_product_ids("222220-222224") == [222222]
    assert invalid_product_ids("1698522-1698528") == []
    assert invalid_product_ids("446443-446449") == [446446]
    assert invalid_product_ids("38593856-38593862") == [38593859]
    assert invalid_product_ids("565653-565659") == []
    assert invalid_product_ids("824824821-824824827") == []

    assert sum_invalid_product_ids(product_ids) == 1227775554

    print(main())

    assert is_more_invalid("12341234")
    assert is_more_invalid("123123123")
    assert is_more_invalid("1212121212")
    assert is_more_invalid("1111111")

    assert more_invalid_product_ids("11-22") == [11, 22]
    assert more_invalid_product_ids("95-115") == [99, 111]
    assert more_invalid_product_ids("998-1012") == [999, 1010]
    assert more_invalid_product_ids("1188511880-1188511890") == [1188511885]
    assert more_invalid_product_ids("222220-222224") == [222222]
    assert more_invalid_product_ids("1698522-1698528") == []
    assert more_invalid_product_ids("446443-446449") == [446446]
    assert more_invalid_product_ids("38593856-38593862") == [38593859]
    assert more_invalid_product_ids("565653-565659") == [565656]
    assert more_invalid_product_ids("824824821-824824827") == [824824824]
    assert more_invalid_product_ids("2121212118-2121212124") == [2121212121]

    print(main(part=2))
