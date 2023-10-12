from aoc import intlist
from collections import deque
data = intlist(20)
for m, r in [(list(enumerate(data)), 1), (list(enumerate(i*811589153 for i in data)), 10)]:
    f = deque(m)
    for k in range(r):
        for n, i in m:
            f.rotate(-f.index((n, i)))
            f.popleft()
            f.rotate(-i)
            f.appendleft((n, i))
    f = deque([i for n, i in f])
    f.rotate(-f.index(0))
    print(sum(f[j] for j in [1000,2000,3000]))
