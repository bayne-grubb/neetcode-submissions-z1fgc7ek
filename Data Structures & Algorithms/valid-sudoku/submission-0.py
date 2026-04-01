class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for i in range(9)]
        cols = [set() for i in range(9)]
        squares = [set() for i in range(9)]

        def get_square(row, col) -> int:
            return (row // 3)*3 + (col // 3)

        def is_valid(i,j,c):
            row_check = c not in rows[i]
            col_check = c not in cols[j]
            square_check = c not in squares[get_square(i, j)]
            return row_check and col_check and square_check

        for i in range(9):
            for j in range(9):
                c = board[i][j]
                if c != ".":
                    if not is_valid(i, j, c):
                        return False
                    rows[i].add(c)
                    cols[j].add(c)
                    squares[get_square(i, j)].add(c)
        return True
        
        
        
        