## (1) 최소공배수, 최대공약수 공식으로 푸는 방법

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

'''
## (2) 최소공배수를 구하는 과정 그자체로 하기
# 변수 선언 및 입력:
n, m = tuple(map(int, input().split()))

# n과 m의 최소공배수를 출력합니다.
# 최소공배수 = a*b/(a랑 b의 최대공약수)

def find_lcm(n, m):
    gcd = 0
    for i in range(1, min(n, m) + 1):
        if n % i == 0 and m % i == 0:
            gcd = i

    print(n * m // gcd)
   

find_lcm(n, m)
'''