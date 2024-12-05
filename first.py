# def check(str):
#     li = list(str)
#     print(li)
#     if(li==li[::-1]):
#         return True
#     return False    

# str = "raj"
# if(check(str)):
#     print("Palin")
# else:
#     print("NP")

# arr = [1,2,3,4]
# s = 0
# for i in arr:
#     s = s + i
# print(s)

# arr = [5,3,6,2,7,5]
# maxm = 0
# for i in arr:
#     if i >= maxm:
#         maxm = i
# print(maxm)

# arr = [100,10,5,25,35,14]
# n = 11
# m = 1

# for i in arr:
#     m = (m * i) % n

# print(m % n)

# def isMonotic(arr):
#     x, y = [], []
#     x.extend(arr)
#     y.extend(arr)
#     x.sort()
#     y.sort(reverse = True)
    
#     if(x == arr or y == arr):
#         return True
#     return False

# arr = [6,5,4,4]
# print(isMonotic(arr))

# arr = [1,2,3,4,5]
# print(arr)
# arr[0], arr[-1] = arr[-1], arr[0]
# arr[1], arr[-2] = arr[-2], arr[1]
# print(arr)

# arr = [1,2,3,4,5,6,7,8,9]
# s = 0
# e = len(arr)-1

# while(s <= e):
#     arr[s], arr[e] = arr[e], arr[s]
#     s = s+1
#     e = e-1

# print(arr)

# arr = [1,2,3,4,5,6,7,8,9]
# for i in arr:
#     arr1[i] = arr[]

# arr = [[1,2,3],[4,5,6],[7,8,9]]
# print(type(arr))
# brr = [[9,8,7],[6,5,4],[3,2,1]]
# res = [[0,0,0],[0,0,0],[0,0,0]]

# for i in range(len(arr)):
#     for j in range(len(arr[i])):
#         res[i][j] = arr[i][j]+brr[i][j]

# print(res)
    

# def isPalin(str):
#     str = str.upper()
#     print(str)
#     return str == str[::-1]

# str = "Racecar"
# if(isPalin(str)):
#     print("Palindrome")
# else:
#     print("Not Palindrome")

# a = int(input("Enter 1st no. "))
# b = int(input("Enter 2nd no. "))
# print("Sum: ", (a+b))


# Camel Case = myVariableName
# Pascal Case = MyVariableName
# Snake Case = my_variable_name


# arr = [1,2,3,4,5]
# for i in arr:
#     print(type(i))
#     a = str(i)
#     print(a,i)

# global x
# x = "Hello"
# def fun():
#     x = "World"
#     print("Python is " + x)
# fun()
# print(x)

# for i in "banana":
#     print(i, end=",")

b = "Hello, World!"
print(b[-5:-2])

# Variables

# Python Numbers -> Int, Float, Complex, Type Conversion, Random Number

# Strings 
# Slicing Strings -> From Start, to the end, -ve indexing
# Modify Strings -> upper(), lower(), strip(), replace("a","b"), split()

