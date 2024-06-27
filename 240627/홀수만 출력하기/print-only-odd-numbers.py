N = int(input())

for i in range(1, N+1):
    n = int(input())

    if (n%2 != 0) and (n%3==0):
        print(n)