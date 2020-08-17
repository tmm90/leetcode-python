# -*- encoding=utf-8 -*-
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums_index_dict = dict()
        for index, num in enumerate(nums):
            if target - num in nums_index_dict:
                return [index, nums_index_dict[target - num]]

            nums_index_dict[num] = index

        return []


def test_0001():
    nums = [2, 7, 11, 15]
    target = 9
    solution = Solution()

    # 存在情况
    assert sum([nums[index]
                for index in solution.twoSum(nums, target)]) == target

    # 不存在情况
    target = 20
    assert solution.twoSum(nums, target) == []

    # 边界情况：空数组
    assert solution.twoSum([], target) == []
