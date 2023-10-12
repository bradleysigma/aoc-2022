y, t = sum(("=-012".find(c)-2)*5**n for i in open("input25.txt") for n, c in enumerate(i[-2::-1])), ""
while y or print(t): y, t = (y+2)//5, "012=-"[y%5]+t
