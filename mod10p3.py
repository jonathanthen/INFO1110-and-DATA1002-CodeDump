def filter_outliers(num, lower=0, upper=100):

  if num > lower and num < upper:
    return num
  elif num > lower and num >= upper:
    return upper
  elif num <= lower and num < upper:
    return lower
  else:
    return num