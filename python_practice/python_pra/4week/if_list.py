# 리스트에 있는 숫자 찾기
s_list = [1,2,3,4,5]

s_find = int(input("찾을 숫자 입력 : "))

if s_find in s_list:
    print("입력 받은 수 : ", s_find,"리스트에 있다.")
else:
    print("리스트에 없다.")
