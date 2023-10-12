from aoc import strlist, vec
import sympy
data = list(map(lambda x: x.split(": "), strlist(21)))
d = {}
f = {"+": lambda x, y: x+y, "-": lambda x, y: x-y, "*": lambda x, y: x*y, "/": lambda x, y: x/y}
while data:
    i, j = data.pop(0)
    if j.isnumeric():
        d[i] = vec([int(j), sympy.Symbol("x") if i == "humn" else int(j)])
    else:
        u, r, v = j.split(" ")
        if u in d and v in d:
            d[i] = f[r](d[u], d[v])
            if i == "root":
                d[i] = vec([d[i][0], d[u][1] - d[v][1]])
        else:
            data.append((i,j))
print(*map(round, [d["root"][0], sympy.solve(d["root"][1])[0]]))
