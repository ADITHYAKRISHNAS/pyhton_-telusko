from array import *

# arr = array('i',[])

# n = int(input("Enter the length of the array "))

# for  i in range(n):
#     x = int(input("Enter the next value "))
#     arr.append(x)
# print(arr)

# val = int(input("Enter the value for search"))
# k = 0

# for e  in arr:
#     if e == val:
#         print(k)
#         break


#     k += 1

# print(arr.index(val))



n = int(input("enter the length of the array"))
arr2 = array('i',[])
for i in range(n):
    x = int(input("Enter the next value"))
    arr2.append(x)
print(arr2)

val = int(input("Enter the value for search"))

k = 0
for e in arr2:
    if e == val:
        print(k)
        break
    k += 1

