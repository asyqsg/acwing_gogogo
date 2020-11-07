class Solution:
    def merge_sort(self,nums:list):
        size = len(nums)
        if size <= 1: return

        mid = size//2
        L = nums[:mid]
        R = nums[mid:]
        self.merge_sort(L)
        self.merge_sort(R)

        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] <= R[j]:
                nums[k] = L[i]
                i += 1
            else:
                nums[k] = R[j]
                j += 1
            k += 1
        while i < len(L):
            nums[k] = L[i]
            k+=1
            i+=1
        while j < len(R):
            nums[k] = R[j]
            k+=1
            j+=1
        return nums

if __name__ == '__main__':
    n = int(input())
    nums = list(map(int,input().split()))
    nums = Solution().merge_sort(nums)
    for i in nums:
        print(i,end = ' ')