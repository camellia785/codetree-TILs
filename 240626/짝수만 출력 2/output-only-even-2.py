# a, b = map(int, input().split())
# i = a

# while i >= b:
#     if i % 2 ==0:
#         print(i, end=' ')
#     i-=1


# 변수 선언, 입력
inp = input()
arr = inp.split()
b = int(arr[0])
a = int(arr[1])
i = b

# 출력
while i >= a:
	print(i, end=" ")
	i -= 2