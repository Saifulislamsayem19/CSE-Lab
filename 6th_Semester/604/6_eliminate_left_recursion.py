
def rmv_left_recursion(p, n):
    c = 0
    for i in range(n):
        n_trmnl = p[i][0]
        for j in range(3, len(p[i])):
            if n_trmnl == p[i][j]:
                c += 1

        if c > 1 or '|' not in p[i]:
            p2 = p[i].split("|")
            for j in range(len(p2)):
                if j > 0:
                    for x in range(len(p2[j])):

                        if n_trmnl == p2[j][x]:
                            print(f"\n{n_trmnl}->{p2[j]} is left recursive.")
                            print("Grammar without left recursion:")
                            print(f"{n_trmnl}->{p2[j][0]}'")
                            print(f"{p2[j][0]}'->{p2[j][1:]}{n_trmnl}'|e")
                            break
                        else:
                            print(f"\n{n_trmnl}->{p2[j]} isn't left recursive.")
                            break
                else:
                    for x in range(3, len(p2[j])):
                        if n_trmnl == p2[j][x]:
                            print(f"\n{p2[j]} is left recursive.")
                            print("Grammar without left recursion:")
                            print(f"{n_trmnl}->{p2[j][3]}'")
                            print(f"{p2[j][3]}'->{p2[j][4:]}{n_trmnl}'|e")
                            break
                        else:
                            print(f"\n{p2[j]} isn't left recursive.")
                            break
        else:

            for j in range(3, len(p[i])):
                if n_trmnl == p[i][j]:
                    a = p[i][j + 1]
                    print(f"\n{p[i]} is left recursive.")
                    while p[i][j] != 0 and p[i][j] != '|':
                        j = j + 1
                    if p[i][j] != 0:
                        b = p[i][j + 1]
                        print("Grammar without left recursion:")
                        print(f"{n_trmnl}->{b}{n_trmnl}'")
                        print(f"{n_trmnl}'->{a}{b}{n_trmnl}'|e")
                        c = 0
                        break
                    else:
                        print(f"{p[i]} can't be reduced")
                        break
                else:
                    print(f"\n{p[i]} is not left recursive.")
                    break


rules = []
n = int(input("Enter number of production: "))
for _ in range(n):
    r = input()
    rules.append(r)

rmv_left_recursion(rules, n)

# S->AB
# A->Aa|B
# B->C

# E->E+T|T
# T->T*F|F
# F->E|id

# E->E+T|E*T
