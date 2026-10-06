class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        mappings = {}
        for i in range(len(nums2)):
            mappings[nums2[i]] = i

        for num in nums1:
            res.append(mappings[num])
        return res