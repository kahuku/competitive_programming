
"""
inputNum1, represents the number X.
inputNum2, represents the number Y.
"""
def funcCount(inputNum1, inputNum2):
	# Write your code here
	def valid(num, Y):
		s = 0
		for dig in str(num):
			s += int(dig)
		return s == Y

	count = 0
	for i in range(inputNum1 + 1):
		count += 1 if valid(i, inputNum2) else 0

	return count if count > 0 else -1

def main():
	#input for inputNum1
	inputNum1 = int(input())
	
	#input for inputNum2
	inputNum2 = int(input())
	
	
	result = funcCount(inputNum1, inputNum2)
	print(result)	

if __name__ == "__main__":
	main()