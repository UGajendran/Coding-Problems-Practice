class Solution:
    def findMedian(self, arr):
        # Sort the array to arrange elements in ascending order
        arr.sort()
        
        # Find the length of the array
        n = len(arr)
        
        # Find the middle index
        s = int(n / 2)
        
        # If the number of elements is odd, return the middle element
        if n % 2 != 0:
            return arr[s]
        else:
            # If the number of elements is even, calculate the median as the average
            # of the two middle elements
            mid1 = s  # First middle element
            mid2 = s - 1  # Second middle element
            med = (arr[mid1] + arr[mid2]) / 2  # Calculate the median
            return med


# { 
# Driver Code Starts
def main():
    # Read the number of test cases
    t = int(input().strip())
    
    # Loop through each test case
    for _ in range(t):
        # Read input as a list of integers
        arr = list(map(int, input().strip().split()))
        
        # Create an instance of the Solution class
        solution = Solution()
        
        # Call the findMedian function and store the result
        ans = solution.findMedian(arr)
        
        # If the result is an integer, print it without a decimal point
        if int(ans) == ans:
            print(int(ans))
        else:
            # Otherwise, print the result as a floating-point number
            print(ans)


# Entry point of the program
if __name__ == "__main__":
    main()

# } Driver Code Ends
