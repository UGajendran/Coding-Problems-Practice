n = int(input("Enter the number: "))
temp = n
sum = 0
#Iterate Loop until n becomes zero
while (n > 0):
    #Calculate last digit
    rem = n % 10
    #Perform Sum of the cubes one by one
    sum += rem**3
    #Decrease n by each digit until it becomes zero 
    n = n // 10

#Check if Sum of Cubes is equal to the Input n         
if(sum == temp):
    print("True")
else:
    print("False")


