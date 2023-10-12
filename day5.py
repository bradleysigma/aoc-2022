from aoc import strgroups
data, moves = strgroups(5)

p = [[] for j in filter(None, data[-1].split(" "))]
for i in data[:-1]:
    for n, j in enumerate(i[1::4]):
        if j != " ":
            p[n].append(j)
q = [list(i) for i in p]

for i in moves:
    _, n, _, x, _, y = i.split(" ")
    n, x, y = map(int, (n, x, y))
    p[y-1] = p[x-1][n-1::-1] + p[y-1]
    p[x-1] = p[x-1][n:]
    q[y-1] = q[x-1][:n] + q[y-1]
    q[x-1] = q[x-1][n:]

print("".join(i[0] for i in p), "".join(i[0] for i in q))
