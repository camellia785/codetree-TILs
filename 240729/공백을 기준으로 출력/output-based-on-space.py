st1 = input()
st2 = input()

# 공백 제거
st1_no_space = st1.replace(" ", "")
st2_no_space = st2.replace(" ", "")

result = st1_no_space + st2_no_space
print(result)