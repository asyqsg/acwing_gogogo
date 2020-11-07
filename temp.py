n = int(input())
list1 = list(map(int, input().split()))

def merge_sort(list1):
    if len(list1) <= 1:
        return
    mid = len(list1) // 2
    L = list1[:mid]
    R = list1[mid:]
    merge_sort(L)
    merge_sort(R)

    i = j = k = 0
    while i < len(L) and j < len(R):
        if L[i] <= R[j]:
            list1[k] = L[i]
            i += 1
        else:
            list1[k] = R[j]
            j += 1
        k += 1
    while i < len(L):
        list1[k] = L[i]
        k += 1
        i += 1
    while j < len(R):
        list1[k] = R[j]
        k += 1
        j += 1

def quick_sort(nums:list,l,r):
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
        quick_sort(nums,l,j+1)
        quick_sort(nums,j+1,r)
        return nums

if __name__ == "__main__":
    merge_sort(list1)
    for i in list1:
        print(i, end=" ")

