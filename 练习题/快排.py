def quick_sort(q,l,r):
    if l>=r:
        return
    x = q[(l+r)//2]
    i,j = l-1,r+1
    while(i<j):
        while True:
            i+=1
            if q[i]>=x:
                break
        while True:
            j-=1
            if q[j] <=x:
                break
        if i < j:
            q[i],q[j]=q[j],q[i]

    quick_sort(q,l,j)
    quick_sort(q,j+1,r)

if __name__ == '__main__':
    n = int(input())
    alist = list(map(int,input().split()))
    quick_sort(alist,0,n-1)
    for i in alist:
        print(i,end = ' ')