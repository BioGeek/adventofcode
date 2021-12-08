def main(part=1, data=None):
    if data is None:
        with open("2018/data/05.txt") as f:
            data = f.read()
    return len(reaction(data))


"""
def reaction(polymer):
    # print('len(polymer1)', len(polymer))
    l = len(polymer)
    print('l', l)
    polymer2 = None
    for i in range(len(polymer)-1):
        a = polymer[i]
        b = polymer[i+1]
        # print('i', i,  a, b)
        if (a.lower() == b.lower()) and ((a.isupper() and b.islower()) or (a.islower() and b.isupper())):
            # print('match', a, b)
            polymer2 = polymer[:i] + polymer[i+2:]
            # print('len(polymer2)', len(polymer2))
            break
    if polymer2 is None:
        return polymer
    if not polymer2:
        return ''
    elif len(polymer2) < l:
        return reaction(polymer2)
    else:
        return polymer2
"""


def is_match(a, b):
    return (a.lower() == b.lower()) and (
        (a.isupper() and b.islower()) or (a.islower() and b.isupper())
    )


def reaction(polymer):
    # return re.findall(, polymer)
    pass


if __name__ == "__main__":
    # assert reaction('Aa') == ''
    # assert reaction('abBA') == ''
    # assert reaction('abAB') == 'abAB'
    # assert reaction('aabAAB') == 'aabAAB'
    # assert reaction('dabAcCaCBAcCcaDA') == 'dabCBAcaDA'
    # print(main())
    print(reaction("Aa"))
    print(reaction("abBA"))
    print(reaction("abAB"))
    print(reaction("aabAAB"))
    print(reaction("dabAcCaCBAcCcaDA"))
