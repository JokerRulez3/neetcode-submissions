class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        subgrid = [[set() for _ in range(3)] for _ in range(3)]

        for r in range(9):
            for c in range(9):
                num = board[r][c]
                if num == ".":
                    continue
                if num in rows[r]:
                    return False
                if num in cols[c]:
                    return False
                if num in subgrid[r//3][c//3]:
                    return False
                
                rows[r].add(num)
                cols[c].add(num)
                subgrid[r//3][c//3].add(num)
        
        return True

                
        