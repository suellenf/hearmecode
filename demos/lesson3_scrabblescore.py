score = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2, 
         "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3, 
         "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1, 
         "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4, 
         "x": 8, "z": 10}
word=raw_input("Enter the word you'd like to score:\n")
word=word.lower()

word_score = 0
letter_score = 0
for w in word:
    #print "getting a score for {0}".format(w)
    letter_score = score[w]
    #print letterscore
    word_score = word_score + letter_score
print "The score for {0} is {1}".format(word,word_score)