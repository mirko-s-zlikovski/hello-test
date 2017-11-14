
cache = {}


def fib(n):
	if n in cache:
		return cache[n]
	else:
		if n == 0:
			val = 1
		elif n == 1:
			val = 2
		else:
			val = fib(n-2) + fib(n-1)
		cache[n] = val
		return val

if __name__ == '__main__':
	print('100th Fibonacci number is {}'.format(fib(100)))


