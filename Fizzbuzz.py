#Fizzbuzz

def fizz_buzz(n):
    #array to be returned
    result = []
    for i in range(1, n + 1):
        #Check if both 3 and 5 divides i
        if i % 3 == 0 and i % 5 == 0:
            result.append("FizzBuzz")
        #Check for 3 alone
        elif i % 3 == 0:
            result.append("Fizz")
        #Check for 5 alone
        elif i % 5 == 0:
            result.append("Buzz")
        #Not Divisible by 3 and 5
        else:
            result.append(str(i))
    return result

n = int(input())

print(fizz_buzz(n))
