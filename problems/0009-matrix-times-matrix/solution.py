def matrixmul(a:list[list[int|float]],
              b:list[list[int|float]])-> list[list[int|float]]:
	
    if len(a[0]) != len(b):
        return -1

    return [[sum([a[i][k] * b[k][j] for k in range(len(a[0]))]) for j in range(len(b[0]))] for i in range(len(a))]

# A: i x k

# [
# [2 2 2] i
# [2 2 2]
# ]

# *

# B: k * j
# [
# [3 3]
# [3 3]
# [3 3]
# j
# ]

# i x j
# loop through each row in A
# for each row, loop through each column in B
# at each cell, compute dot product between row i and column j, iterate through w. k