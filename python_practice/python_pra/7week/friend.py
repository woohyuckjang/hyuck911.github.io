# 아래의 구성과 같은 메뉴를 만들고 친구이름을 관리하는 코드를 작성하시오.
# 리스트 이용할 것
'''
--------------------
1. 친구 리스트 출력
2. 친구 추가
3. 친구 삭제
4. 이름 변경
0. 종료
메뉴를 선택하시오 : 2
이름을 입력하시오 : 
--------------------
'''
friend=[]
menu = 1 #0은 종료
while menu!=0 :
    print("-"*40)
    print("친구 이름 관리-2021136114-장우혁")
    print("-"*40)
    print("1. 친구 리스트 출력")
    print("2. 친구 추가")
    print("3 친구 삭제")
    print("4. 이름 변경")
    print("0. 종료")
    menu=int(input("메뉴를 선택하시오 : "))

    if menu==1: #친구 리스트 출력
        print(friend)
    elif menu==2: # 친구 추가 append()
        name=input("이름을 입력하세요 : ")
        friend.append(name)
    elif menu==3: # 친구 삭제 remove()
        delName=input("지울 이름을 입력하세요 : ")
        if delName in friend:
            friend.remove(delName)
        else:
            print(delName,"은 친구 리스트에 없습니다.")
    elif menu==4: # 이름 변경
        oldName = input("지울 이름을 입력하세요 : ")
        if oldName in friend: # 지울 이름이 친구 리스트에 있으면
                                   # 지울 이름의 인덱스를 찾아아서 지우기
            idx=friend.index(oldName)
            newName=input("새 이름을 입력하세요 : ")
            friend[idx]=newName
        else:
            print(oldName, "은 친구리스트에 없습니다.")
        











    
        
