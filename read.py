data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1 # count= count+1
		if count % 1000 == 0: #每一千筆印一次(餘數等於0)
			print(len(data))
print('檔案讀取完畢，總共有', len(data), '筆資料')

sum_len = 0
for d in data:
	sum_len = sum_len + len(d)
print('每筆留言的平均長度為', sum_len/len(data), '個字元')

new = []
for d in data:
	if len(d) < 100:
		new.append(d)
print('其中有', len(new), '筆留言長度少於100個字元')
print(new[0])
print(len(new[0]))


good = []
for d in data:
	if 'good' in d:
		good.append(d)
print('其中有', len(good), '筆留言中提到good')
print(good[0])
