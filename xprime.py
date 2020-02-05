def modulus(num,divisor):
    if type(num) != int or type(divisor) != int:
        raise TypeError("Input(s) are not integers.")
    else:
        # Handle divisor equals to 0 case 
        if (divisor == 0): 
            return False
    
        n = num

        # Handle negative values 
        if n < 0:
            count = 0
            while n < 0:
                n += divisor
                count += 1
            return n
        else:
            count = -1
            while n > 0:
                n -= divisor
                count += 1
            if n == 0:
                return 0
            else:
                return num - (count * divisor)
            

import sys
try:
    number = int(sys.argv[1])
except ValueError:
    print("Invalid input")

if number > 1:
    i = 2
    if number == 2:
        print("Prime")
    else:
        while i < number:
            if number == 3:
                print("Prime")
                break
            elif modulus(number,i) == 0:
                print("Not Prime")
                break
            else:
                i += 1
                if i == number-1 and modulus(number,i+1) == 0:
                    print("Prime")

else:
    print("Not Prime")
