from aoc import strlist, vec
from math import prod

data = strlist(9)
r = [vec([0,0]) for k in range(10)]
s, t = set([r[1]]), set([r[9]])
for i in data:
    d, n = i.split(" ")
    for j in range(int(n)):
        r[0] += {"U": vec([1,0]), "D": vec([-1,0]), "R": vec([0,1]), "L": vec([0,-1])}[d]
        for k in range(1,10):
            if max(abs(r[k-1]-r[k])) > 1:
                r[k] += (r[k-1]-r[k]).sign()
        s.add(r[1])
        t.add(r[9])
print(len(s), len(t))
