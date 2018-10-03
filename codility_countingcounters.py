# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N, A):
    lena = len(A)
    counters = [0] * N
    max_count = 0
    for i in range(lena):
        if A[i] >= 1 and A[i] <= N:
            counters[A[i] - 1] += 1
            if counters[A[i] - 1] > max_count:
                max_count = counters[A[i] - 1]
            print(counters)
        elif A[i] == N + 1:
            counters = [max_count]*N
            print(counters)
        else:
            raise Exception("Enter correct values")

    return counters

solution(5,[3,4,4,6,1,4,4])