class Solution:
    def rotate(self, matrix) -> None:



        left, right = 0, len(matrix) - 1

        while left < right:

            for i in range(right - left):
                top, bottom = left, right
