def solution(A):
    As = sorted(A)
    for i in range(len(As)):
        if As[i] != (i + 1):
            return 0
    return 1

print(solution([4,1,3,2,3]))