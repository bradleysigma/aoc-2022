from aoc import intgrid
from math import prod

data = intgrid(8)
print(sum(any([all(data[i][k] < data[i][j] for k in range(j)),
               all(data[i][k] < data[i][j] for k in range(j+1, len(data[i]))),
               all(data[k][j] < data[i][j] for k in range(i)),
               all(data[k][j] < data[i][j] for k in range(i+1, len(data)))]) for i in range(len(data)) for j in range(len(data[0]))),
      max(prod([max((k-j for k in range(j, len(data[i])) if all(t < data[i][j] for t in data[i][j+1:k]))),
                max((j-k for k in range(j+1) if all(t < data[i][j] for t in data[i][k+1:j]))),
                max((k-i for k in range(i, len(data)) if all(t[j] < data[i][j] for t in data[i+1:k]))),
                max((i-k for k in range(i+1) if all(t[j] < data[i][j] for t in data[k+1:i])))]) for i in range(len(data)) for j in range(len(data[0]))))
