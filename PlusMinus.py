def PlusMinus(arr):

    pos = 0
    neg = 0
    zer = 0
    n = len(arr)
    for i in range(0, n):
        if arr[i] > 0:
            pos += 1
        elif arr[i] < 0:
            neg += 1
        else:
            zer += 1
            
    print(pos/n)
    print(neg/n)
    print(zer/n)

arr = list(map(int, input().split()))
PlusMinus(arr)

