from aoc import strlist
data = strlist(12)

d = {(i,j): data[i][j] for i in range(len(data)) for j in range(len(data[i]))}
a = set((i,j) for (i,j) in d if d[i,j] == "a")
s = max(d, key=lambda k: d[k] == "S")
e = max(d, key=lambda k: d[k] == "E")
d[s], d[e] = "az"

p = set([e])
r = set()
t = 0
n = None
while p:
    t += 1
    q = set()
    for x, y in p:
        for i, j in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            if (x+i, y+j) not in r and ord(d.get((x+i, y+j), "?")) >= ord(d[x,y])-1:
                if (x+i, y+j) == s:
                    m = t
                elif n is None and (x+i, y+j) in a:
                    n = t
                q.add((x+i, y+j))
    r |= p
    p = q

print(m, n)
