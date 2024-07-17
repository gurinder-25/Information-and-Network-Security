def mono(s, operation):
    map1 = { 'a': 'y', 'b': 'n', 'c': 'l', 'd':'k', 'e': 'x', 'f': 'b', 'g': 's', 'h': 'h',
             'i': 'm', 'j': 'i', 'k': 'w', 'l': 'd',
             'm': 'p', 'n': 'j', 'o': 'm', 'p': 'o', 'q': 'q', 'r':
                 'v', 's':'f', 't': 'e', 'u': 'a', 'v': 'u', 'w': 'g', 'x':'t',
             'y':'z', 'z': 'c', '#': ' '}
    map2 = {val : key for key, val in map1.items()}
    res = []
    for i in s:
        if operation == 'en':
            (res.append(map1.get(i, i)))
        else:
            res.append(map2.get(i, i))

    return ''.join(res).replace('#', ' ')

s = "hello world"
s1 = mono(s, 'en')
print(s1)
print(mono(s1, 'de'))