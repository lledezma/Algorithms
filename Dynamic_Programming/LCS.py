	# Longest Common Subsequence Algorithm
def LCS_Length(X,Y):
	m = len(X)		#rows
	n = len(Y)		#columns
	b = [[0 for i in range(n)] for j in range(m)] 
	c = [[0 for i in range(n)] for j in range(m)] 

	for i in range(m):
		for j in range(n):
			if X[i] == Y[j]:
				if i != 0 and j !=0:
					c[i][j] = c[i-1][j-1]+1
					b[i][j] = "↖"
				else:
					c[i][j] = 1
					b[i][j] = "↖"
			elif c[i-1][j] >= c[i][j-1]:
				c[i][j] = c[i-1][j]
				b[i][j] = "↑"
			else:
				c[i][j] = c[i][j-1]
				b[i][j] = "←"
	return b, c


def PRINT_LCS(b, X, i, j):
	if j == 0 or i == 0:
		if b[i][j] == "↖":
			print(X[i],end='')
			return 
		else:
			return
	if b[i][j] == "↖":
		PRINT_LCS(b,X,i-1,j-1)
		print(X[i],end='')
	elif b[i][j] == "↑":
		PRINT_LCS(b,X,i-1,j)
	else:
		PRINT_LCS(b,X,i,j-1)



X = "ABCBDAB"
Y = "BDCABA"

rows = len(X)
columns = len(Y)

b,c = LCS_Length(X,Y)
PRINT_LCS(b,X,rows-1,columns-1)

print()
for i in range(rows):
	print(b[i])
for j in range(rows):
	print(c[j])
