#Rotate array bu one element
arr = list(map(int, input().split()))
#Store the Last Element in temp using pop()
temp = arr.pop()
#Insert the element in the zeroth index
arr.insert(0, temp)
print(arr)
