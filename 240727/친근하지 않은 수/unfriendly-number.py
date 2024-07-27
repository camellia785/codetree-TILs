# 입력
n = int(input())

# 친근하지 않은 수의 개수를 세기 위한 변수
unfriendly_count = 0

# 1부터 n까지 반복합니다.
for i in range(1, n + 1):
    # i가 2, 3 또는 5로 나누어 떨어지는 경우 친근한 수입니다.
    if i % 2 == 0 or i % 3 == 0 or i % 5 == 0:
        continue  # 친근한 수인 경우 다음 반복으로 건너뜁니다.
    
    # 친근하지 않은 수인 경우 카운트를 증가시킵니다.
    unfriendly_count += 1

# 친근하지 않은 수의 개수를 출력
print(unfriendly_count)