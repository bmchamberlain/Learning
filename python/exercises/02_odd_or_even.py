#prompt for a number, prompt for a second number if the first is even, advise if first number is evenly divisible by the second number, if the number is a multiple of 4 advise that it is, otherwise advise that the number is odd or even


num = int(input("Enter a number: "))
if num % 2 == 0:
    check = int(input("Enter a number: "))
    if num % check == 0:
        print (str(num) + " is evenly divisible by " + str(check))
    elif num % 4 == 0:
        print (str(num) + " is a multiple of 4")
    else:
        print (str(num) + " is an even number and is not evenly divisible by " + str(check))
else:
    print (str(num) + " is an odd number")
