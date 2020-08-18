class Solution(object):
    def __init__(self):
        self.nums = None
        self.smallest_value_index = None

    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        self.nums = nums
        self.search_smallest_value_index()

        left = 0
        right = len(nums)
        while left < right:
            mid = (left + right) // 2
            mid_value = self.get_value_by_unrotated_index(mid)
            if mid_value == target:
                return self.get_rotated_index(mid)

            if mid_value > target:
                right = mid
            else:
                left = mid + 1

        return -1

    def search_smallest_value_index(self):
        # [left, right]
        left = 0
        right = len(self.nums) - 1

        while left <= right:
            if self.nums[left] <= self.nums[right]:
                self.smallest_value_index = left
                return

            if left + 1 == right:
                self.smallest_value_index = right
                return

            mid = (left + right) // 2
            if self.nums[mid] > self.nums[left]:
                left = mid + 1  # middle is not a candidate of smallest value.
            elif self.nums[mid] < self.nums[right]:
                right = mid  # middle value is a candidate of smallest value.

    def get_rotated_index(self, index):
        return (index + self.smallest_value_index) % len(self.nums)

    def get_value_by_unrotated_index(self, index):
        return self.nums[self.get_rotated_index(index)]


def test_0033():
    s = Solution()
    nums = [4, 5, 6, 7, 0, 1, 2]

    assert s.search(nums, 0) == 4
    assert s.search(nums, 3) == -1
    assert s.search([1], 0) == -1

    nums = [0, 1, 2, 4, 5, 6, 7]
    assert s.search(nums, 0) == 0

    nums = [1, 2, 4, 5, 6, 7, 0]
    assert s.search(nums, 0) == 6

    nums = [7, 0, 1, 2, 4, 5, 6]
    assert s.search(nums, 0) == 1

    nums = [3, 1]
    assert s.search(nums, 0) == -1

    nums = [5, 1, 3]
    assert s.search(nums, 5) == 0
