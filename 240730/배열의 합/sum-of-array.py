# 4개의 줄에 걸쳐서 4개씩 숫자가 나옴

for _ in range(4):
    numbers = list(map(int, input().split()))
    total = sum(numbers)
    print(total)