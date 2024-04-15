# # 가장 많이 사용된 알파벳을 찾고 출력하기
# # 숫자가 같으면 "?" 출력 < 예외 처리
A = input().upper()
B = list(set(A)) # 순서가 다를 수 있다.
C= list()
cnt = 0
for i in B:
    for j in range(len(A)):
        if i == A[j]:
            cnt = cnt +1
    C.append(cnt)
    cnt=0

if C.count(max(C)) >= 2:
    print('?')
else:
    print(B[C.index(max(C))])
