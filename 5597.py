# X대학 M교수님은 프로그래밍 수업을 맡고 있다. 교실엔 학생이 30명이 있는데, 학생 명부엔 각 학생별로 1번부터 30번까지 출석번호가 붙어 있다.
#
# 교수님이 내준 특별과제를 28명이 제출했는데, 그 중에서 제출 안 한 학생 2명의 출석번호를 구하는 프로그램을 작성하시오.

# 28개의 입력을 하고
# 그 입력에서 없는 숫자 2개를 확인 << 리스트로
# 2개에 대한 반환 이후, 작은 걸 순서대로

Student = [i for i in range(1,31)]
live= [0 for i in range(0,30)]
a=list()
for i in range(28):
    a.append(input())

# print(Student)
# print(live)
# print(a)

for j in range(0,30):
    for k in range(0,28):
        if Student[j]==int(a[k]):
            live[j]=1
            break
#
# print(live)
for l in range(0,30):
    if live[l]==0:
        print(l+1)

