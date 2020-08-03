#
# @lc app=leetcode.cn id=15 lang=python3
#
# [15] 三数之和
#

# @lc code=start
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        a, i = [], 0
        for i in range(len(nums) - 2):
            if nums[i] > 0: break
            if i > 0 and nums[i]==nums[i - 1]:continue
            l, r = i + 1, len(nums) - 1
            while l < r:
                c = nums[i] + nums[l] + nums[r]
                if c < 0: 
                    l += 1
                    while l < r and nums[l]==nums[l - 1]:l += 1
                elif c > 0: 
                    r -= 1
                    while l < r and nums[r]==nums[r + 1]:r -= 1
                else:
                    a.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l]==nums[l - 1]:l += 1
                    while l < r and nums[r]==nums[r + 1]:r -= 1
                   
        return a
        
# @lc code=end
