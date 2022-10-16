def product(ar, n):

	result = 1
	for i in range(0, n):
		result = result * ar[i]
	return result
ar = [ 1, 2, 3, 4, 5 ]
n = len(ar)

print(product(ar, n))


