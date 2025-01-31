#Right Rotating of array by k elements
arr = list(map(int, input().split()))
k = int(input())
for i in range(0, k):
    #store the Last value in temp using pop()
    temp = arr.pop()
    #Insert it into the zeroth Index k times
    arr.insert(0, temp)

print(arr)
