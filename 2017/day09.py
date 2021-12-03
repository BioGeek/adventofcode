import re

# characters, number of groups, score

valids = [
    {"c": "{}", "g": 1, "s": 1},
    {"c": "{{{}}}", "g": 3, "s": 6},
    {"c": "{{},{}},", "g": 3, "s": 5},
    {"c": "{{{},{},{{}}}}", "g": 6, "s": 16},
    {"c": "{<{},{},{{}}>}", "g": 1, "s": 1},
    {"c": "{<a>,<a>,<a>,<a>}", "g": 1, "s": 1},
    {"c": "{{<a>},{<a>},{<a>},{<a>}}", "g": 5, "s": 9},
    {"c": "{{<!>},{<!>},{<!>},{<a>}}", "g": 2, "s": None},
]


for valid in valids:
    chars = valid["c"]
    groups = valid["g"]
    score = valid["s"]

    print("chars: ", chars)
    groups = []
    garbage = ""
    new_group = ""
    for c in chars:
        if c == "{":
            new_group = "{"
        elif c == "}":
            if new_group:
                new_group += "}"
                groups.append(new_group)
                new_group = ""
        else:
            garbage += c

    print("groups: ", groups)
    print("garbage: ", garbage)
    print("\n")


def lex(characters, token_exprs):
    """https://www.jayconrod.com/posts/37/a-simple-interpreter-from-scratch-in-python-part-1"""
    pos = 0
    tokens = []
    while pos < len(characters):
        match = None
        for token_expr in token_exprs:
            pattern, tag = token_expr
            regex = re.compile(pattern)
            match = regex.match(characters, pos)
            if match:
                text = match.group(0)
                if tag:
                    token = (text, tag)
                    tokens.append(token)
                break
        if not match:
            tokens.append((characters[pos], "Illegal character"))
        else:
            pos = match.end(0)
    return tokens


def lexer(characters):
    pass  # return lex(characters, _)


def groups(characters):
    pass


def score(characters):
    pass
