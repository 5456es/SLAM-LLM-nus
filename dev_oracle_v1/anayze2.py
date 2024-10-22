ocr_list=[]
train_scp_file_path = "/nfs/yangguanrou.ygr/slidespeech/test_oracle_v1/"
with open(train_scp_file_path + "ocr_text_type2",'r') as f:
    for line in f:
        line = line.strip().split(' ',1)
        if len(line) == 1:
            ocr_list.append(None)
        else:
            line = line[1]
            line = line.split()
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

print(useful_list)
print(words_sum)
print(in_sum)
print(in_sum/words_sum)

# from nltk.corpus import wordnet

from tqdm import tqdm
not_word=[]

import json

# 假设你有一个JSON对象，你想将它转换为Python字典
f = open("/nfs/yangguanrou.ygr/slidespeech/test_oracle_v1/words_dictionary.json",) 
json_dict = json.load(f)

# 转换字典的键为集合
keys_set = set(json_dict.keys())

# print(keys_set)

# # print(wordnet.synsets('FOR'))
# # print(wordnet.synsets('for'))
# # print(wordnet.synsets('TYPE'))
from PyDictionary import PyDictionary
dictionary = PyDictionary()

def is_english_word(word):
    return dictionary.meaning(word) is not None

# import enchant
# d = enchant.Dict("en_US")

# def is_english_word(word):
#     return d.check(word)
second_not_word=[]
# print(is_english_word("hello"))  # 输出 True 或 False
for word in tqdm(useful_list):
    # print(wordnet.synsets(word))
    # if not wordnet.synsets(word):
    word = word.lower()
    if not word in keys_set:
       not_word.append(word)
print(not_word)
print(len(not_word))

for word in tqdm(not_word):
    if not is_english_word(word):
        second_not_word.append(word)

exit()
# 82881
# 21870
# 0.26387229883809316


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