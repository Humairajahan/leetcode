from typing import List

# Naive Approach: Two pointer
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        for idx in range(1, k + 1):
            for jdx in range(len(nums) - idx):
                if nums[jdx] == nums[idx + jdx]:
                    return True
        return False


# Optimized Approach
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        z = {}
        for idx in range(len(nums)):
            if nums[idx] not in z:
                z[nums[idx]] = idx 
            else:
                if abs(z[nums[idx]] - idx) <= k:
                    return True
                z[nums[idx]] = idx
        return False
    

s = Solution()

test_case_1 = s.containsNearbyDuplicate(nums=[1, 2, 3, 1], k=3)
print(test_case_1)

test_case_2 = s.containsNearbyDuplicate(nums=[1, 0, 1, 1], k=1)
print(test_case_2)

test_case_3 = s.containsNearbyDuplicate(nums=[1, 2, 3, 1, 2, 3], k=2)
print(test_case_3)
