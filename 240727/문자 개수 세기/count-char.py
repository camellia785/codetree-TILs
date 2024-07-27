str1= input()
alpha = input()

k = len(str1)
i = 0
count = 0

for i in range(k):
    if alpha in str1[i]:
        count += 1

print(count)

'''
# 해설 풀이

# 공백을 포함한 문자열을 입력받습니다.
string = input()

# 소문자 알파벳을 입력받습니다.
a = input()
cnt = 0

# 문자열에서 주어진 알파벳이 몇번 나오는지 확인합니다.
for elem in string:
	if elem == a:
		cnt += 1

# 주어진 알파벳이 나온 횟수를 출력합니다.
print(cnt)
'''