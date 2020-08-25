import re
stripRegex = re.compile(r'''
        ^\s*(.*?)\s*$
    ''', re.VERBOSE)
string = ' This should work like the strip method.  '
char = 'i'
def stripMethod(string, char=None):
    if not char:
        strip = stripRegex.findall(string)
        string = str(strip)
        print(string)
        
    else:
        strip_char = re.compile(char)
        string = re.sub(strip_char, "", string)
        print(string)
    
stripMethod(string)
stripMethod(string, char)