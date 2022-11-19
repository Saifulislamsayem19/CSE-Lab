import keyword


def is_keyword_or_identifier(str):
    if keyword.iskeyword(str):
        print(str + " is an Python Keyword.")
    elif str.isidentifier():
        print(str + " is an valid Identifier.")
    else:
        print(str + " isn't an Python Keyword or Invalid Identifier.")


while True:
    str = input("Enter a word (e to exit):")
    if str == "e":
        break
    else:
        is_keyword_or_identifier(str)
