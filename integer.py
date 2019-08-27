while True:
    number = int(input("Integer: "))
    if (number >= 20 and number <= 200) and (number%2 ==0) or (number < 0) and (number%2 !=0):
        print(str(number) + " passes the test!")

    else:
        print(str(number) + " fails the test :(")
    if number == 0:
        print("Bye!")
        break
