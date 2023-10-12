m, p = (lambda z: (z[:-2], z[-1]+"L0R"))(open("input22.txt").read().strip("\n").split("\n"))
p = [(int(p[max(k for k in range(i) if p[k-1] in "LR"):i]), (ord(p[i])-79)//3*1j) for i in (c for c in range(len(p)) if p[c] in "LR")]
w, x = 2*(m[0].index(".")+1+1j,)
m = {i+1+k*1j+1j: m[k][i] for k in range(len(m)) for i in range(len(m[k]))}
e, f = 1, 1
b = dict(sum(([((100+50j+i*1j, 1), (i+100+50j, -1j)), ((100+i+50j, 1j), (100+50j+i*1j, -1)), ((51+50j+i*1j, -1), (i+101j, 1j)),
               ((i+101j, -1j), (51+50j+i*1j, 1)), ((51+i*1j, -1), (1+151j-i*1j, 1)), ((1+100j+i*1j, -1), (51+51j-i*1j, 1)),
               ((50+i+1j, -1j), (1+150j+i*1j, 1)), ((1+150j+i*1j, -1), (50+i+1j, 1j)), ((150+i*1j, 1), (100+151j-i*1j, -1)),
               ((100+100j+i*1j, 1), (150+51j-i*1j, -1)), ((100+i+1j, -1j), (i+200j, -1j)), ((i+200j, 1j), (i+100+1j, 1j)),
               ((50+i+150j, 1j), (50+150j+i*1j, -1)), ((50+150j+i*1j, 1), (i+50+150j, -1j))] for i in range(1, 51)), start=[]))
for k, r in p:
    for i in range(k):
        w += e * {".": 1, "#": 0}.get(m.get(w+e), -max(j for j in range(150) if m.get(w-e*j, " ") != " "))
        y, g = b.get((x, f), (x+f, f))
        x, f = (y, g) if m[y] == "." else (x, f)
    e, f = e*r, f*r
print(int(4*w.real+1000*w.imag+[1,1j,-1,-1j].index(e)), int(4*x.real+1000*x.imag+[1,1j,-1,-1j].index(f)))
