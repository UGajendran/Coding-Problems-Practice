def lcmAndGcd(a , b):
        #store the a and b values in temp t1 and t2
        t1, t2 = a, b
        #Find Gcd 
        while b > 0:
            r = a % b
            a = b
            b = r
        Gcd = a
        #Find Lcm
        Lcm = int(( t1 * t2) / Gcd)
        return [Lcm, Gcd]
a = int(input("Enter the  number a: "))
b = int(input("Enter the number b: "))
#Call the function that has been defined
print(lcmAndGcd(a,b))
      
