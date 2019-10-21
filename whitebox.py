def max(nums):
"""Returns the `index` of the largest number in a list. 
If two or more indices share the same largest value,
we return the first one we find. If nums is not a list, 
or if nums contains no values, return -1."""
maximum = 0
i = 0
while i < len(nums)-1:
    if nums[i] >= maximum:
        maximum = nums[i]
    i += 1
return maximum

Input | Expected Output | Justification
[0,1,1] | 1 | Simple, Positive Case
[0,2,1] | 1 | Simple, Positive
(0,1,1) | -1 | Simple, Negative Case
# Not List
[True, True, 2, 2] | 2 | Simple, Positive Case
[1,1,1] | -1 | Multiple maxes
1234 | -1 | Not a list
"1234" | -1 | Not a list
[0,0,10] | 2 | Last element of the list
[-3,-2,-5] | 1 | Test for negative values