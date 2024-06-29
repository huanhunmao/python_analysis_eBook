# 问题 🙋 分析一句话/段落/一本书 是积极的 还是消极的

# 下面这些是 原来的基础部分
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
# print(d_list) # [(5346, 'the'), (2795, 'and'), (2729, 'i'), ...

import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
from nltk.data import find

# 显示NLTK数据路径
# print(nltk.data.path)

# 将下载的VADER词典文件放置到上述路径中的一个目录下，例如 `~/nltk_data/sentiment/`
nltk.data.path.append('nltk_data')

# 检查VADER词典是否存在
try:
    find('sentiment/vader_lexicon.zip')
    print("VADER lexicon found")
except LookupError:
    print("VADER lexicon not found")

# 实例化情感分析器
analyzer = SentimentIntensityAnalyzer()
# scores = analyzer.polarity_scores('hhaha, I am happy')
# print('scores', scores)
# neg 是消极分
# pos 是积极分
# neu 是中性分
# compound 是 综合分

# 定义为积极  pos > neg  /  compound > 0
# scores {'neg': 0.0, 'neu': 0.351, 'pos': 0.649, 'compound': 0.5719}

# if scores['pos'] > scores['neg']:
#     print('It is a positive text')
# else:
#     print('It is a negative text')

# 分析一本书是 积极的还是消极的
analyzerBook = analyzer.polarity_scores(book)
# print(analyzerBook)
# {'neg': 0.116, 'neu': 0.76, 'pos': 0.125, 'compound': 1.0}

# 段落分析
import re
pattern4 = re.compile('Chapter [0-9]+')
chapters = re.split(pattern4, book)
# print(len(chapters)) # 只有10段 但打出 11 有 ''
chapters = chapters[1:] # 从第一个 开始
for chapter in chapters:
    scores = analyzer.polarity_scores(chapter)
    # print(scores)
# 打印每个段落的 情感  数值
# {'neg': 0.061, 'neu': 0.779, 'pos': 0.16, 'compound': 1.0}
# {'neg': 0.12, 'neu': 0.726, 'pos': 0.154, 'compound': 0.9991}
# {'neg': 0.145, 'neu': 0.751, 'pos': 0.105, 'compound': -0.9999}
# {'neg': 0.141, 'neu': 0.721, 'pos': 0.138, 'compound': -0.9963}
# {'neg': 0.118, 'neu': 0.742, 'pos': 0.141, 'compound': 0.9997}
# {'neg': 0.124, 'neu': 0.761, 'pos': 0.115, 'compound': -0.9979}
# {'neg': 0.136, 'neu': 0.761, 'pos': 0.103, 'compound': -0.9999}
# {'neg': 0.12, 'neu': 0.786, 'pos': 0.094, 'compound': -0.9998}
# {'neg': 0.097, 'neu': 0.824, 'pos': 0.079, 'compound': -0.9996}
# {'neg': 0.086, 'neu': 0.733, 'pos': 0.181, 'compound': 1.0}


# 带上章节编号
for nr,chapter in enumerate(chapters):
    scores = analyzer.polarity_scores(chapter)
    print(nr + 1, scores)
# 1 {'neg': 0.061, 'neu': 0.779, 'pos': 0.16, 'compound': 1.0}
# 2 {'neg': 0.12, 'neu': 0.726, 'pos': 0.154, 'compound': 0.9991}
# ...