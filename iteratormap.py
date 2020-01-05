def add_one(numbers):
    results = []
    for num in numbers:
        results.append(num + 1)

    return results

nums = [0, 1, 2, 3, 4]
nums2 = add_one(nums)
print(nums2)

def convert_strings(objects):
    results = []
    for obj in objects:
        results.append(str(obj))

    return results

nums = [0, 1, 2, 3, 4]
strings = convert_strings(nums)
print(strings)

def add_on(n):
    return n + 1

nums = [0, 1, 2, 3, 4]
nums1 = list(map(add_on, nums))
print(nums1)

def convert_string(obj):
    return str(obj)

nums = [0, 1, 2, 3, 4]
strings = list(map(convert_string, nums))
print(strings)