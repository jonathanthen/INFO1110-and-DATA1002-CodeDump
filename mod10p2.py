def filter_outliers(num,lower,upper):
  if num > lower and num < upper:
    return num
  elif num > lower and num >= upper:
    return upper
  elif num <= lower and num < upper:
    return lower
  else:
    return num