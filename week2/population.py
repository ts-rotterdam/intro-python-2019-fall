population = {"Amsterdam": [821752, 23456], "London": [
    8136000, 234567], "Madrid": [3174000, 2134567]}

for i in population:
    print(i)

for k in population.keys():
    print(k)

for v in population.values():
    print(v)

for k, v in population.items():
    print(f"{k} has {v[0]} males and {v[1]} females")
