n = int(input("Enter the Year: "))


#Check for Leap year Which is Occurring every Fourth year
if (n % 4 == 0):
    #Check for Century year for century years the year should be divisible by both 100 and 400
    if (n % 100 == 0):
        if (n % 400 == 0):
            print("The Year entered is Leap year ")
        else:
            print("The Year entered is not Leap year")
    #If The given year is not a century year and is divisible by 4 Then it is a Leap year
    else:
        print("The Year entered is Leap year ")
else:
    print("The Year entered is not a Leap year")

        
