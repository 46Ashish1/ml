import numpy as np 
import pandas as pd
matrix = np.array([-1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]).reshape(4,3)
print(matrix)
print("Size of the matrix")
print(matrix.size)
print("Size of the first row") 
print(matrix[0].size)
print("Size of the third column")
print(matrix[:,1].size)
df = pd.read_csv('text1.txt', sep="", header=None)
print(df)
a= np.array([[1, 2, 3], [1,2,3], [7, 8, 9]]) 
print("matrix a: ")
print(a)
np.savetxt('text2.txt',a, fmt="%.2f")
f = open('text2.txt') 
print(f.read())
