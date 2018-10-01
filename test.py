def test(n):
	if (n <= 1):
		return n
	else:
		return (test(n - 1) + test(n - 2))
	
for i in range(10):
	print test(i)