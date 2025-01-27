#Given a number n, find the value of n raised to the power of its own reverse.
def reverse_exponentiation(n):
    
    rev = 0
    temp = n
    #Logic for reversing the given number n and finding its exponent like n**rev
    while n > 0:
        rem = n % 10
        rev = int((rev*10) + rem)
        n = n // 10

    #print the reverse exponent
    print(temp**rev)

n = int(input("Enter the number: "))

#Call the defined Function
reverse_exponentiation(n)
