# 최대공약수 구하는 함수 : 유클리드 호제법:

def gcd(n,m):
    while m != 0:
        n, m = m, n%m
    return n


# 입력 받기
n, m = map(int, input().split())

print(gcd(n,m))