S = ''
Sl = [i for i in S]
Slen = len(S)
print(Slen)
index = Slen//2
if Slen %2 == 0:
    print(-1)
elif Slen ==  1:
    print(0)

for i in range(index):
    if Sl[i] == Sl[-(i+1)]:
        continue
    else:
        print(-1)
print(Sl[index])