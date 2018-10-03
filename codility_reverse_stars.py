import time

def tri(n):
    space = {}
    star = {}

    for i in range(1,n+1):
        space[i] = 2*(i-1)
        star[n-i+1] = 2*i-1
    for i in range(1,n+1):
        print(" "*space[i], end='')
        print("* "*star[i])
    return space, star

def tri2(n):
    space = {1:0}
    star = {1:2*n -1}

    for i in range(1,n+1):
        if i not in space:
            space[i] = space[i-1] + 2
        if i not in star:
            star[i] = star[i-1] - 2
    for i in range(1,n+1):
        print(" "*space[i], end='')
        print("* "*star[i])
    return space, star


start = time.time()
print(tri2(500))
stop = time.time()
print("Time taken is {}".format(stop-start))
