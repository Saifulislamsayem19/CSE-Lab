#
def is_comment(line):
    if line[0] == "/" and line[1] == "/":
        print("Given line is single-line comment")
        return
    elif line[0] == "/" and line[1] == "*" and line[len(line)-3] == "*" and line[len(line)-2] == "/":
        print("Given line is multi-line comment")
        return
    else:
        print("Not a comment.")
        return


multi_line = ""
l = int(input("Enter number of line: "))
for i in range(l):
    line = input(f"Enter {i+1} line : ")
    multi_line += line + " "
print(multi_line)
is_comment(multi_line)

#

# with open("comments.txt",'w') as comments_file:
#     i = input("Enter a line:")
#     print(i, file=comments_file)
#     for line in comments_file:
#         print(line,file=comments_file)

#
# with open("comments.txt", 'r') as file:
#     multi_line = ""
#     lines = file.readlines()
#     for line in lines:
#         multi_line += line
#     print(multi_line)
#     is_comment(multi_line)
