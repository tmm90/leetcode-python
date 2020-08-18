class Solution(object):
    def __init__(self):
        self.n = None
        self.total_len = None
        self.matrix = None

    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        m = len(matrix)
        if not m:
            return False

        n = len(matrix[0])
        if not n:
            return False

        self.n = n
        self.total_len = m * n
        self.matrix = matrix

        left = 0
        right = self.total_len

        while left < right:
            mid = (left + right) // 2
            mid_val = self.get_value_by_line_index(mid)
            if mid_val == target:
                return True

            if mid_val < target:
                left = mid + 1
            else:
                right = mid

        return False

    def get_value_by_line_index(self, line_index):
        assert 0 <= line_index < self.total_len
        i, j = divmod(line_index, self.n)
        return self.matrix[i][j]


def test_0074():
    s = Solution()
    matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 50]]
    target = 3
    assert s.searchMatrix(matrix, target)
    target = 13
    assert not s.searchMatrix(matrix, target)

    assert not s.searchMatrix([], target)
    assert not s.searchMatrix([[]], target)
