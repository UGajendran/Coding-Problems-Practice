def single_number(nums):
    result = 0
    for num in nums:
        result ^= num  # XOR operation
    return result

#Input array
arr = list(map(int, input().split()))
print(single_number(arr))
