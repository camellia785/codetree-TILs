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
print(avg)