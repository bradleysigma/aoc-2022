s = set(tuple(map(int, i.split(","))) for i in open("input18.txt"))
a = set([(i+u,j+v,k+w) for u in (-1,0,1) for v in (-1,0,1) for w in (-1,0,1) for i,j,k in s]) - s
p = set([min(a)])
while len(p) != len(p := p | set([(i+u,j+v,k+w) for i,j,k in p for u in (-1,0,1) for v in (-1,0,1) for w in (-1,0,1) if sum(map(abs,[u,v,w]))==1]) & a): pass
print(*(sum((i+u,j+v,k+w) not in s for u in (-1,0,1) for v in (-1,0,1) for w in (-1,0,1) for i,j,k in s if sum(map(abs,[u,v,w]))==1)-k for k in (0, sum((i+u,j+v,k+w) in s for u in (-1,0,1) for v in (-1,0,1) for w in (-1,0,1) for i,j,k in a-p if sum(map(abs, [u,v,w]))==1))))
