from aoc import strlist
data = strlist(24)
u, v, n = len(data[0])-2, len(data)-2, 0
b = set([(i-1+k*1j-1j, 1j**">v<^".index(data[k][i])) for k in range(v+2) for i in range(u+2) if data[k][i] in ">v<^"])
m = set([i+k*1j for i in range(u) for k in range(v)] + [-1, u-1+v*1j])
for f,g in [(-1, u-1+v*1j), (u-1+v*1j, -1), (-1, u-1+v*1j)]:
    x = set([f])
    while g not in x:
        n += 1
        b = set([((p+q).real%u+(p+q).imag%v*1j, q) for p,q in b])
        x = (lambda t: set(i+k for i in x for k in [0, 1, -1, 1j, -1j] if k+i in m and k+i not in t))(set([p for p,q in b]))
    if f==-1: print(n)
