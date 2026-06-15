class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowhash={}
        colhash={}
        sqrhash={}

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if ((r, board[r][c]) in rowhash or
                    (c, board[r][c]) in colhash or
                    ((r // 3, c // 3), board[r][c]) in sqrhash):
                    return False
                rowhash[(r, board[r][c])] = True
                colhash[(c, board[r][c])] = True
                sqrhash[((r // 3, c // 3), board[r][c])] = True

        return True
