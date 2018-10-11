#this is the txt file for learning linear algebra
# 2a + 3b =13, 10a + b = 13

# a : apple //  b: banana

import numpy as np
A = np.array ([[3,-9],[2,4]])
print(A)
B = np.array([-42,2])

Z = np.linalg.solve(A,B)

print(Z)
