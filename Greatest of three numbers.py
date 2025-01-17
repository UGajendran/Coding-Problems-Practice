# User function Template for Python3
class Solution:
    # Function to find the greatest of three numbers
    def greatestOfThree(self, A, B, C):
        # Check if A is greater than B
        if A > B:
            # If A is also greater than C, return A, else return C
            if A > C:
                return A
            else:
                return C
        else:
            # If B is greater than C, return B, else return C
            if B > C:
                return B
            else:
                return C


# Driver Code
if __name__ == "__main__":
    # Read the number of test cases
    t = int(input())
    
    # Loop through each test case
    for _ in range(t):
        # Read three integers A, B, and C
        A, B, C = map(int, input().split())

        # Create an instance of the Solution class
        ob = Solution()
        
        # Call the greatestOfThree function and print the result
        print(ob.greatestOfThree(A, B, C))
        
        # Print the separator "~" after the result
        print("~")
