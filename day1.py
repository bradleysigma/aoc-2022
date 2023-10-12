from aoc import strgroups

a = [sum(map(int, i)) for i in strgroups(1)]
print(max(a), sum(sorted(a)[-3:]))
