import re
import nltk


def is_real(n):
    exp = re.compile(r"[-+]?[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)")
    flt = re.compile(r"^[+-]?([0-9]*[.])?[0-9]+$")
    integer = re.compile(r"[+-]?(?<!\.)\b[0-9]+\b(?!\.[0-9])")

    if exp.match(n):
        print(f'{n} is a exponential number.')
    elif integer.match(n):
        print(f'{n} is a int number.')
    elif flt.match(n):
        print(f'{n} is a float number.')
    else:
        print(f"{n} isn't a digit.")


RE_Operators = re.compile("(\++)|(-)|(=)|(\*)|(/)|(%)|(--)|(<=)|(>=)|(\&)")

i = input("Enter a number: ")

# tokens = nltk.wordpunct_tokenize(i)
# print(tokens)
num = i.split()
for x in num:
    is_real(x)


# 4.5e-2 +4.5 -2 -2.7 100
# 4.5+6=10.5
# 9+4.285+67.453E-564

