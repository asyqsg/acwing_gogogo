'''
acwing 快排
'''
import sys
data = sys.stdin.readline().strip()
data = data.split()
data = list(map(int,data))

class Sort:
    def quick_sort_more(self,nums:list):
        '''
        快排需要额外的内存空间   不推荐但是好理解
        :param nums: 输入的list
        :return:   返回排序完成的list
        '''
        if len(nums) < 2:
            return nums

        mid = nums[len(nums)//2]
        left,right = [],[]
        nums.remove(mid)
        for item in nums:
            if item >= mid:
                right.append(item)
            else:
                left.append(item)
        return self.quick_sort_more(left) + [mid] + self.quick_sort_more(right)

    def quick_sort_recommand(self,nums:list,l_index,r_index):
        #根据acwing推荐算法
        if l_index >= r_index: return   #注意！！！！！

        flag_num = nums[l_index]
        i = l_index-1
        j = r_index+1
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
        # nums[l] = flag_num
        self.quick_sort_recommand(nums,l_index,j)
        self.quick_sort_recommand(nums,j+1,r_index)
        return nums

    def merge_sort(self,list1):
        #归并排序
        if len(list1) <= 1:
            return
        mid = len(list1) // 2
        L = list1[:mid]
        R = list1[mid:]
        self.merge_sort(L)
        self.merge_sort(R)

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

        return list1




if __name__ == '__main__':
    size = len(data)
    l,r = 0,len(data)-1
    print(Sort().quick_sort_recommand(data,l,r))
    print(Sort().quick_sort_more(data))
    # # print(Sort().merge_sort(data))
    # Sort().merge_sort(data)
    # print(data)
    #