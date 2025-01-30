#Given an array arr[] of positive integers and another integer target.
#Determine if there exists two distinct indices such that the sum of there elements is equals to target.
arr = list(map(int, input().split()))
target = int(input())

c = set(arr)

#Iterate Over the Array one by one
for i in range(0, len(arr)):
    #Store the current index and find the difference between target and current index
    one = arr[i]
    two = target - one
    
    #Check if the diference value is present in array
    if two in c:
        print("Yes")
        break

else:
    print("No")
