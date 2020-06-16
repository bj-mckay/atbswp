# English to piglatin
print('Enter the English message to translate into Pig Latin:')
message = input()

VOWELS = ('a', 'e', 'i', 'o', 'u', 'y')

pigLatin = [] # A list of the words in Pig Latin.
for word in message.split():
    #separeate the non-letters at the start of this word:
    prefixNonLetters = ''
    while len(word) > 0 and not word[0].isalpha():
        prefixNonLetters += word[0]
        word = word[1:]
    if len(word) == 0:
        pigLatin.append(prefixNonLetters)
        continue

    #Separate the non-letters at the end of this word:
    suffixNonLetters = ''
    while not word[-1].isalpha():
        suffixNonLetters += word[-1]
        word = word[:1]

    #Remember if the word was in uppercase or title case
    wasUpper = word.isupper()
    wasTitle = word.istitle()

    word = word.lower() #make lower case for translation

    # Separate the consonants at the start of this word
    prefixConsonants = ''
    while len(word) > 0 and not word[0] in VOWELS:
        prefixConsonants += word[0]
        word = word[1:]

    #add the pig latin ending to the word
    if prefixConsonants != '':
        word += prefixConsonants + 'ay'
    else:
        word += 'yay'

    #Set the word back to upper case
    if wasUpper:
        word = word.upper()
    if wasTitle:
        word = word.title()

    # add the non-letters to the end or the start of the word
    pigLatin.append(prefixNonLetters + word + suffixNonLetters)
# Join all the wordds back together in a single string
print(' '.join(pigLatin))