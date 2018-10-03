
def solution(A):
    dic = {}
    for i in range(len(A)):
        if A[i] in dic:
            del dic[A[i]]
        else:
            dic[A[i]] = 1

    for k,v in dic.items():
        ans = k

    return ans

print(solution([1,1,2,2,3,4,3]))
