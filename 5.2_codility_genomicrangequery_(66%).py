S = 'CAGCCTA'
P = [2,5,0]
Q = [4,5,6]
dic = {'A':1, 'C':2, 'G':3, 'T':4}

Slist = [i for i in S]
w_array = [0] * len(P)

# for i in range(len(P)):
#     mw = 4
#     for k in range((Q[i] - P[i])+1):
#         print('In iteration {}{} - For nucleotide {} weight is {}'.format(i,k, Slist[P[i]+k], mw))
#         if (dic[str(Slist[P[i] + k])]) < mw:
#             mw = dic[str(Slist[P[i] + k])]
#         if mw == 1:
#             break
#
#     w_array[i] = mw
temp = []
for i in range(len(P)):
    temp = sorted(S[P[i] : Q[i]+1])
    w = dic[temp[0]]
    print(temp)
    print(w)

print(w_array)
