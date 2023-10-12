from aoc import strlist

data = strlist(10)
x = 1
c = 0
y = 0
s = ""

for i in data:
    for j in range(2 if i[:4] == "addx" else 1):
        s += "#" if abs(x-c%40)<=1 else " "
        c += 1
        y += c*x if c%40 == 20 else 0
    x += int((i+" 0").split(" ")[1])

print(y)
for i in range(0,len(s),40):
    print(s[i:i+40])
