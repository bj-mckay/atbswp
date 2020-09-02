import pyinputplus as pyip
total = 0
bread = pyip.inputMenu(['wheat', 'white', 'sourdough'], numbered=True)
protein = pyip.inputMenu(['chicken', 'turkey', 'ham', 'tofu'], numbered=True)
cheese = pyip.inputYesNo('Would you like cheese on that?\n')
if cheese == 'yes':
    cheeseType = pyip.inputMenu(['cheddar', 'swiss', 'mozzarella'], numbered=True)

mayo = pyip.inputYesNo('Would you like mayo on that?\n')
mustard = pyip.inputYesNo('Would you like mustard on that?\n')
lettuce = pyip.inputYesNo('Would you like lettuce on that?\n')
tomato = pyip.inputYesNo('Would you like tomato on that?\n')
quantity = pyip.inputInt('How many sandwiches would you like?\n')

order = [bread, protein, cheese, mayo, mustard, lettuce, tomato]
total += float(5.50) # base price of sandwich
if order[2] == 'yes':
    total += 1.00 # upcharge for cheese
if order[3] == 'yes':
    total += 0.25 # upcharge for mayo
if order[4] == 'yes':
    total += 0.25 # upcharge for mustard
if order[5] == 'yes':
    total += 0.25 # upcharge for lettuce
if order[6] == 'yes':
    total += 0.25 # upcharge for tomato 
print('Your total is:')   
print(total * quantity)
