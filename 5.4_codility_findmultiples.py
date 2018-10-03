
def solution1(A,B,K):
    A_prime = (((A - 1)//K) + 1)*K
    return ((B-A_prime)//K) + 1

print(solution1(7,11,2))
