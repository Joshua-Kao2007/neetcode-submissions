class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        cache = {}
        for i in range(len(nums2)):
            cache[nums2[i]] = i # will replace duplicates with last occurrence

        res = [None]*len(nums1)
        for i in range(len(nums1)):
            res[i] = cache[nums1[i]]
        return res

        # # Cache nums2 --> just replace (will give last Occur)
        # # Find nums1 element in cache
        # O(N), O(N)

        
        # O(N^2)
        # # Loop Thru Nums1:
        #     # Fin FIrst Occur in Nums2
        #         # Output res append same element 
        
        
        
        # May contain duplicates
        # nums2 is an anagram of nums1

        # return List[int]