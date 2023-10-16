class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        nums = sorted(nums)
        #since product can be of two positive or two negative integers
        return max(((nums[0]-1)*(nums[1]-1)), ((nums[-1]-1)*(nums[-2]-1)))