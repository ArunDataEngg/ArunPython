import numpy as np
'''
CURVE_CENTER=80
grades=np.array([72,35,64,88,51,90,74,12])
average=grades.mean()
print(average)

change=CURVE_CENTER-average
print(change)
def curves(grades):
    #average=grades.mean()
    new_grades=grades+change #vectorization
    return np.clip(new_grades,grades,100)
print(curves(grades))

temperature=np.array([29.3,42.1,18.8,16.1,38.0,12.5,12.6,49.9,38.6,31.3,9.2,22.2]).reshape(2,2,3)
print(temperature.shape)
print(temperature)
print("*"*60)
print(np.swapaxes(temperature,1,2))



batting_averages=np.array([[50,30,70,10],[20,60,90,70],[100,90,100,80],[40,30,20,0]])

print("size of an array: ",batting_averages.shape)
print("Maximum Average: ",batting_averages.max())
print("Maximum Average Column: ",batting_averages.max(axis=0))
print("Maximum Average Row: ",batting_averages.max(axis=1))

numbers=np.linspace(5,51,24,dtype=int).reshape(4,6)
print("numbers:",numbers)


nums=np.arange(32).reshape(4,1,8)
print("nums:",nums)

nums2=np.arange(48).reshape(1,6,8)
print("nums2:",nums2)

print("*"*60)
print("nums+nums2:", nums+nums2)


arr1=np.arange(10,100,5,dtype=int).reshape(3,6)

print(arr1)
print("*"*60)
arr2=np.arange(10,100,5,dtype=int).reshape(3,6)
print(arr2)
sum=arr1+arr2
print("sum of arrays: ",sum)
'''

square = np.array([
    [16,3,2,13],
    [5,10,11,8],
    [9,6,7,12],
    [4,15,14,1]
])
    
print(square[:2,:2])
print(square[2:,2:])

#assert square[:,i].sum()==34
#assert square[:]

numbers=np.linspace(5,50,24,dtype="int").reshape(4,-1)
print(numbers)
print("-"*60)
mask=numbers%5==0
print("all the values divisible by 5", numbers[mask])#converting a resultant array 
print("all the values divisible by 8", numbers[numbers%8==0])


#transpose:
print(numbers.T)
print("Horizontal sorting", np.sort(numbers,axis=0))

print("vertical sorting", np.sort(numbers,axis=1))


a=np.array([[4,8],[6,1]])
b=np.array([[3,5],[7,2]])

print(np.concatenate((a,b)))
print(np.concatenate((b,a),axis=None))#merging arrays into two array and converting to single dimension
print(np.hstack((a,b)))#horizontal merging of 2 or more arrays 
print(np.vstack((a,b)))#vertical merging of two or more arrays

stock_prices=np.random.random((30,10))
print(stock_prices)


