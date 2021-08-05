def dyn_fib(n):				#Dynamic fibonacci algorithm 
	if n == 0 or n == 1:
		return n
	else:
		arr = [0]*n
		arr[0] = 1
		arr[1] = 1
		for i in range(2,n):
			arr[i] = arr[i-1]+arr[i-2]
	return arr[n-1]

def dynamic_fib(n):			#Dynamic fibonacci algorithm (Space Optimized)
	if n == 0 or n == 1:
		return n
	else:
		arr = [1,1]
		for i in range(2,n):
			temp = arr[1]
			arr[1] = arr[0] + arr[1]
			arr[0] = temp
	return arr[1]


def fib(n):		#Recursion fibonacci number 
	if n == 0 or n == 1:
		return n
	else:
		return fib(n-1) + fib(n-2)


print(dynamic_fib(10))
print(fib(10))
print(dyn_fib(10))