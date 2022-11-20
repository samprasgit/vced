# !/usr/bin/python
# -*- coding: utf-8 -*-


import pandas as pd
import numpy as np
import streamlit as st

st.set_page_config(page_title="Hello Streamlit")

st.title("This is your first Streamlit page!")  # 标题

st.markdown("Streamlit is **_really_ cool**.")  # markdown

code = """def hello():
     print("Hello, Streamlit!")"""
st.code(code, language="python")  # code

df = pd.DataFrame(np.random.randn(50, 20), columns=("col %d" % i for i in range(20)))
st.dataframe(df)  # dataframe

st.latex(
    r"""
     a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
     \sum_{k=0}^{n-1} ar^k =
     a \left(\frac{1-r^{n}}{1-r}\right)
     """
)  # latex

# 图表展示
st.write("绘制一个折线图:")
chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])

st.line_chart(chart_data)

# st.map 绘制地图
st.write("绘制一个地图:")
map_data = pd.DataFrame(np.random.randn(1000, 2) / [50, 50] + [39.56, 116.20], columns=["lat", "lon"])

st.map(map_data)


# 交互性选择
if st.checkbox("Show dataframe"):
    chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])

chart_data


# 选择框
option = st.selectbox("Which number do you like best?", df["col 0"])

"You selected: ", option


# 调整布局
left_column, right_column = st.beta_columns(2)
pressed = left_column.button("Press me?")
if pressed:
    right_column.write("Woohoo!")

expander = st.beta_expander("FAQ")
expander.write("Here you could put in some really, really long explanations...")

# 添加进度条
import time

"Starting a long computation..."

# Add a placeholder
latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    # Update the progress bar with each iteration.
    latest_iteration.text(f"Iteration {i+1}")
    bar.progress(i + 1)
    time.sleep(0.1)

"...and now we're done!"
