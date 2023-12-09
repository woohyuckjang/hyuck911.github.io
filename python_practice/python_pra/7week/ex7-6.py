# 교재 P200 7-6
'''
1   2   3    4
5   6   7    8
9 10  11  12

'''
list1=[]
list2=[]
value=1
for i in range(0,3):
    for k in range(0,4):
        list1.append(value)
        value += 1
    list2.append(list1)
    list1=[]

for i in range(0,3):
    for k in range(0,4):
        print("%3d"%list2[i][k], end="")
    print("")
