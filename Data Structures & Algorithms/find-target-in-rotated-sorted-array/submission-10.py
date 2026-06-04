class Solution:
    def search(self, nums: List[int], target: int) -> int:
        L,R = 0, len(nums)-1
        while L+1 < R:
            mid = L + (R-L)//2
            if nums[L] == target:
                return L
            if nums[R] == target:
                return R
            if nums[mid] == target:
                return mid
            if target > nums[mid] and target > nums[R] and nums[mid] > nums[R]:
                L = mid+1
            elif target > nums[mid] and target > nums[R] and nums[mid] < nums[R]:
                R = mid-1
            elif nums[mid] < target < nums[R]:
                L = mid+1

            elif target < nums[mid] < nums[R]:
                R = mid-1
            elif nums[mid] > target and nums[mid] > nums[R] and target < nums[R]:
                L = mid+1
            elif nums[mid] > target and nums[mid] > nums[R] and target > nums[R]:
                R = mid-1
        if nums[L] == target:
            return L
        if nums[R] == target:
            return R
        return -1


    # target = 5
    # [1,2,3,4,5] --> middle=3. mid < nums[R], nums[]==nums[R]
    # [5,1,2,3,4] --> middle=2. mid < nums[R]. target > mid. target > nums[R]. so on left. target>mid and target >nums[R]. LEFT SIDE. middle < left side
    # [4,5,1,2,3] --> middle=1 target > nums[R] target > mid. LEFT SIDE
    # [3,4,5,1,2] --> middle=5 target = 
    # [2,3,4,5,1] --> middle = 4. target > mid. target > right side. middle > right side. RIGHT SIDE

    # target = 1
    # [1,2,3,4,5] --> middle=3, target<mid<nums[R]--> nums[L]
    # [5,1,2,3,4] --> middle=2, target<mid<nums[R]. ON LEFT
    # [4,5,1,2,3] --> middle=1 good
    # [3,4,5,1,2] --> middle=5,middle > nums[R] and middle > target. ON RIGHT. target < nums[R] on RIGHT

    # [2,3,4,5,1] --> middle=4, middle>nums[R] and nums[R]

    # target = 2
    # [1,2,3,4,5] --> target < mid < nums[R] LEFT
    # [5,1,2,3,4] --> 
    # [4,5,1,2,3] --> mid < target < nums[R] RIGHT
    # [3,4,5,1,2] --> mid > nums[R]  and mid > target RIGHT
    # [2,3,4,5,1] --> mid > nums[R] and mid > target. target > nums[R] on LEFT

    # so if mid is greater than nums[R] and target>mid. than gotta be on right side. L=mid+1
    # if mid is greater than nums[R] and target < mid, left side

    # if mid is less than right. And target > nums[R], then gotta be on left side. R=mid-1
    # if mid is less than right. And target < nums[R], then gotta be on right side
