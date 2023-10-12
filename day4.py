from aoc import strlist

data = strlist(4)
n, m = 0, 0
for i in data:
    a,b,c,d = map(int, i.replace("-", ",").split(","))
    n += set(range(a,b+1)) <= set(range(c,d+1)) or set(range(a,b+1)) >= set(range(c,d+1))
    m += bool(set(range(a,b+1)) & set(range(c,d+1)))
print(n,m)
