import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

pd.read_csv('Stock Price - 2021_04_30.csv')
st.write(df)
st.dataframe(df.style.highlight_max(axis=0), width=200, height=200)
st.table(df.style.highlight_max(axis=0))




st.write('Charts')
df = pd.DataFrame(
    np.random.rand(20,3),
    columns=['a','b','c']
)
st.line_chart(df)
st.area_chart(df)
st.bar_chart(df)





st.write(' progress bar')
'Start'
latest_iteration = st.empty()
bar = st.progress(0)
for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i + 1)
    time.sleep(0.1)
'Done'


























"""
# 章
## 節
### 項

'''python
import streamlit as st
import numpy as np
import pandas as pd
'''
"""

st.title('Test')

text = st.sidebar.text_input('あなたの趣味')
'あなたの趣味：', text

condition = st.sidebar.slider('あなたの調子', 0, 100, 50)
'コンディション: ', condition


option = st.selectbox(
    'あなたが好きな数字',
    list(range(1,11))
)
'あなたの好きな数字は、', option, 'です'


st.write('Map')
df = pd.DataFrame(
    np.random.rand(100,2)/[50,50] + [35.69, 139.70],
    columns=['lat','lon']
)
st.map(df)


st.write('Display Image')
if st.checkbox('Show Image'):
    img = Image.open('Screen Shot 2020-10-16 at 10.54.20.png')
    st.image(img, caption='Takuo Yoneda', use_column_width=True)


st.write('問い合わせ')
expander = st.beta_expander('問い合わせ')
expander.write('問い合わせの回答')


st.write('右に表示')
left_column, right_column = st.beta_columns(2)
button = left_column.button('右に表示')
if button:
    right_column.write('ここは右カラム')
