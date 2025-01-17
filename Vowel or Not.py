# User function Template for Python3
class Solution:
    # Function to check if a given character is a vowel
    def isVowel(self, c):
        # Define a set of vowels (both lowercase and uppercase)
        vow = set("aeiouAEIOU")
        
        # Check if the character is in the set of vowels
        if c in vow:
            return "YES"  # Return "YES" if the character is a vowel
        else:
            return "NO"  # Return "NO" if the character is not a vowel


# Driver Code
if __name__ == '__main__':
    # Read the number of test cases
    t = int(input())
    
    # Loop through each test case
    for _ in range(t):
        # Read the character input
        c = input()

        # Create an instance of the Solution class
        ob = Solution()
        
        # Call the isVowel function and print the result
        print(ob.isVowel(c))
