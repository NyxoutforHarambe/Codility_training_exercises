A = [0,1]
lena = len(A)
# dic= {j:A[j] for j in range(lena)}
# print(dic)
count = 0
temp = 0
for i in range(lena):
    if A[i] == 0:
        temp += 1
    else:
        count += temp
    print('At end of loop {}, the value of temp is {} and value of count is {}.'.format(i, temp, count))

