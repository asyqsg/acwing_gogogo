n,m = map(int,input().split())

nums = list(map(int,input().split()))

def insert(b,l,r,c):
    b[l] += c
    b[r+1] -= c

if __name__ == '__main__':
    a = [0] * (n+10)
    b = [0] * (n+10)
    for index,val in enumerate(nums):
        a[index+1] = val

    for i in range(1,n+1):
        insert(b,i,i,a[i])

    while m>0:
        m-=1
        l,r,c = map(int,input().split())
        insert(b,l,r,c)

    for i in range(1,n+1):
        b[i] += b[i-1]

    for i in range(1,n+1):
        print(b[i],end=' ')