xbar = float(input("Enter xbar: "))
ybar = float(input("Enter ybar: "))
absx = float(input("Enter absolute error in xbar: "))
absy = float(input("Enter absolute error in ybar: "))
quotient = xbar / ybar
qabs = abs((abs(absx/xbar) + abs(absy/ybar)) * quotient)
print(("Quotient of xbar and ybar: {}".format(quotient)))
print(("Absolute error in quotient: {}".format(qabs)))