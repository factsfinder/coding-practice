"""
Problem 6: Sentence Reversal

Given a string of words, reverse all the words. For example:
Input:  'This is the best'
Return: 'best the is This'

As part of this exercise you should remove all leading and trailing whitespace.
So that inputs such as:
'  space here'  and 'space here  '  both become: 'here space'

"""

def sentence_reversal(sentence):
    # make a list of words of the sentence.
    # The list may contain spaces
    words_list = []
    word = ""
    for i in range(len(sentence)):
        if sentence[i] == " ":
            words_list.append(word)
            word = ""
        elif i == len(sentence)-1:
            word += sentence[i]
            words_list.append(word)
        else:
            word += sentence[i]
        i += 1
    print(words_list)

    #remove spaces from the obtained list
    new_words_list = []
    for word in words_list:
        if word != "":
            new_words_list.append(word)

    print(new_words_list)

    return reverse_word(new_words_list)

def reverse_word(s):
    for i in range(len(s)//2):
        temp = s[i]
        s[i] = s[(len(s)-1)-i]
        s[(len(s)-1)-i] = temp
    return " ".join(s)

print(sentence_reversal("space here     "))
