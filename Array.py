from array import *
# vals = array('I',[5, 1, -6, 3])
# vals = array('u',['a', 'e', 'i', 'o', 'u'])

vals = array('i',[5, 1, -6, 3, 5])

new_arr = array(vals.typecode, (a*a for a in vals))

print(vals.buffer_info())
print(vals.typecode)
# vals.reverse()
print(vals[0])

# for i in range(len(vals)):
#     print(vals[i])

# for e in vals:
#     print(e)

# for e in new_arr:
#     print(e)



i = 0

while i < len(new_arr):
    print(new_arr[i])
    i += 1
    