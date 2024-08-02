import numpy as np
digits=np.array([[1,2,3],
                 [4,5,6],
                 [7,8,9]])

print(digits)


print(digits.shape)#size of array
row_vector=digits[:,np.newaxis]
print(row_vector)
col_vector=digits[np.newaxis:]
print(col_vector)