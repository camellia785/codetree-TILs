n = int(input())
sum = 0


for _ in range(n):
    number = int(input())
    sum += number

# 소수점 첫째 자리까지 출력하기 위해서는 round() 함수 사용!! 
avg = sum/n
avg_rounded = round(avg, 1)

print(sum, avg_rounded)