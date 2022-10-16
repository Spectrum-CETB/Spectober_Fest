import array as arr
arrr = arr.array('i',[4,2,5,9,1,8,6])
def bubblesort(arrr):
for j in range(len(arrr)-1,0,-1):
for i in range(j):
if arrr[i]> arrr[i+1]:
temp = arrr[i]
arrr[i] = arrr[i+1]
arrr[i+1] = temp
bubblesort(arrr)
print(arrr)
