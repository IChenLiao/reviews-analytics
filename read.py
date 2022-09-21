data = []
count = 0 #記數用
with open ('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 1000 == 0: # %是用來求餘數
			print(len(data)) #每讀到1000筆資料就印出進度出來，print很花時間

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

#list conprehension 清單快寫法
good = [d for d in data if 'good' in d]
#print(good)

bad = ['bad' in d for d in data]
#print(bad)
