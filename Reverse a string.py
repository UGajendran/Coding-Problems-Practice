def reverseString(s):
    
    res = []
  
    # Traverse on s in backward direction
    
    for i in range(len(s) - 1, -1, -1):
        res.append(s[i])

    # Convert list back to string
    return ''.join(res)

s = input()
print(reverseString(s))
