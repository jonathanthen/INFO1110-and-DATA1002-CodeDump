def append_unique(new_item, items=None):
  
  if items is None:
    items = []
    
  if new_item not in items:
    items.append(new_item)
    return items
  
  else:
    return items
