board = [
  [0,1,0],
  [0,0,1],
  [1,1,1],
  [0,0,0]
]


class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        neighbors = [(1,0),(1,-1),(1,1),(0,1),(0,-1),(-1,0),(-1,-1),(-1,1)]
        board_copy = [[board[rows][cols] for cols in range(len(board[0]))]for rows in range(len(board))]
        for row in range(len(board)):
            for col in range(len(board[0])):
                living_cells = 0
                for neighbor in neighbors:
                    r = neighbor[0] +row
                    c = neighbor[1] + col
                    if 0<=r<len(board) and 0<=c<len(board[0]) and board_copy[r][c] ==1:
                        living_cells +=1
                #rule 1 and 3
                if board_copy[row][col] ==1 and( living_cells<2 or living_cells>3):
                    board[row][col] =0
                #rule 2
                if board_copy[row][col] ==1 and 2<=living_cells<=3:
                    board[row][col] =1
                #rule 4
                if board_copy[row][col] ==0  and living_cells ==3:
                    board[row][col] =1
        return(board)
                    
