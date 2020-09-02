import pyinputplus as pyip
import sys
while True:
    prompt = pyip.inputYesNo('Want to know how to keep an idiot busy for hours?\n')
    if prompt == 'no':
        print('Thank you. Have a nice day.')
        sys.exit()
    if prompt == 'yes':
        continue