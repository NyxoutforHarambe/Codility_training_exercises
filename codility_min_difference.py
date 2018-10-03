A = [3,1,2,4,3]
lena = len(A)
total = sum(A)
print('total : {}'.format(total))
temp = 0
second_half = 0
mini = 1000000
diff = 0

for i in range(0, lena-1):
    temp += A[i]
    second_half = total - temp
    diff = abs(temp - second_half)
    print(diff)
    if diff < mini:
        mini = diff

print(mini)

