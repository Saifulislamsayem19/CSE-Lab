def isValid(str1):
    # if not ((ord('a') <= ord(str1[0]) <= ord('z')) or (ord('A') <= ord(str1[0]) <= ord('Z')) or
    #         ord(str1[0]) == ord('_')):
    #     return False
    if not ((65 <= ord(str1[0]) <= 90) or (97 <= ord(str1[0]) <= 122) or ord(str1[0]) == 95):
        return False

    # for i in range(1, len(str1)):
    #     if not ((ord('a') <= ord(str1[i]) <= ord('z')) or (ord('A') <= ord(str1[i]) <= ord('Z')) or (
    #             ord('0') <= ord(str1[i]) <= ord('9')) or ord(str1[i]) == ord('_')):
    #         return False
    for i in range(1, len(str1)):
        if not ((65 <= ord(str1[i]) <= 90) or (97 <= ord(str1[i]) <= 122) or (48 <= ord(str1[i]) <= 57) or
                ord(str1[i]) == 95):
            return False

    return True

# def isValid(str):
#     if not (('a' <= str[0] <= 'z') or ('A' <= str[0] <= 'Z') or str[0] == '_'):
#         return False
#
#     for i in range(len(str)):
#         if not (('a' <= str[i] <= 'z') or ('A' <= str[i] <= 'Z') or ('0' <= str[i] <= '9') or str[i] == '_'):
#             return False


key_word = ["auto", "double", "int", "struct", "break", "else", "long",
            "switch", "case", "enum", "register", "typedef", "char",
            "extern", "return", "union", "const", "float", "short",
            "unsigned", "continue", "for", "signed", "void", "default",
            "goto", "sizeof", "voltile", "do", "if", "static", "while"]

while True:
    str = input("Enter a word (e to exit):")
    if str == "e":
        break
    elif str in key_word:
        print(str + " is a keyword.")
    elif isValid(str):
        print(str + " is valid identifier.")
    else:
        print(str + " is not a keyword or valid Identifier")
