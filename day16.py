from aoc import strlist

data = strlist(16)
f = {}
d = {}
z = {}
for j, i in enumerate(data):
    v = i.split(" ")[1]
    f[v] = int(i.split("=")[1].split(";")[0])
    d[v] = i.split("valves ")[1].split(", ") if "valves " in i else [i.split("valve ")[1]]
    z[v] = j if f[v] else None

b = {}
u = [("AA", frozenset([None]), 0)]
for t in range(30-1, -1, -1):
    m = max(b.values(), default=0) - max(f.values())*t
    v = []
    for p, r, g in u:
        if z[p] not in r and g+f[p]*t > max(m, b.get((p, r), m)):
            b[p, r] = g+f[p]*t
            v.append((p, r.union([z[p]]), g+f[p]*t))
        for i in filter(lambda x: g > max(m, b.get((x, r), m)), d[p]):
            b[p, r] = g
            v.append((i, r, g))
    u = v

c = {}
u = [("AA", "AA", frozenset([None]), 0)]
for t in range(26-1, -1, -1):
    m = max(c.values(), default=0) - max(f.values()) * t
    v = []
    for p, q, r, g in u:
        if z[p] not in r and z[q] not in r and p != q and g+(f[p]+f[q])*t > max(m, c.get((p, q, r.union([z[p], z[q]])), m)):
            c[p, q, r.union([z[p], z[q]])] = g+(f[p]+f[q])*t
            v.append((p, q, r.union([z[p], z[q]]), g+(f[p]+f[q])*t))
        for i in filter(lambda x: z[q] not in r and g + f[q]*t > max(m, c.get((x, q, r.union([z[q]])), m)), d[p]):
            c[i, q, r.union([z[q]])] = g+f[q]*t
            v.append((i, q, r.union([z[q]]), g+f[q]*t))
        for j in filter(lambda y: z[p] not in r and g+f[p]*t > max(m, c.get((p, y, r.union([z[p]])), m)), d[q]):
            c[p, j, r.union([z[p]])] =  g+f[p]*t
            v.append((p, j, r.union([z[p]]), g + f[p]*t))
        for i in d[p]:
            for j in filter(lambda y: g > max(m, c.get((i, y, r), m)), d[q]):
                c[i, j, r] = g
                v.append((i, j, r, g))
    u = v

print(max(b.values()), max(c.values()))
