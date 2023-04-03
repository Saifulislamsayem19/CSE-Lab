import nltk

program = input("Enter a program: ")
count = 0
All_token = []


def remove_Spaces(program):
    scanned_Program = []
    for line in program:
        if line.strip() != '':
            scanned_Program.append(line.strip())
    return scanned_Program


prog = program.split('\n')
scanned_Prog = remove_Spaces(prog)
scanned_Program = '\n'.join([str(elem) for elem in scanned_Prog])
scanned_Program_lines = scanned_Program.split('\n')
match_counter = 0

Source_Code = []
for line in scanned_Program_lines:
    Source_Code.append(line)
print(Source_Code)
display_counter = 0

for line in Source_Code:
    count = count + 1

    tokens = nltk.wordpunct_tokenize(line)
    for token in tokens:
        All_token.append(token)

print("There Are total: ", len(All_token), " Tokens: ", All_token)

# int main() { int a,b=20,c;}
# float x = a + 1b, y=a++b2, z= c+2;
