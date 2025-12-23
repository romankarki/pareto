# uses dfs in this case rather than bfs


class Solution:


    def find_words(self, board, words):

        result= []

        for word in words:
            if self.is_word_available(board, word):
                result.append(word)
        return result


    

    def is_word_available(self, board, word):

        R, C = len(board), len(board[0])

        def dfs(row, col, i):
            if i == len(word):
                return True

            if row < 0 or col < 0 or row >= R or col >= C or word[i] != board[row][col] or board[row][col] == "*":
                return False

            board[row][col] = "*"

            res = dfs(row + 1, col, i+1) or dfs(row-1, col, i+1) or dfs(row, col +1, i+1) or dfs(row, col -1, i+1)
            board[row][col] = word[i]
            return res
         
        


        for r in range(0, R):
            for c in range(0, C):
                if word[0] == board[r][c] and dfs(r,c, 0):
                    return True
        return False