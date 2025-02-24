# Problem Statement:
# Given a string containing multiple words, the task is to compute a numerical value 
# for each word based on the absolute differences of the first and last letters moving inward.
# If a word has a middle letter (odd length), its alphabetical position is added.
# The final output is obtained by concatenating the computed values of all words.

# Approach:
# - Split the input string into words.
# - Convert each word to uppercase for uniformity.
# - Use a two-pointer technique to calculate the absolute differences of letter pairs.
# - If the word has an odd length, add the middle letter’s alphabetical position.
# - Concatenate the computed values of all words to form the final result.
# - Return the concatenated number as an integer.

def let(s):
    s = input1.split()
    sh = ""
    for i in s:
        i = i.upper()
        n = len(i)
        j, k = 0, n -1
        sumn = 0
        while j <= k:
            if j == k:
                sumn += ord(i[j]) - 64
            sumn += abs(ord(i[j]) - ord(i[k]))
            j += 1
            k -= 1
                

        sh += str(sumn)

    return int(sh)

input1 = str(input())
print(let(input1))
