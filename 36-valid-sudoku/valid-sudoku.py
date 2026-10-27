
class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for r in range(9):
            for c in range(9):
                num = board[r][c]

                # Skip empty cells
                if num == ".":
                    continue

                # Identify the 3 x 3 box
                box_index = (r // 3) * 3 + (c // 3)

                # Check for duplicates
                if (num in rows[r] or
                    num in cols[c] or
                    num in boxes[box_index]):
                    return False

                # Record the number
                rows[r].add(num)
                cols[c].add(num)
                boxes[box_index].add(num)

        return True
