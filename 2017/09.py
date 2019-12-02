# characters, number of groups, score
valids = [
    {'c': '{}',             'g': 1, 's': 1},
    {'c': '{{{}}}',         'g': 3, 's': 6},
    {'c': '{{},{}},',       'g': 3, 's': 5},
    {'c': '{{{},{},{{}}}}', 'g': 6, 's': 16},
    {'c': '{<{},{},{{}}>}', 'g': 1, 's': 1},
    {'c': '{<a>,<a>,<a>,<a>}', 'g': 1, 's': 1},
    {'c': '{{<a>},{<a>},{<a>},{<a>}}', 'g': 5, 's': 9},
    {'c': '{{<!>},{<!>},{<!>},{<a>}}', 'g': 2, 's': None},
    
    
]

for valid in valids:
    chars = valid['c']
    groups = valid['g']
    score = valid['s']
    
    print('chars: ', chars)
    groups = []
    garbage = ''
    new_group = ''
    for c in chars:
        if c == '{':
            new_group = '{'
        elif c == '}':
            if new_group:
                new_group += '}'
                groups.append(new_group)
                new_group = ''
        else:
            garbage += c
            
    print('groups: ', groups)
    print('garbage: ', garbage)
    print('\n')
        
        