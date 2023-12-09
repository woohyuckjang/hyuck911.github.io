'''
2. 숫자 추측 프로그램
컴퓨터 = 숫자
사용자 = 맞추기
1. 기본
- 1번만 정답 얘기하고 맞춤, 크다, 작다
2. 맞출때까지 반복
3. 시도횟수 제한
4. 점수 추가
5. 중간에 그만하는 기능
6. 3번안에 맞추면 점수를 더 주고
7. 시도횟수에 따라 점수를 차등주기
'''

com = 5
print("숫자 맞추기")
player = int(input("숫자 입력 : "))
if com == player: #같다
    print("player Win")
elif com > player: #com이 큼
    print("작다")
else:
    print("크다")
