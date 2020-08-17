# -*- encoding=utf-8 -*-
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums_set = set()
        for num in nums:
            if target - num in nums_set:
                return [num, target - num]

            nums_set.add(num)

        return []


def test_0001():
    nums = [2, 7, 11, 15]
    target = 9
    solution = Solution()

    # 存在情况
    assert sum(solution.twoSum(nums, target)) == target

    # 不存在情况
    target = 20
    assert solution.twoSum(nums, target) == []

    # 边界情况：空数组
    assert solution.twoSum([], target) == []
