# 1. 이름, 전화번호, 이메일 주소를 키로 사용하는 사전 자료를 생성 하시오.
dic = {'이름':'장우혁', '전화번호':'010-1234-1234', '이메일':'email@naver.com'}
#print(dic)

# 2. 리스트형 변수에 1번 문제와 같은 사전 자료가 여러 개 생성될 수 있도록 하시오.
phone_list = [] # 리스트형 변수
# 여러개 생성 -> 무한 루프
while True:
    name = input("이름 : ")
    phone = input("전화번호 : ")
    email = input("이메일 : ")
    phone_list.append({'이름':name, '전화번호':phone, '이메일':email})
    # 계속 입력할지 물어보기.
    if input("계속 할거냐(yes/no)") == "no":
        break
    
