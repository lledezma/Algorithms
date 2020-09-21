def dynFib(n):			#Dynamic fibonacci algorithm
	if n == 0 or n == 1 :
		return n
	else:
		arr = [0] * 2
		arr[0] = 1
		arr[1] = 1
		for i in range(2,n):
			temp = arr[1]
			arr[1] = arr[0] + arr[1]
			arr[0] = temp
	return arr[1]


def fib(n):			#recursion fibonacci number 
	if n == 0 or n == 1:
		return n
	else:
		return fib(n-1) + fib(n-2)


print(dynFib(30))
print(fib(30))