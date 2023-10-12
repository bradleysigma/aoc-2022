from aoc import strgroups, strlist
from functools import cmp_to_key
from math import prod

def comp(x, y):
    if type(x) == int and type(y) == int:
        return x - y
    if type(x) != type(y):
        return comp(x if type(x) == list else [x],
                    y if type(y) == list else [y])
    if len(x) * len(y) == 0:
        return len(x) - len(y)
    return (x[0] != y[0] and comp(x[0], y[0])) or comp(x[1:], y[1:])

data = [eval(i) for i in strlist(13) if i != ""] + [[[2]], [[6]], 0]
print(sum(i//2 for i in range(2, len(data)-3, 2) if comp(*data[i-2:i]) < 0),
      prod(n for n,i in enumerate(sorted(data, key=cmp_to_key(comp))) if i in [[[2]], [[6]]]))
