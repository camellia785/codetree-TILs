# 5행이고 3열의 배열

for _ in range(5):
    lower_alpha = input().split()
    
    # 리스트로 감싸기
    upper_alpha = [alpha.upper() for alpha in lower_alpha]

    # 공백을 사이에 두고 출력하는 법
    print(' '.join(upper_alpha))