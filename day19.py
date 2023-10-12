from aoc import strlist, tock
m, n = 0, 1
for i, (ww, xw, yw, yx, zw, zy) in enumerate(map(int, filter(lambda k: k.isnumeric(), j.split(" "))) for j in strlist(19)):
    dw = max(ww, xw, yw, zw)
    p = set([(1, 0, 0, 0, 0, 0, 0, 0, 0)])
    q = set()
    h, g = 0, 0
    c = 32 if i < 3 else 24
    while p:
        wb, xb, yb, zb, wr, xr, yr, zr, t = p.pop()
        h = max(h, zr)
        if t == 24: g = max(g, zr)
        if zr+sum(range(zb, zb+c-t)) < h or t == c: continue
        wr = min(wr, (c-t)*dw-(c-t-1)*wb)
        xr = min(xr, (c-t)*yx-(c-t-1)*xb)
        yr = min(yr, (c-t)*zy-(c-t-1)*yb)
        if (wb, xb, yb, zb, wr, xr, yr, zr, t) in q: continue
        q.add((wb, xb, yb, zb, wr, xr, yr, zr, t))
        if wr >= zw and yr >= zy:
            p.add((wb, xb, yb, zb+1, wb+wr-zw, xb+xr, yb+yr-zy, zb+zr, t+1))
            continue
        if wr >= yw and xr >= yx and yb < zy:
            p.add((wb, xb, yb+1, zb, wb+wr-yw, xb+xr-yx, yb+yr, zb+zr, t+1))
        if wr >= xw and xb < yx:
            p.add((wb, xb+1, yb, zb, wb+wr-xw, xb+xr, yb+yr, zb+zr, t+1))
        if wr >= ww and wb < dw:
            p.add((wb+1, xb, yb, zb, wb+wr-ww, xb+xr, yb+yr, zb+zr, t+1))
        p.add((wb, xb, yb, zb, wb+wr, xb+xr, yb+yr, zb+zr, t+1))
    m += (i+1)*g
    n *= h if i < 3 else 1
print(m, n)
