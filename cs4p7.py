def contains(item, collection):
    if type(collection) == int:
        return None
    else:
        if type(item) != str and (type(collection) != list or type(collection) != tuple):
            return None
        else:
            i = 0
            while i < len(collection):
                if item != collection[i]:
                    i += 1
                else:
                    return True