def maximum(collection):
      if len(collection) == 0:
            return None
      else:
            i = 0
            maxi = -999999
            while i < len(collection):
                  if type(collection[i]) != int:
                        return False
                        break
                  else:
                        if collection[i] < 0:
                              if maxi < collection[i]:
                                    maxi = collection[i]
                        elif maxi < collection[i]:
                              maxi = collection[i]
                  i += 1
            return maxi