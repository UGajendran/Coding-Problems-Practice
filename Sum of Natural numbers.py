# Function to calculate the sum of the first n natural numbers
class Solution:
    @staticmethod
    def seriesSum(n):
        # Initialize the sum to 0
        sum = 0
        
        # Loop from 1 to n (inclusive) to calculate the sum
        for i in range(1, n + 1):
            sum += i
        
        # Return the calculated sum
        return sum


# Driver Code
def main():
    import sys
    input = sys.stdin.read
    data = input().splitlines()
    
    # Read the number of test cases
    t = int(data[0])
    results = []
    
    for test_case in range(1, t + 1):
        # Read the value of n for each test case
        n = int(data[test_case])
        
        # Create an instance of the Solution class and call the seriesSum method
        solution = Solution()
        res = solution.seriesSum(n)
        
        # Append the result to the results list
        results.append(res)
    
    # Print all the results line by line
    for result in results:
        print(result)
        print("~")


# Entry point for the program
if __name__ == "__main__":
    main()
