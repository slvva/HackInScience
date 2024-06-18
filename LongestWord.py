text='Monty Python and the Holy Grail'

def longest_word(text):
    
    words=text.split()
    longest=max(words, key=len)
    return longest
    

print(longest_word(text))
