# 问题🙋 load the book
with open('miracle_in_the_andes.txt') as file:
    book = file.read()

# 问题🙋 找到 使用 love 的段落
import re
# [^\n] 是 每个段落特征 段落前后 都有 空行
pattern = re.compile("[^\n]+love[^\n]+")
findings = re.findall(pattern, book)
# print(findings[:2]) # 只展示前两个

# 问题🙋 找到标题
import re
pattern1 = re.compile('[a-zA-Z ,]+\n\n')
findings1 = re.findall(pattern1, book)
# print(findings1) # ['Before\n\n', 'Everything Precious\n\n'...
# 去掉末尾的 \n\n
findings1 = [item.strip('\n\n') for item in findings1]
# print(findings1)
# 非常漂亮的拿到结果
# ['Before', 'Everything Precious', 'A Promise', 'Breathe Once More',
# 'Abandoned', 'Tomb', 'East', 'The Opposite of Death', 'I See a Man',
# 'After']

# 第二种方法
import re
# 匹配由字母和空格组成的字符串，后面紧跟着两个换行符
pattern2 = re.compile('([a-zA-Z ]+)\n\n')
findings2 = re.findall(pattern2 , book)
# print(findings2) # # ['Before', 'Everything Precious', ...

# 问题 🙋
# 写个函数方法 输入一个单词 找到出现次数
def find(w):
    pattern3 = re.compile('[a-zA-Z]+')
    findings3 = re.findall(pattern3,book.lower())
    d = {}
    for word in findings3:
        if word in d.keys():
            d[word] = d[word] + 1
        else:
            d[word] = 1

    try:
        return d[w]
    except:
        return f'The book does not contain the word "{w}"'

print(find('love')) # 83
print(find('hite')) # The book does not contain the word "hite"