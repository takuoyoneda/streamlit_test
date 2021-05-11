import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time


st.title('Counter')

latest_iteration = st.empty()
bid = 100000
latest_iteration.text(f'BID {bid}')

# button_down = st.button('start')
button_down = True
is_upward = True
while(button_down):
    if is_upward:
        bid += 100
    else:
        bid -= 100
    latest_iteration.text(f'BID {bid}')
    time.sleep(1)
    if bid >= 103000:
        is_upward = False
    if bid <= 100000:
        is_upward = True
#         button_down = False





df = pd.read_csv('Stock Price - 2021_04_30.csv')
# st.write(df)
# st.dataframe(df.style.highlight_max(axis=0), width=200, height=200)
st.table(df.style.highlight_max(axis=0))


        
st.title('Tracer')
        
latest_iteration = st.empty()
bid = df['BID'].tolist()[0]
latest_iteration.text(f'BID {bid}')

button = st.button('start')
i = 0
while(button):
    bid = df['BID'].tolist()[i]
    latest_iteration.text(f'BID {bid}')
    time.sleep(0.1)
    i+=1    
    if i >= len(df['BID'].tolist()):
        button = False

        

        














st.title('Charts')

chart_df = df.drop('VOLUME', 1)
# chart_df = chart_df.drop('VWAP', 1)
chart_df = chart_df.drop('DATE', 1)
chart_df = chart_df.drop('TIME', 1)
chart_df = chart_df.drop('CREDIT', 1)
chart_df = chart_df.drop('PRESSURE', 1)
# chart_df

st.write('line_chart')
st.line_chart(chart_df)

# st.write('area_chart')
# st.area_chart(chart_df)

# st.write('bar_chart')
# st.bar_chart(chart_df)

st.write('altair_chart')
st.altair_chart(chart_df)















# """
# # 章
# ## 節
# ### 項

# '''python
# import streamlit as st
# import numpy as np
# import pandas as pd
# '''
# """


# st.write('Charts')
# df = pd.DataFrame(
#    np.random.rand(20,3),
#     columns=['a','b','c']
# )


# st.write(' progress bar')
# 'Start'
# latest_iteration = st.empty()
# bar = st.progress(0)
# for i in range(100):
#     latest_iteration.text(f'Iteration {i+1}')
#     bar.progress(i + 1)
#     time.sleep(0.1)
# 'Done'


# st.title('Test')


# option = st.selectbox(
#     'あなたが好きな数字',
#     list(range(1,11))
# )
# 'あなたの好きな数字は、', option, 'です'


# condition = st.sidebar.slider('あなたの調子', 0, 100, 50)
# 'コンディション: ', condition


# text = st.sidebar.text_input('あなたの趣味')
# 'あなたの趣味：', text


# st.write('Map')
# df = pd.DataFrame(
#     np.random.rand(100,2)/[50,50] + [35.69, 139.70],
#     columns=['lat','lon']
# )
# st.map(df)


# st.write('Display Image')
# if st.checkbox('Show Image'):
#     img = Image.open('Screen Shot 2020-10-16 at 10.54.20.png')
#     st.image(img, caption='Takuo Yoneda', use_column_width=True)


# st.write('問い合わせ')
# expander = st.beta_expander('問い合わせ')
# expander.write('問い合わせの回答')


# st.write('右に表示')
# left_column, right_column = st.beta_columns(2)
# button = left_column.button('右に表示')
# if button:
#     right_column.write('ここは右カラム')
