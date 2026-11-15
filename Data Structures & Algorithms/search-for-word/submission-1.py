class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        # choices: move up, down, left, or right
        # constraints: match the letter, stay in bounds, don't reuse a cell
        # base case: matched every letter in word
        # backtrack: add cell - recurse - remove cell

        hashset = set()

        def backtrack(i, row, col):
            if i == len(word): #base case
                return True

            if (row < 0 or row >= len(board) or
                col < 0 or col >= len(board[0]) or
                (row, col) in hashset or #these are constraints
                board[row][col] != word[i]):
                return False

            hashset.add((row, col)) # add to set so dont reuse- constraints

            found = (
                backtrack(i + 1, row + 1, col) or
                backtrack(i + 1, row - 1, col) or
                backtrack(i + 1, row, col + 1) or
                backtrack(i + 1, row, col - 1)
            ) # explore all directions

            hashset.remove((row, col)) # pop recurse part
            return found

        # Try every cell as the starting point.
        for row in range(len(board)):
            for col in range(len(board[0])):
                if backtrack(0, row, col): # check each path
                    return True

        return False