import time

list_big = []
for i in range(1,10000):
    list_big.append(i)
list_big.reverse()
list_big.append(20000)
print(list_big)

start = time.time()
def solution(A):
    mini_arr = [i for i in sorted(A) if i>0]
    dic = {}
    for i in range(1, 1000000):
        if i in mini_arr:
            dic[i] = 1
        else:
            dic[i] = 0

    return {k:v for (k,v) in dict.items() if v == 1}



ans = solution(list_big)
end = time.time()
print(ans)
print("--- {:.9f} seconds ---".format(end-start))
