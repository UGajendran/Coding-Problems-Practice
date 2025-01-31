arr = list(map(int, input().split()))
temp = []
g = []
n = len(arr)
flag = 0
#Iterate Over the Array and Find the Repeating Elements
for i in range(0, n):
    if arr[i] in temp:
        #If Elements already in temp then raise the flag and add it to the g array
        flag += 1
        g.append(arr[i])
    else:
        #If elements not in temp then add the elememts to temp
        temp.append(arr[i])

#Print the elements inn g array (i.e) Repeating elements
for i in range(0, flag):
    print(g[i])
