arr = input("Input the array of numbers \n(eg. 1 7 3 6 5 6) \n: ")
arr = list(map(int, arr.split(' ')))

total = sum(arr)
total_till_now = 0

for i in range(len(arr)):

	if total_till_now == total - total_till_now - arr[i]:
		print(i)
		exit()

	total_till_now += arr[i]

print(-1)
