from secrets import choice
from string import ascii_lowercase, ascii_uppercase, digits
from re import compile,sub

def generate(message: str) -> str:
    flags = {'-lower': ascii_lowercase, 
             '-upper': ascii_uppercase, 
             '-digits': digits, 
             '-symbols': '!@#$%^()'}
    
    chars = ''
    
    sizeregex = compile(r'\!(\d+)')
    charregex = compile(r'(\-lower|\-upper|\-digits|\-symbols)')

    try:
        size = int(sizeregex.search(message)[1])
    except:
        size = 16

    options = charregex.findall(message)

    if options:
        for o in options:
            chars += flags[o]
    else:
        chars = chars.join(list(flags.values()))

    return ''.join(choice(chars) for i in range(size)) 

def char_score(message: str) -> int:
    lower = compile(r'[a-z]')
    upper = compile(r'[A-Z]')
    digits = compile(r'[0-9]')
    symbols = compile(r'[\!\@\#\$\%\^\(\)]')

    score = 0

    if lower.search(message):
        score += 1
    if upper.search(message):
        score += 1
    if digits.search(message):
        score += 1
    if symbols.search(message):
        score += 1
    
    return score

def analyze(message: str) -> str:
    strength = {
        0 : 13*[0],
        1 : 2*[0] + 6*[1] + 5*[2],
        2 :   [0] + 5*[1] + 7*[2],
        3 : 5*[1] + 8 *[2],
        4 : 5*[1] + 8 *[2]
    }

    msg = sub('=>','', message)

    score = char_score(msg)

    size = len(msg)

    score = 0 if size < 6 else char_score(msg)

    size_param = min(size-6, 12)

    result = strength[score][size_param]

    answers = ['weak', 'moderate', 'strong']

    return 'Your password is '+ answers[result]

def talk(message: str) -> str:
    genrgx = compile(r'(\!\d+|\-lower|\-upper|\-digits|\-symbols)')

    help = '''Here is what I can do:
    **GENERATE PASSWORDS**:
        Use `!NUMBER` to determine the length of the password and apply some flags:
            `-lower` to Lowercase
            `-upper` to Uppercase
            `-digits`  to Digits
            `-symbols` to !@#$%^()
        No flags will use all of them by default
        No `!NUMBER` will apply an length of 16 by default
    **ANALYZE PASSWORDS**:
        Any sequence of characters starting with `=>` will be analyzed as an password
    '''
    
    if genrgx.search(message):
        return generate(message)
    elif message.startswith('=>'):
        return analyze(message)
    elif message == 'Hello there':
        return '_General Kenobi_'
    elif message.startswith('?help'):
        return help
    else:
        return "Repeat please or type `?help` to learn what I can do"