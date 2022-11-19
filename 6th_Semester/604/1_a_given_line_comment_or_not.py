
def is_comment(line):
    if line[0] == "/" and line[1] == "/":
        print("Given line is single-line comment")
        return
    elif line[0] == "/" and line[1] == "*" and line[len(line)-2] == "*" and line[len(line)-1] == "/":
        print("Given line is multi-line comment")
        return
    else:
        print("Not a comment.")


while True:
    line = input("Enter a line or e to exit: ")
    if line.lower() == "e":
        break
    else:
        is_comment(line)
