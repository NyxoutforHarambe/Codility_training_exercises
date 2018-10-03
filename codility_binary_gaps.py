def solution(N):
    N_bin = bin(N)[2:]

    N_list = list(N_bin)
    N_int=[int(i) for i in N_list]
    print(N_int)

    count = 0
    max_count = 0
    for i in range(1,len(N_int)):
        if N_int[i] == 0 or N_int[i] < N_int[i-1]: # for 00, 10
                  count += 1

        else:
            if count > max_count:
                max_count = count
            count = 0

    return max_count

print("solution is : {}".format(solution(32)))