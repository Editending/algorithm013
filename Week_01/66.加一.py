#
# @lc app=leetcode.cn id=66 lang=python3
#
# [66] 加一
#

# @lc code=start
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        res = 0
        for i in digits:
            res = res * 10 + i
        return [int(j) for j in str(res + 1)]
    

# @lc code=end
