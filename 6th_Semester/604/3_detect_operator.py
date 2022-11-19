
s = input("Enter an operator: ")

#Arithmatic Operator
if s == "+":
    print("Plus Operator.")
elif s == "-":
    print("Minus Operator.")
elif s == "*":
    print("Multiply Operator.")
elif s == "/":
    print("Divide Operator.")
elif s == "%":
    print("Modulas Operator.")

#Logical Operator
elif s == "||":
    print("Logical OR Operator.")
elif s == "&&":
    print("Logical AND Operator.")
elif s == "!":
    print("Logical NOT Operator.")

#Assignment Operator
elif s == " == ":
    print("Equal Operator.")
elif s == "<":
    print("Less Than Operator.")
elif s == ">":
    print("Greater Than Operator.")
elif s == "<=":
    print("Less than or equal Operator.")
elif s == ">=":
    print("Greater than or equal Operator.")
elif s == "!=":
    print("Not equal Operator.")

#Relational Operator
elif s == "=":
    print("Assign assignment Operator.")
elif s == "+=":
    print("Add AND assignment Operator.")
elif s == "-=":
    print("Subtract AND assignment Operator.")
elif s == "*=":
    print("Multiply AND assignment Operator.")
elif s == "/=":
    print("Divide AND assignment Operator.")
elif s == "%=":
    print("Modulas AND assignment Operator.")

elif s == "++":
    print("Increment Operator.")
elif s == "--":
    print("Decrement Operator.")

#Bitwise Operator
elif s == "|":
    print("Bitwise OR Operator.")
elif s == "&":
    print("Bitwise AND Operator.")
elif s == "<<":
    print("Binary Left Shift Operator.")
elif s == ">>":
    print("Binary Right Shift Operator.")
elif s == "^":
    print("Binary XOR Operator.")
elif s == "~":
    print("Binary One's Complement Operator.")

else:
    print("It's not an Operator.")