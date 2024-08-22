def can_form_same_word(word1, word2):
    # 두 단어를 정렬하여 비교
    if sorted(word1) == sorted(word2):
        return "Yes"
    else:
        return "No"

# 입력을 받습니다.
word1 = input().strip()
word2 = input().strip()

# 결과 출력
print(can_form_same_word(word1, word2))