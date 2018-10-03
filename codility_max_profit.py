A = [23171, 21011, 21123, 21366,21013,21367]
As = sorted(A, reverse=True)
print(As)

pl = []
max = 0
difference = 0
for i in range(len(A)-1):
    print('i : {}'.format(i))
    j = len(A)
    while j>(i+1):
        print('j : {}'.format(j))
        difference = As[i] - As[i+1 +len(A)-j]
        index1 = A.index(As[i])
        index2 = A.index(As[i+1 +len(A)-j])
        pl.append(difference)

        if (difference > max) and (index1>index2):
            max = difference
        j-=1

print(max)