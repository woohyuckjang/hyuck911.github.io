# f_list 이름의 리스트에
# 5개의 데이터를 넣는 프로그램 작성
print("-"*25)
print("      2021136114-장우혁")
print("-"*25)

f_list = [] # F리스트 선언
for i in range(5):
    name = input("이름 입력 : ")
    f_list.append(name)
print("%s"%f_list)
