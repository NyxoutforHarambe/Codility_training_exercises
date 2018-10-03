    if (A[i].x >= 0 and A[i].y >= 0):
        slope = A[i].y / A[i].x
        if slope in m1:
            no_rays -= 1
        else:
            m1.append(slope)
    elif (A[i].x <= 0 and A[i].y <= 0):
        slope = A[i].y / A[i].x
        if slope in m3:
            no_rays -= 1
        else:
            m3.append(slope)

    elif (A[i].x >= 0 and A[i].y <= 0):
        slope = A[i].y / A[i].x
        if slope in m4:
            no_rays -= 1
        else:
            m4.append(slope)

    elif (A[i].x <= 0 and A[i].y >= 0):
        slope = A[i].y / A[i].x
        if slope in m2:
            no_rays -= 1
        else:
            m2.append(slope)