st1 = input()
st2 = input()

# 공백 제거
st1_no_space = st1.replace(" ", "")
st2_no_space = st2.replace(" ", "")

result = st1_no_space + st2_no_space
print(result)

'''
# 문자열을 전부 순회하며 공백을 제외한 모든 문자를 출력하는 방법
for elem in string:
	if elem != " ":
		print(elem, end="")

for elem in string2:
	if elem != " ":
		print(elem, end="")
'''