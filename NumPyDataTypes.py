# Agood practice is to set 'dtype' manually to improve performance and make program more mermory efficient

# intereger (int8, int16, int32, int64 )
# float     (float16, float32, float64   )
# boolean   ( bool_  )
# string    ( str_,  <U# )
# object    ( object_  )

import numpy as np

arr1 = np.array([2,4,6,8], dtype = np.int8)
print(arr1)

print(arr1.dtype)

print(f"array uses {arr1.nbytes}bytes")

arr2 = np.array([122,124,126,128], dtype = np.int16)
print(arr2)
print(arr2.dtype)

print(f"array uses {arr2.nbytes}bytes")

arr3 = np.array([2,4,6,8], dtype = np.float64)
print(arr3)

print(arr3.dtype)

print(f"array uses {arr3.nbytes}bytes")


arr4 = np.array([2,4,6,8], dtype = np.bool_)
print(arr4)

print(arr4.dtype)

print(f"array uses {arr4.nbytes}bytes")

arr5 = np.array(["Hello","Python"], dtype = np.str_)
print(arr5)

print(arr5.dtype)

print(f"array uses {arr5.nbytes}bytes")

arr6 = np.array([2,4.5,True,"Hello"], dtype = np.object_)
print(arr6)

print(arr6.dtype)

print(f"array uses {arr6.nbytes}bytes")


arr7 = np.array([2,4,6,8])

newArray7 = arr7.astype(np.float16)
print(newArray7)
print(newArray7.dtype)


print(f"array uses {newArray7.nbytes}bytes")


arr8 = np.array([2.1,4.4,6.3,8.2])

newArray8 = arr8.astype(np.int16)
print(newArray8)
print(newArray8.dtype)


print(f"array uses {newArray7.nbytes}bytes")


