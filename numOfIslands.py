class Solution():
	def numIslands(self, grid):
		if not grid: 
			return 0
		count = 0
		print("the length of the grid is {}".format(len(grid)))
		for i in range(len(grid)):
			for j in range(len(grid[0])):
				print("{}".format(grid[i][j]))
				if grid[i][j] == '1':
					self.dfs(grid, i, j)
					count +=1
		return count

	def dfs(self, grid, i, j):
		if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] != '1':
			return 
		grid[i][j] = '#'
		self.dfs(grid, i + 1, j)
		self.dfs(grid, i - 1, j)
		self.dfs(grid, i, j + 1)
		self.dfs(grid, i, j - 1)

grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]

second_grid =  [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]

solution = Solution()
answer = solution.numIslands(grid)
second_answer = solution.numIslands(second_grid)
print("the answer is {}".format(answer))
print("the second answer is {}".format(second_answer))
