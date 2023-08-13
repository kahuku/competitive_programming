# cisco summer 2024 intern assessment
# find which words are in a grid up, down, left, or right
"""
grid, represents the letters in the grid of size N*M.
word, represents the words to be searched of size K.
"""

def find(grid, word):
	for line in grid:
		if ''.join(line).count(word): return True
		if ''.join(line).count(word[::-1]): return True
	for col in range(len(grid[0])):
		line = [grid[i][col] for i in range(len(grid))]
		if ''.join(line).count(word): return True
		if ''.join(line).count(word[::-1]): return True
	return False

def funcPuzzle(grid, word):
	# Write your code here
	out = []
	for w in word:
		if find(grid, w):
			out.append("Yes")
		else:
			out.append("No")
	return ' '.join(out)

def main():
	#input for grid
	grid = []
	grid_rows,grid_cols  = map(int, input().split())
	for idx in range(grid_rows):
		grid.append(list(map(str, input().split())))
	
	#input for word
	word = []
	word_size  = int(input())
	word = list(map(str,input().split()))
	
	
	result = funcPuzzle(grid, word)
	print(result)	

if __name__ == "__main__":
	main()