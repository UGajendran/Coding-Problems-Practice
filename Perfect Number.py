
#Perfect Number

def Perfect_number(n):
    
    s = []
    #Iterate till n/2 to find the divisors
    for i in range(1, int((n/2)+1)):
        if n % i == 0:
            s.append(i)

    j = len(s)
    sums = 0
    #Now Find the sum of the s array
    for i in range(0, j):
        sums += s[i]

    #Check if the sum value equals n if yes Print "True" else "False"

    if (sums == n):
        return True
    else:
        return False

#Input
n = int(input())

print(Perfect_number(n))
