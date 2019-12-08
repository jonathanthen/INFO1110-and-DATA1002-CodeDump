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
            return num - (count * divisor)
            

print(modulus(16,3)) #1
print(modulus(-2,3)) #1
print(modulus(-16,7)) #5
#print(modulus(True,1))