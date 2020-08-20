import re
passRegex = re.compile(r'''(
        (^.*(?=.{8,})(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).*$)
    )''', re.VERBOSE)

def strongPass(password):
    if len(password) < 8:
        print('Error: ' + password + ' is not long enough')
     
    else:
        mo = passRegex.search(password)
        if mo is not None:
            print(password + ' is secure')
        else:
            if mo is None:
                print('Error: ' + password + ' does not meet the minimum requirements')
  
strongPass('123456bG')
strongPass('v7DdwCFC')
strongPass('RJY7Dbhxr')
strongPass('VaFjoja555')
strongPass('^@j7tzQz')
strongPass('6qX3!fd%')
strongPass('77xj3Tq$qw')
strongPass('&&qjt3^m')
strongPass('E5E@2XV&')
strongPass('Hr!fSDyp')
strongPass('1234567')
strongPass('abcdefg')