# User-defined function to find the minimum and maximum elements in an array
class Solution:
    def get_min_max(self, arr):
        # Initialize the minimum and maximum with the first element of the array
        min = int(arr[0])
        max = int(arr[0])
        
        # Get the length of the array
        n = len(arr)
        
        # Loop through the array to find the maximum element
        for i in range(n):
            if arr[i] > max:
                max = arr[i]
        
        # Loop through the array to find the minimum element
        for i in range(n):
            if arr[i] < min:
                min = arr[i]
        
        # Return the minimum and maximum as a tuple
        return (min, max)


# Driver Code
if __name__ == "__main__":
    # Read the number of test cases
    t = int(input())
    
    while t > 0:
        # Read the array of integers
        arr = list(map(int, input().split()))
        
        # Create an instance of the Solution class
        ob = Solution()
        
        # Call the get_min_max function and unpack the returned tuple
        mn, mx = ob.get_min_max(arr)
        
        # Print the minimum and maximum values
        print(mn, mx)
        
        # Decrement the test case counter
        t -= 1
        
        # Print the separator "~"
        print("~")
