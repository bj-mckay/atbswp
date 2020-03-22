spam = ['apples', 'bananas', 'tofu', 'cats']
ham = ['apples', 'bananas', 'tofu', 'cats', 'ham']
emptyList = []

def commaList(listName):
    if len(listName) == 0: # When empty lists are passed
        print('This is an empty list') # Print a notification
    else : # Otherwise run this for loop
        for i in range(len(listName) -1): 
            print(listName[i] + ', ', end = '')
        print('and ' + listName[-1])

# Examples of the commaList function called against different lists 
commaList(spam)
commaList(ham)
commaList(emptyList)