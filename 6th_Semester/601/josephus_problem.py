
def josephus(N, K):
    if N == 1:
        print(f'Survival for {N} is {N}')
        return 1

    else:
        r = ((josephus(N - 1, K) + K - 1) % N + 1)
        print(f'Survival for {N} is {r}')
        return r

# def findTheWinner(n, k):
#
#     return winner(n, k) + 1
#
#
# def winner(n, k):
#
#     if n == 1:
#         return 0
#     print(f'Survival for {n} is {((winner(n - 1, k) + k) % n)}')
#     return (winner(n - 1, k) + k) % n


p, k = int(input("Enter number of people: ")), int(input("Enter number of kill: "))
print(f'Survival is: {josephus(p, k)}')
