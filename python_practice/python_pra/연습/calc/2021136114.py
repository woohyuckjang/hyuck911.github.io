# input() 함수로 입력 받은 더하기, 빼기, 곱하기, 나누기의 간단한 수식을
# 처리 할 수 있도록 코드를 작성하시오.
calc_list = [] # 리스트 형 변수
# 무한 루프
while True: 
    calc = input("수식 입력(예: 2+5) : ")
    result = eval(calc)
    calc_list.append({'입력한 수식':calc, '입력한 수식에 대한 결과':result}) # 입력한 수식 및 결과
    # 계속 진행 여부
    if input("계속 진행(yes/no) : ") == "no":
        break
    # 입력 내용 출력
    if input("지금까지 입력한 내용 확인(yes/no) : ") == "yes":
        for values in calc_list: # 리스트에 있는 자료 하나씩 values에 할당
            for key, value in values.items():
                print("{} : {}".format(key, value))
