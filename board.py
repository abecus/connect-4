#%%
class Board:
	def __init__(self, turn=0):
		""""
		0:Yellow
		1:Red        
		"""
		self.remainingCells = 7*6
		self.board = [[2]*7 for _ in range(6)]
		self.turn = 0
		self.over = False

	def reset(self):
		"resets the board"
		self.__init__()
	
	def _isValidMove(self, col):
		"checks for valid move"
		return (0 <= col < 7) and (self.remainingCells > 0) and not self.over

	def drop(self, col):
		if not self._isValidMove(col):
			return False

		for i in reversed(range(6)):
			if self.board[i][col]==2:
				self.board[i][col]=self.turn
				self.remainingCells -= 1

				flag = self._isOver(self.turn)
				if flag:
					self.over = True
					return flag

				self.turn^=1
				return True

		return False

	def _checkDiagonal(self, i, j):
		# diagonally up-right
		curr = self.board[i][j]
		if all(self.board[i-x][j+x]==curr if 0<=i-x and j+x<7 else False 
				for x in range(4)):
			return True
		
		# diagonally up-left
		if all(self.board[i-x][j-x]==curr if 0<=i-x and 0<=j-x else False 
				for x in range(4)):
			return True
		return False

	def _checkVertical(self, i, j):
		return all(self.board[i][j]==self.board[i-x][j] if 0<=i-x else False
					for x in range(4))

	def _checkHorizontal(self, i, j):
		return all(self.board[i][j]==self.board[i][j+x] if j+x<7 else False
					for x in range(4))

	def _isOver(self, player):
		"checks if theirs winner"
		for i in reversed(range(6)):
			for j in range(7):
				if self.board[i][j]!=player:
					continue
				if self._checkVertical(i,j) or \
					self._checkDiagonal(i,j) or self._checkHorizontal(i,j):
					return "Yellow Wins" if player==0 else 'Red Wins'
		return 'Tie' if self.remainingCells==0 else ''

	def __repr__(self) -> str:
		return "\n".join(
			map(lambda row: "".join(map(str, row)), self.board)
				)
	
	def __str__(self) -> str:
		s = []
		for row in self.board:
			tmp = ''
			for i in row:
				if i==2:
					tmp+='.'
				elif i==0:
					tmp+='Y'
				else:
					tmp+='R'
			s.append(tmp)
		return "\n".join(s)

#%%
if __name__ == "__main__":
	game = Board()
	print(game)
	game.drop(1)
	print(game)
	game.drop(1)
	print(game)




# %%
