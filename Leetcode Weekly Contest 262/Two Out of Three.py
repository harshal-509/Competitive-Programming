class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        return set(list(set(nums1).intersection(set(nums2)))+list(set(nums3).intersection(set(nums2)))+list(set(nums1).intersection(set(nums3))))