from secrets import choice
from string import ascii_lowercase, ascii_uppercase, digits
from re import compile

def generate(message: str) -> str:
    flags = {'-lower': ascii_lowercase, 
             '-upper': ascii_uppercase, 
             '-digits': digits, 
             '-symbols': '!@#$%^()'}
    
    chars = ''
    
    sizeregex = compile(r'\!(\d+)')
    charregex = compile(r'(\-lower|\-upper|\-digits|\-symbols)')

    try:
        value = sizeregex.search(message)[1]
    except:
        value = 16
    size = int(value)

    options = charregex.findall(message)

    if options:
        for o in options:
            chars += flags[o]
    else:
        chars = chars.join(list(flags.values()))

    return ''.join(choice(chars) for i in range(size)) 

def talk(message: str) -> str:
    genrgx = compile(r'(\!\d+|\-lower|\-upper|\-digits|\-symbols)')
    
    if genrgx.search(message):
        return generate(message)
    elif message == 'Hello there':
        return '_General Kenobi_'
    else:
        return 'Repeat please'