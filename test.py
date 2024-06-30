import numpy as np
arr = np.array([1,2,3,4,5])
print(arr)
print(arr.ndim)

# 5x5 size of the array and the data is 10
n1 = np.full((5,5),10)
print(n1)

# print in range (start from 0 to n-1)
n2 = np.arange(50,100)
print(n2)

# Join the array
n3 = np.array([7,8,9,10])
n4 = np.array([11,12,13,14])
#  it join the vertically
res1 = np.vstack((n3,n4))
print(res1)
# it join the horizontally
res2 = np.hstack((n3,n4))
print(res2)
# column stack
res3 = np.column_stack((n3,n4))
print(res3)

# concatenate the array(Note: The dimention should be same for both the array)
res4 = np.concatenate((n3,n4))
print(res4)
# union,intersection and difference will be same as the list
res5 = np.intersect1d(n3,n4)
print(res5)
res6 = np.union1d(n3,n4)
print(res6)
# find
find = np.where(n3 == 10)
print(find)

# Sort the array
arr = np.array([30,28,25,17,40])
print(np.sort(arr))

newArr = arr[arr>25]
print(newArr)