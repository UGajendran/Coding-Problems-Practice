# Function to calculate the sum of all elements in a matrix
class Solution:
    def sumOfMatrix(self, N, M, Grid):
        # Initialize sum to 0
        total_sum = 0
        
        # Loop through each row of the matrix
        for i in range(N):
            # Loop through each column in the current row
            for j in range(M):
                # Add the current element to the total sum
                total_sum += Grid[i][j]
        
        # Return the total sum
        return total_sum


# Driver Code
def main():
    import sys
    input = sys.stdin.read
    data = input().splitlines()
    
    # Read the number of test cases
    t = int(data[0])
    index = 1  # Pointer to track input lines
    
    for _ in range(t):
        # Read dimensions of the matrix (N x M)
        N, M = map(int, data[index].split())
        index += 1
        
        # Initialize the matrix
        Grid = []
        
        # Read each row of the matrix
        for i in range(N):
            row = list(map(int, data[index].split()))
            Grid.append(row)
            index += 1
        
        # Create an instance of the Solution class
        solution = Solution()
        
        # Calculate the sum of the matrix and print the result
        print(solution.sumOfMatrix(N, M, Grid))
        
        # Print the separator "~"
        print("~")


# Entry point for the program
if __name__ == "__main__":
    main()
