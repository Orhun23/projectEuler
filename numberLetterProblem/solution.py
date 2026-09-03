import inflect

def number_to_words(num):
    p = inflect.engine()
    return p.number_to_words(num)

num = 1
ch = 0
while num < 1001:
    words = number_to_words(num)
    words_without_spaces = ''.join(words.split()).replace('-','')

    
    print(words)
    print(len(words))
    
    ch += len(words_without_spaces)
    num += 1
    
print("Total character count without spaces:", ch)