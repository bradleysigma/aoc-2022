from aoc import strgroups
from math import prod

data = strgroups(11)

m, f, t, d, y, z = map(list, zip(*[(list(map(int, i[1].split(": ")[1].split(", "))),
                                    eval("lambda old: "+i[2].split("= ")[1]),
                                    int(i[3].split(" ")[-1]),
                                    (int(i[5].split(" ")[-1]), int(i[4].split(" ")[-1])),
                                    0,
                                    0) for i in data]))
n = [list(i) for i in m]
q = prod(t)

for k in range(20):
    for i in range(len(m)):
        y[i] += len(m[i])
        for j in map(lambda x: f[i](x)//3, m[i]):
            m[d[i][(j%t[i])==0]].append(j)
        m[i] = []

for k in range(10000):
    for i in range(len(n)):
        z[i] += len(n[i])
        for j in map(lambda x: f[i](x), n[i]):
            n[d[i][(j%t[i])==0]].append(j%q)
        n[i] = []

print(max(y)*sorted(y)[-2], max(z)*sorted(z)[-2])
