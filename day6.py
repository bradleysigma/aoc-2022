from aoc import read
data = read(6)

print([min(i for i in range(j, len(data)) if len(set(data[i-j:i])) == j) for j in [4, 14]])
