class Solution:
    def isValidSudoku(self, board):

        # Check rows
        for row in board:
            seen = set()

            for num in row:
                if num == '.':
                    continue

                if num in seen:
                    return False

                seen.add(num)

        # Check columns
        for col in range(9):
            seen = set()

            for row in range(9):
                num = board[row][col]

                if num == '.':
                    continue

                if num in seen:
                    return False

                seen.add(num)

        # Check 3 x 3 boxes
        for start_row in range(0, 9, 3):
            for start_col in range(0, 9, 3):

                seen = set()

                for row in range(start_row, start_row + 3):
                    for col in range(start_col, start_col + 3):

                        num = board[row][col]

                        if num == '.':
                            continue

                        if num in seen:
                            return False

                        seen.add(num)

        return True