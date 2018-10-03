def solution(X,Y,D):
    count = 0
    while True:
        if X==Y:
            break
        else:
            count += 1
            X += D
            if(X >= Y):
                break

    return count
print(solution(10,100,5))

def solution2(X,Y,D):
    if (Y-X)%D == 0:
        count = (Y-X)//D
    else:
        count = ((Y-X)//D) + 1
    return count
print('Output of solution2 : {}'.format(solution2(10,100,5)))


import time
def benchmark(N):
    start = time.time()
    for i in range(N):
        solution(10,100,5)
    stop = time.time()
    print('Time taken was {} seconds !'.format(stop-start))
    return
benchmark(100000)

def benchmark(N):
    start = time.time()
    for i in range(N):
        solution2(10,100,5)
    stop = time.time()
    print('Time taken for solution 2 was {} seconds !'.format(stop-start))
    return
benchmark(100000)