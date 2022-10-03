
arr = input("Input the array of prices with a space between each price \n(eg. 7 1 5 3 6 4) \n: ")
arr = list(map(int, arr.split(' ')))

min_item = arr[0]
max_profit = 0

for item in arr:
	if min_item > item:
		min_item = item
		
	if max_profit < item - min_item:
		max_profit = item - min_item

print(max_profit)
