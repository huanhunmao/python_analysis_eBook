# 问题🙋
# 刚才的问题是 正则无法 分辨那些是真的单词， 比如 i u 这种无法区别
# 使用 nltk 来解决这个问题

# load the book
with open('miracle_in_the_andes.txt') as file:
    book = file.read()

import re
d = {}
pattern3 = re.compile('[a-zA-Z]+')
findings3 = re.findall(pattern3, book.lower())
for word in findings3:
    if word in d.keys():
        d[word] = d[word] + 1
    else:
        d[word] = 1

d_list = [(value, key) for (key, value) in d.items()]
d_list = sorted(d_list, reverse=True)
d_list[:5]
# print(d_list) # [(5346, 'the'), (2795, 'and'), (2729, 'i'), (2400, 'to'),

# 问题🙋
# 刚才的问题是 正则无法 分辨那些是真的单词， 比如 i u 这种无法区别
# 使用 nltk 来解决这个问题

# load the book
with open('miracle_in_the_andes.txt') as file:
    book = file.read()

import re
d = {}
pattern3 = re.compile('[a-zA-Z]+')
findings3 = re.findall(pattern3, book.lower())
for word in findings3:
    if word in d.keys():
        d[word] = d[word] + 1
    else:
        d[word] = 1

d_list = [(value, key) for (key, value) in d.items()]
d_list = sorted(d_list, reverse=True)
d_list[:5]
# print(d_list) # [(5346, 'the'), (2795, 'and'), (2729, 'i'), (2400, 'to'),

# 使用 nltk 自然语言处理工具
import nltk

# 下载停用词数据包
# nltk.download('stopwords')

# 导入停用词
from nltk.corpus import stopwords
from nltk.data import find
# 设置 NLTK 数据目录  这个地方直接手动下载好 放入 nltk_data 文件夹
nltk.data.path.append('nltk_data')

# 确认是否能够找到数据包
try:
    find('corpora/stopwords')
    print("Stopwords data found")
except LookupError:
    print("Stopwords data not found")

# 使用停用词数据 拿到英语单词
english_stopwords = stopwords.words('english')
# print(english_stopwords) # ['i', 'me', 'my', 'myself', 'we', 'our', 'ours', '

filtered_words = []
for count, word in d_list:
    if word not in english_stopwords:
        filtered_words.append((word, count))
print('filtered_words', filtered_words)
# [('would', 575), ('us', 519), ('said', 292),