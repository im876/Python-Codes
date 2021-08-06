# A Dynamic Programming based Python
# Program for 0-1 Knapsack problem
# Returns the maximum value that can
# be put in a knapsack of capacity W


def knapSack(W, wt, val, n):
	K = [[0 for x in range(W + 1)] for x in range(n + 1)]

	# Build table K[][] in bottom up manner
	for i in range(n + 1):
		for w in range(W + 1):
			# Base Case
			if i == 0 or w == 0:
				K[i][w] = 0
			# return the maximum of two cases:
			# (1) nth item included
			# (2) not included
			elif wt[i-1] <= w:
				K[i][w] = max(val[i-1]+ K[i-1][w-wt[i-1]], K[i-1][w])
			# If weight of the nth item is
			# more than Knapsack of capacity W,
			# then this item cannot be included
			# in the optimal solution
			else:
				K[i][w] = K[i-1][w]

	return K[n][W]


# Driver code
val = list(map(int, input().split()))
wt = list(map(int, input().split()))
W = int(input().strip())
n = len(val)
print(knapSack(W, wt, val, n))
