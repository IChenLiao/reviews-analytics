import time
import progressbar

data = []
count = 0
bar = progressbar.ProgressBar(max_value=1000000)
with open ('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		bar.update(count)
print('檔案讀取完了，總共有', len(data), '筆資料') #直接印出總數出來

#寫程式碼算出留言的平均長度

sum_len = 0
for d in data:
	sum_len = sum_len + len(d)

print('留言平均長度是', sum_len/len(data))

new = []
for d in data:
	if len(d) < 100:
		new.append(d)
print('一共有', len(new), '筆留言長度小於100')
print(new[0])


good = []
for d in data:
	if 'good' in d:
		good.append(d)
print('一共有', len(good), '筆留言提到good')
print(good[0])

start_time = time.time()
wc = {} #word count
for d in data:
	words = d.split() #split預設值是用空白符號切
	for word in words:
		if word in wc:
			wc[word] += 1
		else:
			wc[word] = 1 #新增新的key進wc字典

for word in wc:
	if wc[word] > 1000000 :
		print(word, wc[word])
end_time = time.time()
print('花了', end_time - start_time, 'seconds')
print(len(wc))
print(wc['Tina'])

while True:
	word = input('請問你想查什麼字: ')
	if word == 'q':
		break
	if word in wc:
		print(word, '出現過的次數為: ', wc[word])
	else:
		print('這個字沒有出現過哦!')

print('感謝使用本查詢功能')