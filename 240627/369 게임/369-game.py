n = int(input())

for i in range(1, n+1):
    # 3의 배수일때
    if (i % 3 == 0):
        print(0, end=' ')

    # 숫자에 3, 6, 9 중 하나라도 들어가있을때
    # i라는 숫자를 10으로 나누고 각 자리의 숫자를 파악한 다음
    # 3, 6, 9 나뉘어지면 이제 0프린트
    
    elif (i // 10) in {3, 6, 9} or (i % 10) in {3, 6, 9}:
        print(0, end=' ')
        
    else:
        print(i, end=' ')