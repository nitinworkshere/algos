#f(n) = f(n - 1) + (n - 1) * f(n - 2)


# Python program solution of
# friends pairing problem

# Returns count of ways
# n people can remain
# single or paired up.
def countFriendsPairings(n):

	dp = [0 for i in range(n + 1)]

	# Filling dp[] in bottom-up manner using
	# recursive formula explained above.
	for i in range(n + 1):

		if(i <= 2):
			dp[i] = i
		else:
			dp[i] = dp[i - 1] + (i - 1) * dp[i - 2]

	return dp[n]

# Driver code
n = 4
print(countFriendsPairings(n))

# This code is contributed
# by Soumen Ghosh.
