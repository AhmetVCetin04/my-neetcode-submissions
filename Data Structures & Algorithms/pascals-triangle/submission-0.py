class Solution:
    def generate(self, numRows: int) -> List[List[int]]:

        pascals_triangle = [[1]]

        current_row = 2
        while current_row <= numRows:
            row = [1] * current_row
            for i in range(1, current_row-1):
                row[i] = pascals_triangle[-1][i-1] + pascals_triangle[-1][i]
            pascals_triangle.append(row)
            current_row += 1

        return pascals_triangle