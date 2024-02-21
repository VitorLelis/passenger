from secrets import choice
from string import ascii_lowercase, ascii_uppercase, digits
from re import compile,sub

def generate(message: str) -> str:
    """
    This function is designed to generate a random password based on provided flags. 
    It utilizes two regular expressions to identify the flags:

    1. Password size;
    2. Characters used.

    If the flags are not specified, default values are applied:

    1. Size of 16
    2. All characters
    """
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
    """
    Responsible for assessing the strength of a password by analyzing the types of characters present.
    """
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
    """
    This function computes the overall strength of a password using the following steps:

    1. Utilizes 'char_score' to identify characters and calculate their individual strength.
    2. Assesses the length, categorizing it as weak if it is less than 6 characters.
    3. Searches the strength dictionary for the result if the length is 6 or greater, returning the corresponding strength value.
    """
    strength = {
        0 : 13*[0],
        1 : 2*[0] + 6*[1] + 5*[2],
        2 :   [0] + 5*[1] + 7*[2],
        3 : 5*[1] + 8 *[2],
        4 : 5*[1] + 8 *[2]
    }

    msg = sub('=>','', message)

    size = len(msg)

    if size >= 6:
        score = char_score(msg)
        size_param = min(size-6,12)
    else:
        score = 0
        size_param = 0

    result = strength[score][size_param]

    answers = ['weak', 'moderate', 'strong']

    return 'Your password is '+ answers[result]

def talk(message: str) -> str:
    """
    This function is tasked with processing the incoming message and generating the appropriate response.
    """
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
    
    if message.startswith('?help'):
        return help
    elif message.startswith('=>'):
        return analyze(message)
    elif genrgx.search(message):
        return generate(message)
    elif message == 'Hello there':
        return '_General Kenobi_'
    else:
        return "Repeat please or type `?help` to learn what I can do"