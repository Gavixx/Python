import numpy as np
matrix1 = np.array([[1,2,3], [3,4,5], [6,7,8]])
print(matrix1, "\n")
matrix2 = np.array([[5,10, 15], [20,25,30], [35,40, 45]])
print(matrix2, "\n")
a = matrix1.dot(matrix2)
print(a)