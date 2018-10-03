def solution(A, K):

    max_index = len(A)

    try:
        for i in range(K):
            temp = A[-1]
            for j in range(max_index - 1, 0, -1):
                A[j] = A[j - 1]
            A[0] = temp
    except IndexError:
        print('Oops !')
    return A

print(solution([], 3))