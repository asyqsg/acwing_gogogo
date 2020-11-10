def merge_sort(nums):
    size = len(nums)
    if size < 2: return
    l,r = 0,size-1
    mid = [l+r >> 1]
    L = nums[:mid]
    R = nums[mid:]
    merge_sort(L)
    merge_sort(R)

    i,j,k = 0,0,0
    while i < len(L) and j < len(R):
        if L[i] < R[j]:
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
        k+=1
        j+=1
    return nums 
