import glob
import streamlit as st
import plotly.express as px

import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
from nltk.data import find

# 读取 文件数据
filepaths = sorted(glob.glob('diary/*.txt'))
# print(filepaths)
# ['diary/2023-10-21.txt', 'diary/2023-10-22.txt', 'diary/2023-10-23.txt', 'diary/2023-10-24.txt', 'diary/2023-10-25.txt', 'diary/2023-10-26.txt', 'diary/2023-10-27.txt']

# 准备 SentimentIntensityAnalyzer 分析本地数据
nltk.data.path.append('nltk_data')
# 检查VADER词典是否存在
try:
    find('sentiment/vader_lexicon.zip')
    print("VADER lexicon found")
except LookupError:
    print("VADER lexicon not found")
analyzer = SentimentIntensityAnalyzer()

positivity = []
negativity = []
for filepath in filepaths:
    with open(filepath) as file:
        content = file.read()
    scores = analyzer.polarity_scores(content)
    positivity.append(scores['pos'])
    negativity.append(scores['neg'])

dates = [name.strip('.txt').strip('diary/') for name in filepaths]
print(dates)
# ['2023-10-21', '2023-10-22', '2023-10-23', '2023-10-24', '2023-10-25', '2023-10-26', '2023-10-27']

print(positivity) # [0.065, 0.17, 0.203, 0.238, 0.159, 0.062, 0.177]

# 开始画图
st.title('Diary Notes')
st.subheader('Positivity')
pos_figure = px.line(x=dates, y=positivity,
                     labels={'x': 'Date', 'y': 'Positivity'})
st.plotly_chart(pos_figure)

st.subheader('Negativity')
neg_figure = px.line(x=dates, y=negativity,
                     labels={'x': 'Date', 'y': 'Negativity'})
st.plotly_chart(neg_figure)

# 运行 streamlit run analyze_notes_daily.py 可看到图表📈
