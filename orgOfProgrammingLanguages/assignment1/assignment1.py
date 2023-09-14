"""
Write a program in any programming language of your choice to read a statement
(or statements) written in a specific programming language called (OPCS) that has
the following specific rules:
1- Keywords: if , then.
2- Identifier rules: A sequence of letters, digits, and underscores. However,
the identifier must start with either a letter or an underscore.
3- Digits: A sequence od digits (at least one digit)
4- Arithmetic operators: +, -, *, **, /, and %.
5- Logical Operators: and, or, ==, !=.
6- Assignment operator: =.
7- Comments: Any line (or lines) that starts with “” and ends with “” will
count as comments.
"""

# input: result = x + y / 2 ""Result Equation""
# preprocessor: result=x+y/2
# scanner: (IDENTIFIER: _result) (ASSIGNMENT_OPEREATOR: =) (IDENTIFIER: x) (ARITHMATIC_OPERATOR: +) (DIGIT: 2) (ARITHMATIC_OPERATOR: /) (DIGIT: 2)

# input_code = ' result = x + y / 2 ""Result Equation"" '

# read input code from file
input_code = ''
with open('inputCode.opcs', 'r') as file:
    input_code = file.read()

input_code = input_code.split('\n')

print(input_code)

def preprocessor(code):
    # remove spaces
    code = code.replace(' ', '')

    # remove comments between double double quotes
    while code.find('""') != -1:
        start = code.find('""')
        end = code.find('""', start+2)
        code = code[:start] + code[end+2:]
    
    return code


preprocessed_code = []
for line in input_code:
    preprocessed_code.append(preprocessor(line))
print(preprocessed_code)


def tokenizer(code):
    # convert code to list of tokens
    tokens = []
    token = ''
    for char in code:
        if char in ['+', '-', '*', '**', '/', '%', '=', '==','!=']:
            if token != '':
                tokens.append(token)
                token = ''
            tokens.append(char)
        else:
            token += char
    if token != '':
        tokens.append(token)
    
    return tokens

tokens=[]
for line in preprocessed_code:
    tokens.append(tokenizer(line))

print(tokens)



def scanner(tokens):
    # convert list of tokens to list of tuples (token_type, token_value)
    scanned_tokens = []
    for token in tokens:
        if token in ['+', '-', '*', '**', '/', '%', '==','!=']:
            scanned_tokens.append(('ARITHMATIC_OPERATOR', token))
        elif token == '=':
            scanned_tokens.append(('ASSIGNMENT_OPERATOR', token))
        elif token in ['and', 'or']:
            scanned_tokens.append(('LOGICAL_OPERATOR', token))
        elif token in ['if', 'then']:
            scanned_tokens.append(('KEYWORD', token))
        elif token.isdigit():
            scanned_tokens.append(('DIGIT', token))
        else:
            scanned_tokens.append(('IDENTIFIER', token))
    
    return scanned_tokens



scanned_tokens = []
for line in tokens:
    scanned_tokens.append(scanner(line))
print(scanned_tokens)
