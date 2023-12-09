# 사용자가 숫자를 여러 개 입력하면 하트 모양을 입력한 숫자만큼 출력하는 프로그램


# 반복문에 사용할 변수와 하트 개수를 세는 변수 선언
i, k, heartNum = 0, 0, 0
#i=k=heartNum=0
#i=0;k=0;heart=0

# 입력받을 숫자를 저장할 numStr, 하트를 저장할 heartStr, 1개씩 분리한 숫자를 저장할 ch 선언
numStr, ch, heartStr = "","",""

if __name__ == "__main__" : #환경변수. 메인이면 실행
    numStr = input("숫자를 여러개 입력하세요 : ")
    print("")
    i = 0
    ch = numStr[i] # ch에 입력한 숫자 1개씩 저장
    
    # 무한 반복
    while True :
        heartNum = int(ch) # ch에 저장된 숫자를 heartNum에 저장

        heartStr = ""
        for k in range(0, heartNum) : # 하트의 개수만큼 반복
            heartStr += "\u2665" # 하트의 개수만큼 반복하면서 하트(\u2665)를 hearStr에 누적
            k += 1

        print(heartStr) # 하트 출력

        i += 1
        if (i > len(numStr) -1 ) :
            break

        ch = numStr[i]
