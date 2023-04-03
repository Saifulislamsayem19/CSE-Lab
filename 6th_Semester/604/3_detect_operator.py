
s = input("Enter an Equation (e to exit): ")
lst = s.split()

for i in range(len(lst)):

    #Arithmatic Operator
    if "+" in lst[i]:
        print(lst[i] + " Plus Operator.")
    elif lst[i] == "-":
        print(lst[i] + " Minus Operator.")
    elif lst[i] == "*":
        print(lst[i] + " Multiply Operator.")
    elif lst[i] == "/":
        print(lst[i] + " Divide Operator.")
    elif lst[i] == "%":
        print(lst[i] + " Modulas Operator.")

    #Logical Operator
    elif lst[i] == "||":
        print(lst[i] + " Logical OR Operator.")
    elif lst[i] == "&&":
        print(lst[i] + " Logical AND Operator.")
    elif lst[i] == "!":
        print(lst[i] + " Logical NOT Operator.")

    #Assignment Operator
    elif lst[i] == " == ":
        print(lst[i] + " Equal Operator.")
    elif lst[i] == "<":
        print(lst[i] + " Less Than Operator.")
    elif lst[i] == ">":
        print(lst[i] + " Greater Than Operator.")
    elif lst[i] == "<=":
        print(lst[i] + " Less than or equal Operator.")
    elif lst[i] == ">=":
        print(lst[i] + " Greater than or equal Operator.")
    elif lst[i] == "!=":
        print(lst[i] + " Not equal Operator.")

    #Relational Operator
    elif lst[i] == "=":
        print(lst[i] + " Assign assignment Operator.")
    elif lst[i] == "+=":
        print(lst[i] + " Add AND assignment Operator.")
    elif lst[i] == "-=":
        print(lst[i] + " Subtract AND assignment Operator.")
    elif lst[i] == "*=":
        print(lst[i] + " Multiply AND assignment Operator.")
    elif lst[i] == "/=":
        print(lst[i] + " Divide AND assignment Operator.")
    elif lst[i] == "%=":
        print(lst[i] + " Modulas AND assignment Operator.")

    elif lst[i] == "++":
        print(lst[i] + " Increment Operator.")
    elif lst[i] == "--":
        print(lst[i] + " Decrement Operator.")

    #Bitwise Operator
    elif lst[i] == "|":
        print(lst[i] + " Bitwise OR Operator.")
    elif lst[i] == "&":
        print(lst[i] + " Bitwise AND Operator.")
    elif lst[i] == "<<":
        print(lst[i] + " Binary Left Shift Operator.")
    elif lst[i] == ">>":
        print(lst[i] + " Binary Right Shift Operator.")
    elif lst[i] == "^":
        print(lst[i] + " Binary XOR Operator.")
    elif lst[i] == "~":
        print(lst[i] + " Binary One's Complement Operator.")

    else:
        print(lst[i] + " It's not an Operator.")
