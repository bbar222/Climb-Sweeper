import numpy as np
field = np.random.randint(0,2,(8,8))
field[1,2] = 9
print(field[1,2])



for r in field:
    for c in r:
        print(c,end = "\t")
    print()