import re

with open('miracle_in_the_andes.txt') as file:
    book = file.read()
    # print(type(book)) # <class 'str'>

# 🙋 问题
# 如果想得到 有多少章节
# print(book.count('Chapter')) # 11 但这个不对只有10章节 还有一处来自 正文

# 使用正则匹配
pattern = re.compile('Chapter [0-9]+')
findings = re.findall(pattern, book)
# print(findings)
# ['Chapter 1', 'Chapter 2', 'Chapter 3', 'Chapter 4', 'Chapter 5', 'Chapter 6',
#  'Chapter 7', 'Chapter 8', 'Chapter 9', 'Chapter 10']

# print(len(findings)) # 10

# 🙋 问题
# 再来一个
pattern1 = re.compile('chapter [a-z]+')
findings1 = re.findall(pattern1, book)
# print(findings1) # ['chapter ab']


# 🙋 问题
# 找 哪个句子 使用了 love 这个词
pattern2 = re.compile('love')
findings2 = re.findall(pattern2, book)
# print(findings2) # 答案是 错误的 ❌  找到的都是 单独的 love 单词

# 怎么 ✅ 正确解决这个问题
pattern3 = re.compile('[a-zA-Z]* love [a-zA-Z]*')
findings3 = re.findall(pattern3, book)
# print(findings3) # 找到些 'passionate love for',  这样的 接近答案了

# 继续接近答案
# ^. 表示排除.  意思是从上一句话末尾
pattern4 = re.compile('[^.]*[^a-zA-Z]+love[^a-zA-Z]+[^.]*.')
pattern5 = re.compile('[A-Z]{1}[^.]*[^a-zA-Z]+love[^a-zA-Z]+[^.]*.')
findings4 = re.findall(pattern4, book)
findings5 = re.findall(pattern5, book)
# print(findings4)
# print(len(findings4)) # 67
# print(findings5)


# 🙋 问题
# 如何得到使用 最多的单词？
pattern6 = re.compile('[a-zA-Z]+')
findings6 = re.findall(pattern6, book.lower())
# print(len(findings6)) # 86799

d = {}
for word in findings6:
    if word in d.keys():
        d[word] = d[word] + 1
    else:
        d[word] = 1

# print(d) # {'chapter': 11, 'before': 93, 'it': 800, 'was': 1430, ...}

# 排序
d_list = [(value, key) for (key, value) in d.items()]
res = sorted(d_list, reverse=True)
print(res) # 找到出现最多的就是 这个 (5346, 'the')