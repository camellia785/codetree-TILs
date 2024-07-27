# 입력된 문자열의 길이를 리스트에 저장
lengths = [len(input()), len(input()), len(input())]

# 리스트에서 최댓값과 최솟값을 구함
max_length = max(lengths)
min_length = min(lengths)

# 최댓값과 최솟값의 차이를 계산
result = max_length - min_length

# 결과 출력
print(result)


''' 
# 런타임 에러 뜬 코드
a = len(input())
b = len(input())
c = len(input())

if a>b:
    if b>c:
        result = a-c

    elif b<c:
        if a>c:
            result = a-b
        else:
            result = c-b

elif a<b:
    if a>c:
        result = b-c

    elif a<c:
        if b>c:
            result = b-a

        else:
            result = c-a
print(result)
'''