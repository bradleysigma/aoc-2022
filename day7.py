from aoc import strlist
from collections import defaultdict

data = strlist(7)

d = defaultdict(list)
x = []
for i in data:
    if i == "$ cd ..":
        x.pop()
    elif i.startswith("$ cd"):
        x.append(i[5:])
    elif i.startswith("$ ls"):
        continue
    elif i.startswith("dir"):
        d[tuple(x)].append(tuple(x) + (i[4:],))
    else:
        d[tuple(x)].append(int(i.split(" ")[0]))

b = True
while b:
    b = False
    for i in d:
        for j in range(len(d[i])):
            if type(d[i][j]) != int and all(type(k) == int for k in d[d[i][j]]):
                b = True
                d[i][j] = sum(d[d[i][j]])
                

print(sum(sum(d[i]) for i in d if sum(d[i]) <= 100000),
      min(sum(d[i]) for i in d if sum(d[("/",)]) - 40000000 <= sum(d[i])))
