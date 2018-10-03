def solution(A):
    lena = len(A)
    As = sorted(A, reverse=True)
    print(As)
    prod = 1

    if As[0] == 0:
        prod = 0
    elif lena == 3:
        if 0 not in As:
            prod = As[0] * As[1] * As[2]
        else:
            prod = 0
    elif lena == 4:
        if As[2] > 0:
            prod = As[0]*As[1]*As[2]
        elif As[1] > 0 and 0 in As:
            prod = 0
        elif As[1] > 0:
            prod = max(As[0]*As[1]*As[2] , As[0],As[-1],As[-2])
        elif As[0] > 0:
            prod = As[0] * As[-1] * As[-2]

    elif lena > 4:
        if As[2] > 0:
            prod = max(As[0]*As[1]*As[2],As[0]*As[-1]*As[-2])
        else:
            prod = max(As[0]*As[1]*As[2], As[0],As[-1],As[-2])

    return prod
print(solution([0, -1,-22,-33]))