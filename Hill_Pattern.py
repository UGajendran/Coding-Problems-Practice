#Total levels in the hill(input1)
#The weight of the head level(input2)
#The weight increments each level(input3)
#To find Total weight

def Hill_pattern(input1, input2, input3):
    sumn = 0
    for i in range(1, input1 + 1):
        for j in range(1, i + 1):
            sumn += input2
            
        input2 += input3

    return sumn

input1 = int(input("Total Levels in the hill pattern"))
input2 = int(input("The weight of the head level"))
input3 = int(input("The weight increments of each level"))

print(Hill_pattern(input1,input2, input3))
