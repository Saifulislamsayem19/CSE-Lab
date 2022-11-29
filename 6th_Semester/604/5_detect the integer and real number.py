import re


def is_real(n):
    realnum = re.compile(r"^[-+]?[0-9]*\.?[0-9]+(e[-+]?[0-9]+)?$")
    if realnum.match(n):
        # if isinstance(n, int):
        #     print(f'{n} is a real number and also a integer number.')
        # else:
        #     print(f'{n} is a real number but not a integer number.')

        # try:
        #     int(i)
        #     print(f'{n} is a real number and also a integer number.')
        # except ValueError:
        #     print(f'{n} is a real number but not a integer number.')
        return True

    else:
        return False


i = input("Enter a number: ")

if is_real(i):
    try:
        int(i)
        print(f'{i} is a real number and also a integer number.')
    except ValueError:
        print(f'{i} is a real number but not a integer number.')
else:
    print(f'{i} isn\'t a real number.')

# try:
#     int(i)
#     print(f'{i} is a integer number.')
# except:
#     print(f'{i} is a real number.')

# if i - int(i) == 0:
#     print(f'{i} is a integer number.')
# else:
#     print(f'{i} is a real number.')
