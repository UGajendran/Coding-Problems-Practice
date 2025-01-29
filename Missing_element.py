#array arr 
arr = [1, 2, 4]
#Find The number of ELements present in the given array 
n = len(arr)
#N is summed by one since one element is missing
n = n + 1
#Original sum formula for N natural numbers
org_sum = int((n * (n + 1))/2)
#Sum got by the Current values 
act_sum = 0
for i in range(0, n - 1):
    act_sum += arr[i]

#Print The differnce between the Two sum which is said to be the missing element
print(org_sum - act_sum)
