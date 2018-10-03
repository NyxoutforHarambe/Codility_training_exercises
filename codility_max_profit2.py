A = [23171, 21011, 21123, 21366,21013,21367]
pl = []
max = 0
difference = 0
for i in range(len(A)-1):
    print('i : {}'.format(i))
    j = len(A)
    while j>(i+1):
        print('j : {}'.format(j))
        difference = A[i+1 +len(A)-j]-A[i]

        pl.append(difference)

        if (difference > max):
            max = difference
        j-=1

print(max)