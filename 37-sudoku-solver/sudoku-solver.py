
class Solution:
    def solveSudoku(self, board: list[list[str]]) -> None:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        empty = []

        # Initialize sets and collect empty cells
        for r in range(9):
            for c in range(9):
                num = board[r][c]

                if num == ".":
                    empty.append((r, c))
                else:
                    box = (r // 3) * 3 + c // 3
                    rows[r].add(num)
                    cols[c].add(num)
                    boxes[box].add(num)

        digits = set("123456789")

        def backtrack(pos):
            if pos == len(empty):
                return True

            # Find the empty cell with the fewest candidates
            best = pos
            best_candidates = None

            for i in range(pos, len(empty)):
                r, c = empty[i]
                box = (r // 3) * 3 + c // 3

                candidates = (
                    digits - rows[r] - cols[c] - boxes[box]
                )

                if best_candidates is None or len(candidates) < len(best_candidates):
                    best = i
                    best_candidates = candidates

                if len(best_candidates) == 0:
                    return False

                if len(best_candidates) == 1:
                    break

            # Place the most constrained cell first
            empty[pos], empty[best] = empty[best], empty[pos]
            r, c = empty[pos]
            box = (r // 3) * 3 + c // 3

            for num in best_candidates:
                board[r][c] = num
                rows[r].add(num)
                cols[c].add(num)
                boxes[box].add(num)

                if backtrack(pos + 1):
                    return True

                # Undo the choice
                board[r][c] = "."
                rows[r].remove(num)
                cols[c].remove(num)
                boxes[box].remove(num)

            empty[pos], empty[best] = empty[best], empty[pos]
            return False

        backtrack(0)
