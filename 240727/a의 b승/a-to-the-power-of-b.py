# 변수 선언 및 입력
a, b = map(int, input().split())
prod = 1

for i in range(b):
    prod*=a

print(prod)

'''
# 변수 선언 및 입력 방법2
1) inp를 한번에 받음 array 형태
inp = input()

2) array형태로 빈칸으로 쪼개고
arr = inp.split()

3) 0번이 a, 1번이 b
a = int(arr[0])
b = int(arr[1])

prod = 1

'''