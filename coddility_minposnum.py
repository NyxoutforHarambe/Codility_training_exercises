# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    A_sort = sorted(A)
    Apos = [i for i in A_sort if i > 0]
    offset = 0
    print(Apos)

    for i in range(len(Apos)):
        if Apos[0] != 1:
            return 1
        if (Apos[i]- (i+1))-offset > 0:
            return Apos[i-1]+1
        elif i+1 >Apos[i]-offset:
            offset -= 1


    if not Apos:
        return 1
    else:
        return Apos[-1] + 1


print(solution([-99,100000,7772828,92920,0,35000,2,3,4,5,6,67,8,89,2323]))