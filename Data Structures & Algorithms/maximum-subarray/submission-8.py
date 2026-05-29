class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # in the subarray: stop now, include
        # not in the subarray: skip, start
        def helper(i:int, flag:bool)->int:
            if i == len(nums)-1:
                if flag: # we are in the subarray
                    return max(0, nums[i]) #include
                else: #not in the subarray we must get
                    return nums[i]
            if not flag:
                return max(helper(i+1, False), nums[i]+helper(i+1,True))
            if flag:
                return max(0, nums[i]+helper(i+1, True))

        return helper(0,False)

# [-5,8,-3,9]



