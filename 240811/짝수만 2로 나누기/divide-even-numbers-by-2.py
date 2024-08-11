N = int(input())  # 입력받은 값을 정수로 변환
N_list = list(map(int, input().split())) # 입력받은 문자열을 리스트로 변환

def magic_function(N, N_list):
    for i in range(N):
        N_list[i] = int(N_list[i])  # 문자열을 정수로 변환
        if N_list[i] % 2 == 0:  # 짝수인지 확인
            N_list[i] = N_list[i] // 2  # 짝수라면 값을 2로 나눈 값으로 변경
        else:
            pass

    # 리스트의 각 요소를 문자열로 변환하고, 공백으로 구분하여 출력
    print(" ".join(map(str, N_list)))  

magic_function(N, N_list)