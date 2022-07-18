from typing import *


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # import itertools
        # for i, j in itertools.combinations_with_replacement(nums, 2):
        #     if i + j == target:
        #         pass
        for i in range(l := len(nums)):
            for j in range(i + 1, l):
                if nums[i] + nums[j] == target:
                    return [i, j]


if __name__ == "__main__":
    print(Solution().twoSum([1, 2, 3, 4], target=3))
    print(Solution().twoSum(nums = [2,7,11,15], target = 9))
    print(Solution().twoSum(nums = [3,2,4], target = 6))
    print(Solution().twoSum(nums = [3,3], target = 6))
