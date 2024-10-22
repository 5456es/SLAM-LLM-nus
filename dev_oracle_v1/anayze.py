ocr_list=[]
train_scp_file_path = "/nfs/yangguanrou.ygr/slidespeech/test_oracle_v1/"
with open(train_scp_file_path + "hot_related/ocr_1gram_top50_mmr070_hotwords_list",'r') as f:
    for line in f:
        line = line.strip().split()
        if len(line) == 1:
            ocr_list.append(None)
        else:
            line = line[1]
            line = line.split('$')
            ocr_list.append(line)

label_list=[]
with open(train_scp_file_path + "text",'r') as f:
    for line in f:
        line = line.strip().split(' ',1)
        if len(line) == 1:
            label_list.append(None)
        else:
            label_list.append(line[1])

words_sum=0
in_sum=0

useful_list=[]
for i in range(len(ocr_list)):
    text=label_list[i].split()
    hotwords=ocr_list[i]

    words_sum+= len(text)
    if hotwords is None:
        continue
    for word in hotwords:
        if word in text:
            in_sum+=1
            useful_list.append(word)
            # print(word)


print(words_sum)
print(in_sum)
print(in_sum/words_sum)
print(useful_list)
exit()
# 82881
# 4996
# 0.0602791954730276


ocr_list=[]
train_scp_file_path = "/nfs/yangguanrou.ygr/slidespeech/dev_oracle_v1/"
with open(train_scp_file_path + "hot_related/ocr_1gram_top50_mmr070_hotwords_list",'r') as f:
    for line in f:
        line = line.strip().split()
        if len(line) == 1:
            ocr_list.append(None)
        else:
            line = line[1]
            line = line.split('$')
            ocr_list.append(line)

label_list=[]
with open(train_scp_file_path + "text",'r') as f:
    for line in f:
        line = line.strip().split(' ',1)
        if len(line) == 1:
            label_list.append(None)
        else:
            label_list.append(line[1])

words_sum=0
in_sum=0


for i in range(len(ocr_list)):
    text=label_list[i].split()
    hotwords=ocr_list[i]

    words_sum+= len(text)
    if hotwords is None:
        continue
    for word in hotwords:
        if word in text:
            in_sum+=1
            useful_list.append(word)


print(words_sum)
print(in_sum)
print(in_sum/words_sum)
print(useful_list)

# 46952
# 2937
# 0.06255324586812064


ocr_list=[]
train_scp_file_path = "/nfs/yangguanrou.ygr/slidespeech/train_95/"
with open(train_scp_file_path + "hot_related/ocr_1gram_top50_mmr070_hotwords_list",'r') as f:
    for line in f:
        line = line.strip().split()
        if len(line) == 1:
            ocr_list.append(None)
        else:
            line = line[1]
            line = line.split('$')
            ocr_list.append(line)

label_list=[]
with open(train_scp_file_path + "text",'r') as f:
    for line in f:
        line = line.strip().split(' ',1)
        if len(line) == 1:
            label_list.append(None)
        else:
            label_list.append(line[1])

words_sum=0
in_sum=0

for i in range(len(ocr_list)):
    text=label_list[i].split()
    hotwords=ocr_list[i]

    words_sum+= len(text)
    if hotwords is None:
        continue
    for word in hotwords:
        if word in text:
            in_sum+=1


print(words_sum)
print(in_sum)
print(in_sum/words_sum)


# 1046615
# 40161
# 0.03837227633848168