# (1) change라는 함수를 이용해서 불러오기
n, m = map(int, (input().split()))

def change(n,m):
    n, m = m, n
    print(n,m)

change(n,m)

'''
# (2) tuple 형태로 받고 실행

# 변수 선언 및 입력:
n, m = tuple(map(int, input().split()))


def swap(n, m):
    n, m = m, n
    return n, m


n, m = swap(n, m)
print(n, m)
'''