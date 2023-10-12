from aoc import strlist

data = strlist(15)

s = []
r = []
d = set()
for i in data:
    _, _, x, y, _, _, _, _, p, q = (i+"_").split(" ")
    x, y, p, q = map(lambda t: int(t[2:-1]), (x, y, p, q))
    s.append((x, y, abs(x-p)+abs(y-q)))
    d.add((p, q))

n = sum((i, 2000000) not in d and any(abs(x-i) + abs(y-2000000) <= t for (x, y, t) in s)
        for i in range(min(s[j][0]-s[j][2] for j in range(len(s))), max(s[j][0]+s[j][2] for j in range(len(s)))+1))

a, b = set(), set()
for x, y, t in s:
    a.update([y-x+t+1, y-x-t-1])
    b.update([y+x+t+1, y+x-t-1])

for i in a:
    for j in b:
        p=((j-i)//2, (j+i)//2)
        if all(0<=k<=4000000 for k in p) and all(abs(x-(j-i)//2) + abs(y-(j+i)//2) > t for x, y, t in s):
            print(n, 4000000*(j-i)//2 + (j+i)//2)
