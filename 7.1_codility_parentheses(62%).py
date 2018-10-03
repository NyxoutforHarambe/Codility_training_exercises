brackets = '('*100000 + ')'*100000 +')('
S = brackets
Slist = [i for i in S]
# print(Slist)
br = ['(', ')', '{', '}', '[', ']', 'V', 'W']

stack = [0]*200010
global N
N = 0

def push(bracket):
    global N
    stack[N] = bracket
    N+=1

def pop():
    global N
    N-=1
    temp = stack[N] = 0
    stack[N] = 0
    return temp

for i in range(len(Slist)):
    print('stack[{}]: {}'.format(i,stack[i]))
    if (Slist[i] == br[0]):
        push(0)
    elif (Slist[i] == br[2]):
        push(2)
    elif (Slist[i] == br[4]):
        push(4)
    elif (Slist[i] == br[6]):
        push(6)
    else:
        if (Slist[i] == br[1]) and (stack[N-1] == 0):
            pop()
        elif (Slist[i] == br[3]) and (stack[N-1] == 2):
            pop()
        elif (Slist[i] == br[5]) and (stack[N-1] == 4):
            pop()
        elif (Slist[i] == br[7]) and (stack[N-1] == 6):
            pop()
        elif (Slist[i].isalnum() == True):
            continue
        else:
            print(0)
            break

print(1)


