
grammer = input('Enter the grammar: ')
lhs = grammer[0]
f = grammer[3:]
rhs = f.split('|')

grammar = {lhs: rhs}


def minimum_matched_string(a, b, len_a, len_b):
    if len_a == 0 or len_b == 0:
        return 0
    elif a[len_a - 1] == b[len_b - 1]:
        return 1 + minimum_matched_string(a, b, len_a - 1, len_b - 1)
    else:
        return max(minimum_matched_string(a, b, len_a, len_b - 1), minimum_matched_string(a, b, len_a - 1, len_b))


length = 1000
for key in grammar.copy():
    item = grammar[key]
    for i in range(0, len(item) - 1):
        for j in range(i, len(item)):
            if i != j:
                # print(item[i], item[j], len(item[i]), len(item[j]))
                l = minimum_matched_string(item[i], item[j], len(item[i]), len(item[j]))
                if l > 0:
                    if length > l:
                        length = l

exp2 = []
if length > 0:
    common_val = grammar[key][0][:length]
    for i in range(len(grammar[key])):
        if common_val in grammar[key][i]:
            grammar[key][i] = grammar[key][i][length:]
            exp2.append(grammar[key][i])
            grammar[key][i] = ''

exp1 = grammar[key]
for i in range(len(exp1)):
    if '' in exp1:
        exp1.remove('')

exp1.append(common_val + f"{lhs}'")

for i in exp2:
    if i == '':
        ind = exp2.index(i)
        exp2[ind] = 'ε'

fi = f' {lhs}->'
fii = f" {lhs}'->"
# print(exp1)
for i in exp1:
    fi += i + '|'

for i in exp2:
    fii += i + '|'

fi = fi[:-1]
fii = fii[:-1]

print(fi)
print(fii)

# S->iEtS|iEtSeS|a
# A->aab|aac|aaaf|d
