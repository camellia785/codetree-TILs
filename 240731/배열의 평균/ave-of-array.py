# 입력을 받습니다.
row1 = list(map(int, input().split()))
row2 = list(map(int, input().split()))

# 가로 평균_받은대로 
row1_avg = sum(row1)/4
row2_age = sum(row2)/4
print(row1_avg, row2_age)

# 세로 평균
i = 0
for i in range(4):
    length_avg = (row1[i]+row2[i])/2
    print(length_avg, end=' ')
print("")

avg = (sum(row1)+sum(row2)) / 8
print(f'{avg:.1f}')

''' 
# 해설
# 2차원 배열을 구현해 각 줄마다 정수를 입력받습니다.
arr_2d = [
	list(map(int, input().split()))
	for _ in range(2)
]

# 가로 평균을 출력합니다.
for i in range(2):
	sum_val = 0
	for j in range(4):
		sum_val += arr_2d[i][j]
	print(f"{sum_val / 4:.1f}", end=" ")
print()

# 세로 평균을 출력합니다.
for j in range(4):
	sum_val = 0
	for i in range(2):
		sum_val += arr_2d[i][j]
	print(f"{sum_val / 2:.1f}", end=" ")
print()

# 전체 평균을 출력합니다.
sum_val = 0
for i in range(4):
	for j in range(2):
		sum_val += arr_2d[j][i]
print(f"{sum_val / 8:.1f}")

'''