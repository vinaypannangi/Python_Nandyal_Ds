import numpy as np
A=np.array([[2,3],[1,1]])
B=np.array([8,3])
solution=np.linalg.solve(A,B)
print("solution is")
print("x is",solution[0])
print("y is",solution[1])