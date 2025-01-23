def nStarDiamond(n: int):
    def Up(n: int):
        c = 2
        star = 1
        #Logic For Upper Half
        for i in range(0,n):
            F_s = (" ") * ((n*2) - c)
            Stars = ("* ") * star
            print(F_s + Stars)
            star += 2
            c += 2
    def Low(n: int):
        c = 2*n
        star = (2*n) - 1
        #Logic for Lower Half
        for i in range(0, n):
            F_s = (" ") * ((2 * n) - c)
            Star = ("* ") * (star)
            print(F_s + Star)
            c -= 2
            star -= 2
    #Call the defined Functions
    Up(n)
    Low(n)

n =  int(input("Enter the value of n: "))
nStarDiamond(n)
