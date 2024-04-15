#카이사르 Password

A = str(input().upper())
B = list()
for i in range(len(A)):
    if 65<=ord(A[i])<=67:
        B.append(ord(A[i])+23)
    else:
        B.append(ord(A[i])-3)
# print(B)

for j in range(len(A)):
    print(chr(B[j]),end='')
