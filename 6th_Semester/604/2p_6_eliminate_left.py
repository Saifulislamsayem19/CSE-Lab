
def rmv_left_recursion(p,n):

    for i in range(n):
        non_terminal=p[i][0]
        for j in range(3,len(p[i])):
            if non_terminal == p[i][j]:
                alpha = p[i][j+1]
                print(f"\n{p[i]} is left recursive.")
                while p[i][j] != 0 and p[i][j] != '|':
                    j = j + 1
                if p[i][j] != 0:
                    beta=p[i][j+1]
                    print("Grammar without left recursion:")
                    print(f"{non_terminal}->{beta}{non_terminal}'")
                    print(f"{non_terminal}'->{alpha}{beta}{non_terminal}'|e")
                    break
                else:
                    print(f"{p[i]} can't be reduced")
                    break
            else:
                print(f"\n{p[i]} is not left recursive.")
                break


production = []
num = int(input("Enter Number of Production : "))
print("Enter Rules:")
for i in range(num):
    rules = input()
    production.append(rules)

rmv_left_recursion(production, num)
