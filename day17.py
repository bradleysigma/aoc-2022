from aoc import read

data = read(17)
s = set((u,0) for u in range(7))
r = [set([(0,0), (1,0), (2,0), (3,0)]),
     set([(1,0), (0,1), (1,1), (2,1), (1,2)]),
     set([(0,0), (1,0), (2,0), (2,1), (2,2)]),
     set([(0,0), (0,1), (0,2), (0,3)]),
     set([(0,0), (0,1), (1,0), (1,1)])]

m = 0
h = [None]
n = 0
t = [0]
while True:
    p = set((u+2, v+4+max(j[1] for j in s)) for u,v in r[n%len(r)])
    while True:
        if all(0<=u+ord(data[m])-61<7 and (u+ord(data[m])-61,v) not in s for u, v in p):
            p = set((u+ord(data[m])-61, v) for u, v in p)
        m = (m+1)%len(data)
        if all((u,v-1) not in s for u, v in p):
            p = set((u, v-1) for u,v in p)
        else:
            s.update(p)
            break
    n += 1
    t.append(max(j[1] for j in s))
    w = (n%len(r), m)
    if n > 2022 and w in h:
        c = n - h.index(w)
        f = (1000000000000-n)//c+1
        print(t[2022], t[999999999999-n-f*c] + f*(t[-1]-t[n-c]))
        break
    h.append(w)
