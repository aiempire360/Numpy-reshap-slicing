# reshap()
import numpy as np

arr = np.array([1,2,3,4,5,6,7,8,9,10,11,12])

arr = arr.reshape(3,4)
print(arr.shape)
print(arr)


# slicing   array[start:end:stop]

arr1 = np.array([ [1,2,3,4],
                  [5,6,7,8],
                  [9,10,11,12],
                  [13,14,15,16]  ])

print(arr1[1])
print(arr1[-1])
print(arr1[0:2:3])
print(arr1.ndim)
print(arr1[:,3])
print(arr1[1,:])