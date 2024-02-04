from secrets import choice
from string import ascii_lowercase, ascii_uppercase, digits
from re import compile

def generate(message: str) -> str:
    flags = {'-lower': ascii_lowercase, 
             '-upper': ascii_uppercase, 
             '-digits': digits, 
             '-symbols': '!@#$%^()'}
    
    chars = ""

    for k,v in flags.items():
        if k in message:
            chars += v
    if chars == "":
        chars = ascii_lowercase + ascii_uppercase + digits + flags['-symbols']

    regex = compile(r'\!(\d+)')
    try:
        value = regex.search(message)[1]
    except:
        value = 16
    size = int(value)

    return ''.join(choice(chars) for i in range(size)) 

def talk(message: str) -> str:
    genrgx = compile(r'(\!\d+|\-lower|\-upper|\-digits|\-symbols)')
    
    if genrgx.search(message):
        return generate(message)
    elif message == 'Hello there':
        return '_General Kenobi_'
    else:
        return 'Repeat please'