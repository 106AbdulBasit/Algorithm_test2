while True:
    num = input("Please enter a number ")
    try:
        val = int(num)
        print("Input is an integer number.")
        print("Input number is: ", val)
        break;
    except ValueError:
        print("enter the valid number")



res = list(map(int, str(val)))
print ("The list from number is " + str(res))
sumof = sum(res)
print("The sum of the list  is " , sumof)