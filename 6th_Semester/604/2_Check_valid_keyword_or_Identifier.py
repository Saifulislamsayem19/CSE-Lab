
def is_identifier(str1):
    if not((65 <= ord(str1[0]) <= 90) or (97 <= ord(str1[0]) <= 122) or ord(str1[0]) == 95):
        return False
    for i in range(len(str1)):
        if not ((65 <= ord(str1[i]) <= 90) or (97 <= ord(str1[i]) <= 122) or ord(str1[i]) == 95 or (48 <= ord(str1[i]) <= 57)):
            return False
    return True


key_word = ["auto", "double", "int", "struct", "break", "else", "long",
            "switch", "case", "enum", "register", "typedef", "char",
            "extern", "return", "union", "const", "float", "short",
            "unsigned", "continue", "for", "signed", "void", "default",
            "goto", "sizeof", "voltile", "do", "if", "static", "while"]

str1 = input("Enter any program: ")
str2 = str1.split()
for str3 in str2:
    if str3 in key_word:
        print(str3 + " is a Keyword.")
    elif is_identifier(str3):
        print(str3 + " is a valid Identifier.")
    else:
        lst = ['{', '}', ';', '()', ',']
        if str3 in lst:
            None

        # if str3 == '{' or str3 == '}' or str3 == '()' or str3 == ';':
        #     None
        else:
            str4 = str3.translate({ord(i): None for i in '();{},'})
            if is_identifier(str4):
                print(str4 + " is a valid Identifier.")

            else:
                print(str4 + " is not a keyword or valid Identifier.")

# int main() { int a, a?b, a_b; }
