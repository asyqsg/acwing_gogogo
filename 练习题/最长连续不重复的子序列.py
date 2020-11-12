class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        def check(my_list:list,num):
            nonlocal max_lenght
            if num in my_list:
                index = my_list.index(num)
                my_list = my_list[index+1:]
            my_list.append(num)
            max_lenght = max(max_lenght,len(my_list))
            return my_list
        my_list = []
        max_lenght = 0
        for i in s:
            my_list = check(my_list,i)
        return max_lenght



if __name__ == '__main__':
    print(Solution().lengthOfLongestSubstring('aav'))