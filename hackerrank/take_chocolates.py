# cisco 2024 summer intern assessment
# same as leetcode house robber

"""
numJars, represents the number of jars.
Value of the array represents the number of chocolates in each jar.
"""
def maxSum(inputArr):
	# Write your code here
	def get_chocolates(nums, i, dp):
		if i == 0:
			dp[0] = nums[0]
		if i == 1:
			dp[1] = max(nums[0], nums[1])
		
		if dp[i] != -1:
			return dp[i]
		
		take = nums[i] + get_chocolates(nums, i - 2, dp)
		skip = get_chocolates(nums, i - 1, dp)
		dp[i] = max(take, skip)
		return dp[i]

	return get_chocolates(inputArr, len(inputArr) - 1, [-1 for i in range(len(inputArr) + 2)])

def main():
	#input for inputArr
	inputArr = []
	inputArr_size  = int(input())
	inputArr = list(map(int,input().split()))
	
	
	result = maxSum(inputArr)
	print(result)	

if __name__ == "__main__":
	main()