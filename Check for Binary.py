# Function to check if a given string represents a binary number
class Solution:
    def isBinary(self, s):
        # Loop through each character in the string
        for char in s:
            # If the character is not '0' or '1', return False
            if char != '0' and char != '1':
                return False
        # If no non-binary character is found, return True
        return True


# Driver Code
def main():
    # Importing for user input
    import sys
    input = sys.stdin.read
    data = input().splitlines()
    
    # Read the number of test cases
    T = int(data[0])
    
    # Loop through the test cases
    for test_case in range(1, T + 1):
        # Read the binary string for the current test case
        str_val = data[test_case]
        
        # Create an instance of the Solution class
        solution = Solution()
        
        # Check if the string is binary
        is_binary = solution.isBinary(str_val)
        
        # Print "true" if the string is binary, otherwise print "false"
        if is_binary:
            print("true")
        else:
            print("false")
        
        # Print the separator "~" as specified
        print("~")


# Entry point for the program
if __name__ == "__main__":
    main()
