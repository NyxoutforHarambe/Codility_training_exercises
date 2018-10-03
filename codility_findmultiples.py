def ismultiple(N, M):
    return N%M == 0

def solution(A,B,K):
    count = len([i for i in range(A, B+1) if ismultiple(i,K)])
    return count

def solution2(A,B,K):
    A_prime = (((A - 1)//K) + 1)*K
    return ((B-A_prime)//K) + 1


def solution3(A,B,K):
    count = 0
    temp = 0
    if A%K == 0:
        count+=1
        temp = A
    else:
        temp = A + A%K
        if temp > B:
            return 0
        else:
            count+=1

    count+= (B-temp)//K
    return count




print(solution2(7,11,2))