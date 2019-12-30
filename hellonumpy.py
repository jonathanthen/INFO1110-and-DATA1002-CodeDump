import numpy as np # import the `numpy` module, and give it the name `np`

ls_a = [100, 150, 200, 250]
print(type(ls_a))

nums = np.array(ls_a, dtype=np.int32) 
print(type(nums))
print(nums)

# ^ more efficient ways of creating this: 
nums2 = np.arange(100, 251, 50, dtype=np.int32) 

print(nums2)

nums3 = np.linspace(100, 250, 4, dtype=np.int32)