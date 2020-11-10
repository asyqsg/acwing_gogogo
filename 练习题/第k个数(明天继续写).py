n, k = map(int, input().split())
a = list(map(int, input().split()))

def quick_select(a, l, r, k):
    if l >= r:
        return a[l]
    x = a[l + r >> 1]
    i = l - 1
    j = r + 1
    while i < j:
        i += 1
        while a[i] < x:
            i += 1

        j -= 1
        while a[j] > x:
            j -= 1

        if i < j:
            a[i], a[j] = a[j], a[i]

    length = j - l + 1 # 左半区间的区间长度
    if k <= length:
        return quick_select(a, l, j, k)
    else:
        return quick_select(a, j+1, r, k-length)

res = quick_select(a, 0, n-1, k)
print(res)