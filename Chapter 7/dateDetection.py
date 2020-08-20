#! python3
# dateDetection.py - detects dates in the DD/MM/YYY format
import re, sys
print('Enter a date DD/MM/YYYY.')
date = str(input())
#date = str('28/02/2001')
leapyear = None
dateRegex = re.compile(r'''(
    ([0][1-9]|[1|2][0-9]|[3][0|1]) # Day
    \/                             # slash
    ([0][0-9]|[1][0-2])            # Month
    \/                             # slash
    ([1|2][0-9][0-9][0-9])         # Year   
)''', re.VERBOSE)
validaton = dateRegex.search(date)
if validaton is None:
    print('This is an invalid date.')
    sys.exit()
else:
    day = int(validaton.group(2))
    month = validaton.group(3)
    year = int(validaton.group(4))
if (year % 4) == 0:
    if (year % 100) == 0:
        if (year % 400) == 0:
            leapyear = True
        else:
            leapyear = False
if month == '02':
    if leapyear == True:
        if int(day) < 30:
            print('This is an valid February leapyear date!')
        else:
            if int(day) > 29:
                print('This is an invalid February Date')
    if leapyear != True:
        if int(day) > 28:
            print('This is an invalid February Date') 
        else:
            print('This is a valid date.')
elif month in ['04', '06', '09', '11']:
    if day > 30:
        print('Invalid: This month only has 30 days')
    else:
        print('This is a valid date.')
elif month in ['01', '03', '05', '07', '08', '10', '12']:
    print('This is a valid date.')