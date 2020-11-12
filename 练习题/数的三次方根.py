n = float(input())

def find(l,r):
    while r-l > 1e-8:
        mid = float((l+r)/2)
        if mid*mid*mid >= n:
            r = mid
        else:
            l = mid
    return l

l = find(-10000,10000)

#取6位小数的方法
print("{:.6f}".format(l))
