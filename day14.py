from aoc import strlist
data = strlist(14)
s = set()

for i in data:
    r = [tuple(map(int, j.split(","))) for j in i.split(" -> ")]
    for j in range(1, len(r)):
        p, q = sorted(r[j-1:j+1])
        s.update((x,y) for x in range(p[0], q[0]+1) for y in range(p[1], q[1]+1))

y = max(g[1] for g in s)
n = len(s)
t = None

while (500, 0) not in s:
    i = 500
    for j in range(y+2):
        for d in filter(lambda c: (i+c, j+1) not in s, [0, -1, 1]):
            i += d
            break
        else:
            break
    else:
        t = t or len(s) - n
    s.add((i,j))
print(t, len(s) - n)
