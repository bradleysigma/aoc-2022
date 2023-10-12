p, n, b = (lambda f: set(u+v*1j for v in range(len(f)) for u in range(len(f[v])) if f[v][u] == "#"))(open("input23.txt").readlines()), 0, 1
while (p := set().union(*([k] if len(g) == 1 else g for k, g in q.items())) if n else p) and b and (n := n+1) or print(n):
    q, b = {}, n == 11 and print(round(max((i-k).real+1 for i in p for k in p) * max((i-k).imag+1 for i in p for k in p) - len(p)))
    for i in p:
        t = min((k for k in range(n-1, n+3) if all(i+[-1j, 1j, -1, 1][k%4]*r not in p for r in [1-1j, 1, 1+1j])), default=None)
        t, b = (None, b) if all(i+k not in p and i+k+k*1j not in p for k in [-1j, 1j, -1, 1]) else (t, True)
        q[i+(0 if t is None else [-1j, 1j, -1, 1][t%4])] = q.get(i+(0 if t is None else [-1j, 1j, -1, 1][t%4]), set()) | set([i])

