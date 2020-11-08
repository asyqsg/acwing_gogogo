def find_k(nums:list,l,r,k):
    if l >= r: return nums[r]

    flag_num = nums[(l+r)//2]
    i,j = l-1,r+1
    while i<j:
        while True:
            i+=1
            if nums[i] >= flag_num:
                break
        while True:
            j-=1
            if nums[j] <= flag_num:
                break
        if i < j:
            nums[i],nums[j] = nums[j],nums[i]

        Sl = j-l+1
        if k <= Sl:
            return find_k(nums,l,j,k)
        else:
            k = k-Sl
            return find_k(nums,j+1,r,k)

if __name__ == '__main__':
    temp = list(map(int,input().split()))
    n = temp[0]
    k = temp[1]
    if k > n: print(None)
    nums = list(map(int,input().split()))
    print(find_k(nums,0,n-1,k))
