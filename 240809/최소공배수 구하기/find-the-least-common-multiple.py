def gcd(n, m):
    while m != 0:
        n, m = m, n % m
    return n

def lcm(n, m):
    return (n * m) // gcd(n, m)

# 입력 받기
n, m = map(int, input().split())

# 최소공배수 계산 및 출력
print(lcm(n, m))