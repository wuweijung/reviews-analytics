data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 1000 == 0: #每一千筆印一次(餘數等於0)
			print(len(data))
print(len(data))

print(data[0])
print('---------------------')
print(data[1])	