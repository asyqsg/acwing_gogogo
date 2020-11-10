def quick_sort(nums:list,l:int,r:int):
    if l >= r: return

    flag_num = nums[r+l >> 1]
    i,j = l-1,r+1
    while i < j:
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

    quick_sort(nums,l,j)
    quick_sort(nums,j+1,r)

if __name__ == '__main__':
    n = int(input())
    nums = list(map(int,input().split()))
    l,r = 0,n-1
    quick_sort(nums,l,r)
    for i in nums:
        print(i,end=' ')