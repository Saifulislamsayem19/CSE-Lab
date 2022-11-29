import nltk
import re

f = open('tokens.txt', 'r')
# f = open('C:\\Users\\Saiful IN\\Desktop\\My Program\\C\\Mathematical problem\\GCD.c', 'r')
program = f.read()
count = 0

All_token = []
Identifiers_Output = []
Invalid_Identifiers = []
Keywords_Output = []
Symbols_Output = []
Operators_Output = []
Numerals_Output = []
Headers_Output = []


def remove_spaces(program):
    scanned_program = []
    for line in program:
        if line.strip() != '':
            scanned_program.append(line.strip())
    return scanned_program


def remove_comments(program):
    multi_comments_removed = re.sub("/\*[^*]*\*+(?:[^/*][^*]*\*+)*/", "", program)
    single_comments_removed = re.sub("//.*", "", multi_comments_removed)
    comments_removed = single_comments_removed
    return comments_removed


RE_Keywords = "auto|double|int|struct|break|else|long|switch|case|enum|register|typedef|char|extern|return|union|const|"\
              "float|short|unsigned|continue|for|signed|void|default|goto|sizeof|voltile|do|if|static|while"
RE_Operators = "^[\++]|(-)|(=)|(\*)|(/)|(%)|(--)|(<)|(>)|(\&)"
# RE_Operators = "(+)|(-)|(*)|(/)|(%)|(\&&)|(!)|(=)|(<)|(>)|(\<=)|(\>=)|(\!=)|(\+=)|(\-=)|(\*=)|(\%=)|(\++)|(\--)|(&)|(\<<)|(\>>)|(^)|(~)"
# RE_Operators = "(+)|(-)|(*)|(/)|(%)|(\&&)|(!)|(=)|(<)|(>)|(\<=)|(\>=)|(\!=)|(\+=)|(\-=)|(\*=)|(\%=)|(\++)|(\--)|(&)|(\<<)"
RE_Numerals = "^(\d+)$"
RE_Special_Characters = "[\[@&~!#$\^\|{}\]:;<>?,\.']|\(\)|\(|\)|{}|\[\]|\""
RE_Identifiers = "^[a-zA-Z_]+[a-zA-Z0-9_]*"
RE_Headers = "([a-zA-Z]+\.[h])"

comments_removed = remove_comments(program)
prog = comments_removed.split('\n')

scanned_Prog = remove_spaces(prog)

scanned_program = '\n'.join([str(elem) for elem in scanned_Prog])

scanned_Program_lines = scanned_program.split('\n')
match_counter = 0

Source_Code = []
for line in scanned_Program_lines:
    Source_Code.append(line)
print(Source_Code)

display_counter = 0

for line in Source_Code:
    count = count + 1
    if line.startswith("#include"):
        Headers_Output.append(line)
        tokens = ""
    else:
        tokens = nltk.wordpunct_tokenize(line)

    for token in tokens:
        All_token.append(token)
        if re.findall(RE_Keywords, token):
            Keywords_Output.append(token)
        elif re.findall(RE_Operators, token):
            Operators_Output.append(token)
        elif re.findall(RE_Numerals, token):
            Numerals_Output.append(token)
        elif re.findall(RE_Special_Characters, token):
            Symbols_Output.append(token)
        elif re.findall(RE_Identifiers, token):
            Identifiers_Output.append(token)
        else:
            Invalid_Identifiers.append(token)

print("There Are ", len(Keywords_Output), "Keywords: ", Keywords_Output)
print("There Are ", len(Identifiers_Output), "Identifiers: ", Identifiers_Output)
print("There Are ", len(Invalid_Identifiers), "Invalid Identifiers: ", Invalid_Identifiers)
print("There Are ", len(Operators_Output), "Operators: ", Operators_Output)
print("There Are ", len(Headers_Output), "Header Files: ", Headers_Output)
print("There Are", len(Symbols_Output), "Symbols:", Symbols_Output)
print("There Are ", len(Numerals_Output), "Numerals:", Numerals_Output)
print("There Are total: ", len(All_token), " Tokens: ", All_token)
