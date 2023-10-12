from aoc import strlist
data = strlist(3)
print(sum(" abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ".index(min(set(i[:len(i)//2]) & set(i[len(i)//2:]))) for i in data),
      sum(" abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ".index(min(set.intersection(*map(set, data[n:n+3])))) for n in range(0, len(data), 3)))
