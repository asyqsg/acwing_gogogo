n,q = list(map(int,input().split()))
nums = list(map(int,input().split()))
check_num = []
for i in range(q):
    check_num.append(int(input()))

def get_left_bound(nums,k):
    l,r = 0,len(nums)-1
    while l < r:
        mid = (l+r)//2
        if nums[mid] >= k:
            r = mid
        else:
            l = mid+1
    if nums[l] != k:
        return -1
    return l

def get_right_bound(nums,k):
    l,r = 0,len(nums)-1

    while l < r:
        mid = (l + r + 1) // 2
        if nums[mid] <= k:
            l = mid
        else:
            r = mid-1
    if nums[r] != k:
        return -1
    return r

if __name__ == '__main__':
    for i in check_num:
        r = get_right_bound(nums,i)
        l = get_left_bound(nums,i)
        for i in [l,r]:
            print(i,end=' ')
