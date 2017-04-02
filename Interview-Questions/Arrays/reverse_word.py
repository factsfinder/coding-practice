"""
Problem 5: Reverse String/Word
Reverse the letters in a given string/word.
Example:
Input:  "Hello"
Output: "olleh"
"""

def reverse_word(s):
    s = list(s)
    for i in range(len(s)//2):
        temp = s[i]
        s[i] = s[(len(s)-1)-i]
        s[(len(s)-1)-i] = temp
    return "".join(s)
print(reverse_word("hesxlo"))
