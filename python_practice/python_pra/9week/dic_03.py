# 2. 리스트형 변수에 1번 문제와 같은 사전 자료가 여러 개 생성될 수 있도록 하시오.
# 3. 2번에서 입력한 자료가 출력 될 수 있도록 하시오.
phone_list = [] # 리스트형 변수
# 여러개 생성 -> 무한 루프
while True:
    name = input("이름 : ")
    phone = input("전화번호 : ")
    email = input("이메일 : ")
    phone_list.append({'이름':name, '전화번호':phone, '이메일':email})
    # 계속 입력할지 물어보기.
    if input("계속 할거냐(yes/no) : ") == "no":
        break
    # 입력한 내용 출력하기.
    if input("지금까지 입력한 내용을 확인할거냐?(yes/no) : ") == "yes":
        # 출력하기
        for values in phone_list: # 리스트에 있는 자료를 하나씩 values에 할당
            # 할당한 자료가 사전자료형
            for key, value in values.items():
                print("{} : {}".format(key,value))
