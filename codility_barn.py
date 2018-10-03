A= [1,2,5,1,1,2,3,5,1,20,10,10]
X = 20
counts = dict()
for i in A:
  counts[i] = counts.get(i, 0) + 1
print(counts)
S = set(A)
Amod = [i for i in S if counts[i] >= 2]
temp = 0
ii = len(Amod) - 1
j = -1
c = 0
print(Amod)

for i in range(0,len(Amod)-1):
    print('i is {}.'.format(i))
    temp = Amod[i]
    j+=1
    print('j is {}.'.format(j))
    ii = len(Amod) - 1
    jj = 0
    print(ii,0+j)
    while ii>0+j:
        print('ii = {}'.format(ii))
        if temp * Amod[i+1+jj] >= X:
            # print('Product of {} and {} is {}.'.format(temp,Amod[i+1+jj],temp * Amod[i+1+jj] ))
            c += 1
            if c > 1000000000:
                print(-1)
        jj += 1
        ii -= 1

print(c)