class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        length = len(board)
        board.reverse()
        def intTopos(square):
            r = (square-1)//length
            c = (square-1) % length
            if r%2:
                c = length-1-c
            return [r,c]
        
        q = deque()
        q.append([1,0])
        visit = set()

        while q:
            square, moves = q.popleft()

            for i in range(1,7):
                nxt = square + i
                r,c = intTopos(nxt)
                if board[r][c] !=-1:
                    nxt = board[r][c]
                if nxt  == length * length:
                    return moves + 1
                if nxt not in visit:
                    visit.add(nxt)
                    q.append([nxt, moves+1])
        return -1