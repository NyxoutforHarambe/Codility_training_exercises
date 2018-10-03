def solution(A):
    try:
        A_s = sorted(A)

    except Exception:
        print('enter array of more than 2 integers')
    else:
        i = A_s[0]
        ans = 0

        for j in A_s[1:]:
            if j < i + 2:
                i = j
            else:
                ans = i + 1
        return ans


print(solution([1,2,4]))
