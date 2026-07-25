class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in board:
            row_dict = {}
            for j in i:
                if j == ".":
                    continue
                row_dict[j] = row_dict.get(j, 0) + 1
            if bool(row_dict.values()) == True and max(row_dict.values()) >= 2:
                return False

        for j in range(len(board)):
            column_dict = {}
            for i in range(len(board)):
                if board[i][j] == ".":
                    continue
                column_dict[board[i][j]] = column_dict.get(board[i][j], 0) + 1   

            if bool(column_dict.values()) == True and max(column_dict.values()) >= 2:
                return False

        for i in range(3):
            for j in range(3):
                box_dict = {}
                for k in range(3):
                    for l in range(3):
                        if board[3 * i + k][3 * j + l] == ".":
                            continue
                        box_dict[board[3 * i + k][3 * j + l]] = box_dict.get(board[3 * i + k][3 * j + l], 0) + 1
                if bool(box_dict.values()) == True and max(box_dict.values()) >= 2:
                    return False

        return True