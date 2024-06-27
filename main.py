import re

with open('miracle_in_the_andes.txt') as file:
    book = file.read()
    # print(type(book)) # <class 'str'>

# 如果想得到 有多少章节
# print(book.count('Chapter')) # 11 但这个不对只有10章节 还有一处来自 正文

# 使用正则匹配
pattern = re.compile('Chapter [0-9]+')
findings = re.findall(pattern, book)
print(findings)
# ['Chapter 1', 'Chapter 2', 'Chapter 3', 'Chapter 4', 'Chapter 5', 'Chapter 6',
#  'Chapter 7', 'Chapter 8', 'Chapter 9', 'Chapter 10']

# print(len(findings)) # 10

# 再来一个
pattern1 = re.compile('chapter [a-z]+')
findings1 = re.findall(pattern1, book)
# print(findings1) # ['chapter ab']