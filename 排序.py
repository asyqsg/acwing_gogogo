def quick_sort(nums,l,r):
    if l >= r: return
    
    flag_num = nums[l]
    i = l-1
    j = r+1
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
    return nums

def merge_sort(nums):
    size = len(nums)
    mid = size//2
    L = nums[:mid]
    R = nums[mid:]
    merge_sort(L)
    merge_sort(R)
    
    i,j,k =0,0,0
    while i < len(L) and j < len(R):
        if L[i] <= R[j]:
            nums[k] = L[i]
            i+=1
        else:
            nums[k] = R[j]
            j+=1
        k+=1
    while i < len(L):
        nums[k] = L[i]
        i+=1
        k+=1
    while j < len(R):
        nums[k] = R[j]
        j+=1
        k+=1
    
    return nums