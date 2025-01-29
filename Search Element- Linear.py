#Array arr
arr = [1,23, 4,5,8,94,3,5]
n = len(arr)
s = int(input("Enter the Element to be searched: "))
#Searching the value s is present in arr or not using Linear Search
flag = 0
for i in range(0, n):
        #For each value Check it Equals the searching Element s or not
        if arr[i] == s:
            flag = 1
            
if flag == 1:
    print(f"The element {s} is present in the array")
else:
    print("Not found")
