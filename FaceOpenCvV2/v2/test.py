import numpy as np
a=[False,False,False, False]
b=np.array([2,5,1,7])

check = True
while True:
    minIndex=np.argmin(b)
    if a[minIndex]:
        print('vi tri be nhat tai ',minIndex)
        break
    elif len(a)==1:
        break
    else:
        a.pop(minIndex)
        b.pop(minIndex)
        