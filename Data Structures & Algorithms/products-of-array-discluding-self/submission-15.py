class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # 1st pass
        res = [0]*len(nums)

        left = []
        cur_num = 1
        for num in nums:
            left.append(cur_num)
            cur_num *= num
        
        # Second pass
        cur_product = 1
        for i in range(len(nums)-1,-1,-1):
            res[i] = left[i]*cur_product
            cur_product *= nums[i]
        return res


    #     # 0 messes everything
    #     [1,2,4,6] --> [48,24,12,8]

    #     [-1,0,1,2,3] --> [0,-6,0,0,0]

    #     # Method 1 using division:
    #     Two pass: O(N)

    #     # Method 2: not using division
    #     cur_product = 1
    #     product of everything to the right * product of everything to the left

    #     [1,2,4,6]

    # left --> [1,1,2,8]
    # right --> [48,24,6,1]
    # O(N) Time O(N) Space
    # Two pass
