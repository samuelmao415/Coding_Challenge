def search_word(board,i,j,w):
    if len(w)==0:
        return True
    if i<0 or i>=len(board) or j<0 or j>=len(board[0]) or w[0]!=board[i][j]:
        return False

    backup = board[i][j]
    board[i][j] = 0
    res = search_word(board, i+1,j,w[1:]) or search_word(board, i,j-1,w[1:]) or search_word(board, i-1,j,w[1:]) or search_word(board, i,j+1,w[1:])
    #print('res',res)
    board[i][j] = backup
    print(res)
    return res
#word = list(word)
for row in range(len(board)):
    for col in range(len(board[0])):
            if search_word(board,row,col,word):
                print('True')


word
board

board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCCED"


board = [["a","b"],["c","d"]]
word = "abcd"

board =[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

word = "ABCCED"
