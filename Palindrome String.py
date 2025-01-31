import re

def is_palindrome(s):
    s = re.sub(r'[^a-zA-Z0-9]', '', s).lower()  # Remove non-alphanumeric characters & convert to lowercase
    return s == s[::-1]  # Check if string is the same forward and backward

s = input()

print(is_palindrome(s))
