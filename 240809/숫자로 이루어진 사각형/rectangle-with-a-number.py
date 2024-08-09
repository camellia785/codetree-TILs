def print_square(N):
    current_number = 1
    for i in range(N):
        row = []
        for j in range(N):
            row.append(current_number)
            current_number += 1
            if current_number > 9:
                current_number = 1
        print(' '.join(map(str, row)))

# 예제 입력
N = int(input())

# 함수 호출 및 출력
print_square(N)