from collections import defaultdict


class SudokuSolver():
    def solveSudoku(self, board):

        def place_number(d, i, j):
            rows[i][d] += 1
            columns[j][d] += 1
            boxes[box_index(i, j)][d] += 1
            board[i][j] = str(d)

        def remove_number(d, i, j):
            del rows[i][d]
            del columns[j][d]
            del boxes[box_index(i, j)][d]
            board[i][j] = '.'

        def place_next(i, j):
            ## if at the last element, solves the sudoku
            if i == N - 1 and j == N - 1:
                nonlocal sudokuSolved
                sudokuSolved = True
            else:
                # if end of a row, go to the next row
                if j == N - 1:
                    backtrace(i + 1, 0)
                else:
                    backtrace(i, j + 1)

        def can_place(d, row, col):
            return not (d in rows[row] or d in columns[col] or d in boxes[box_index(row, col)])

        def backtrace(row = 0, col = 0):
            if board[row][col] == '.':
                for d in range(1, 10):
                    if can_place(d, row, col):
                        place_number(d, row, col)
                        place_next(row, col)

                        if not sudokuSolved:
                            remove_number(d, row, col)
            else:
                place_next(row, col)

        n = 3
        N = n * n
        box_index = lambda row, col: (row // n) * n + col // n

        rows = [defaultdict(int) for i in range(N)]
        columns = [defaultdict(int) for i in range(N)]
        boxes = [defaultdict(int) for i in range(N)]

        for i in range(N):
            for j in range(N):
                if board[i][j] != '.':
                    d = int(board[i][j])
                    place_number(d, i, j)
        sudokuSolved = False
        backtrace()


board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
solver = SudokuSolver()
solver.solveSudoku(board)
# print(board)
