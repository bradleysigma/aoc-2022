from aoc import strlist, vec as v

print(sum(map({"A X": v([4, 3]), "B X": v([1, 1]), "C X": v([7, 2]), "A Y": v([8, 4]), "B Y": v([5, 5]), "C Y": v([2, 6]), "A Z": v([3, 8]), "B Z": v([9, 9]), "C Z": v([6, 7])}.get, strlist(2))))
