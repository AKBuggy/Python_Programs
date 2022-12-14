# How to define array without numpy package

# from array import *
#
# arr = array('i', [1, 2, 3, 4, 5])
# print(arr)


# How to define array using numpy

from numpy import *

# arr = array([1.5, 2.4, 3, 4, 5])
# or
# arr = array([1, 2, 3, 4, 5], int)

# print(arr)
# print(arr.dtype)
#
# for i in range(len(arr)):
#     print(arr[i])

print("---------------------------------------------------------------------")

arr = linspace(0, 15, 16)
print(arr)

arr = arange(0, 15, 2)
print(arr)

arr = logspace(1, 40, 5)
print(arr)
print("%.2f" % arr[0])

# if we want to create array with value zero

arr = zeros(5)
print(arr)

# if we want to create array with value one

arr = ones(5)
print(arr)

print("---------------------------------------------------------------------")

arr1 = array([1, 2, 3, 4, 5])
arr2 = array([5, 6, 7, 8, 9])

# arr1 += 5
# print(arr1)

arr3 = arr1 + arr2
print(arr3)

print("---------------------------------------------------------------------")

arr3 = array([1, 4, 2, 5, 0])
print(sin(arr))  # cos, log, sqrt, sum, min, max, sort, unique, concatenate
print(concatenate([arr1, arr2]))










