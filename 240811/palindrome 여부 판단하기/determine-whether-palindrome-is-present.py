def is_palindrome(A):
    # 문자열을 뒤집은 것과 원래 문자열이 같은지 비교하기
    if A == A[::-1]:
        return "Yes"
    else:
        return "No"

# 입력받은 문자열
A = input()

# palindrome 여부 확인 및 출력
print(is_palindrome(A))