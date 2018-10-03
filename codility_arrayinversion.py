    A = [-1,6,3,4,7,4]
    lena = len(A)
    k = 0
    count = 0
    j = -1
    for i in range(lena-1, 0,-1):
        print('i : {}'.format(i))
        temp = A[i]
        ii=0
        j+=1
        kk = 0

        while ii < lena-1-j:
            print('Difference between {} and {} is {}'.format(temp, A[i-1-ii], temp - A[i-1-ii]))
            print('ii is {}'.format(ii))
            if temp - A[i-1-kk] < 0:
                count += 1
                if count > 1000000000:
                    print(-1)
            kk += 1
            ii += 1


    print(count)