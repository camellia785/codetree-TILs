'''
소수점을 수학적으로 구하는 방법은
a를 b로 나눈 나머지에 10을 곱한 값을 b로 나눴을때의 몫을
순서대로 적는 것을 계속 반복하면 된다.

format 함수만으로는 소수점 20번째까지의 값을 
올바르게 구할 수 없음
'''

# 변수 선언
a, b = map(int, input().split())

# 정수 부분 먼저 출력
print(f'{a//b}.', end="")

# a를 b로 나눈 나머지를 시작으로
# 소수점 자리를 하나씩 계산
a %= b
# a = a % b

for _ in range(20):
    # 나머지에 10을 곱한 값을 기준으로
    # b를 나누었을때의 몫을 구함
    a *= 10
    print(a//b, end="")

    #a를 b로 나눈 나머지 갱신
    a %= b