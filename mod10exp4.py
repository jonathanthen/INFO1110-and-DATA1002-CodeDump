def append_to_clone(new_item, items):
  items_copy = list(items)
  items_copy.append(new_item)
  return items_copy

n = [1, 2, 3]
new_n = append_to_clone(4, n)
print(n)
print(new_n)

def append(new_item, items):
  items.append(new_item)

n = [1, 2, 3]
append(4, n)
print(n)

def append_and_return(new_item, items):
  items.append(new_item)
  return items

numbers = [1, 2, 3]
numbers2 = append_and_return(4, numbers)

print(numbers)
print(numbers2)

def append_default(new_item, items=[]):
  items.append(new_item)
  return items

items1 = append_default(5)
print(items1)

items2 = append_default(10)
print(items2)

def append_default_fixed(new_item, items=None):
  if items is None:
    items = []
  items.append(new_item)
  return items

items1 = append_default_fixed(5)
print(items1)

items2 = append_default_fixed(10)
print(items2)