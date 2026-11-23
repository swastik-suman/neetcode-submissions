class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        new_list=set(nums)
        l=0
        for i in new_list:
            if(i-1) not in new_list:
                le=1
                while (i+le)in new_list:
                    le+=1
                l=max(le,l)
        return l
             