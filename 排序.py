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
        i = l_index
        j = r_index
        while i < j:
            while nums[i] < flag_num:
                i+=1
            while nums[j] > flag_num:
                j-=1
            if i < j:
                nums[i],nums[j] = nums[j],nums[i]
                i+=1
                j-=1
        self.quick_sort_recommand(nums,l_index,j)
        self.quick_sort_recommand(nums,j+1,r_index)
        return nums

    def guibin_sort(self):
        #归并排序
        


if __name__ == '__main__':
    size = len(data)
    l,r = 0,len(data)-1
    print(Sort().quick_sort_recommand(data,l,r))
    print(Sort().quick_sort_more(data))