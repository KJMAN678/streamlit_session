import streamlit as st
import uuid

# クリックするたび数字が増える
st.subheader("1.クリックするたび数字が増える")
if 'count' not in st.session_state:
  st.session_state["count"] = 0
  
if st.button("カウント", key=0):
  st.session_state["count"] += 1
  
st.write("カウント", st.session_state["count"])

# ボタンを押した数だけテキストが増える
st.subheader("2.ボタンを押した数だけテキストが増える")
if 'increasement' not in st.session_state:
  st.session_state["increasement"] = 0
  
if st.button("カウント", key=1):
  st.session_state["increasement"] += 1

for i in range(st.session_state["increasement"]):
  st.write(f"ボタンを押した回数 {i+1} 回目分")
  
# テキストフィールドに入力したテキストの追加ボタン、削除ボタンを設置。
st.subheader("3.テキストフィールドの文字が、追加ボタンを押すと増え、削除ボタンを押すと消える")
text = st.text_input("表示したい単語を入力してください")

if 'text_list' not in st.session_state:
  st.session_state["text_list"] = []

col1, col2 = st.columns(2)

with col1:
  if st.button("追加", key=2):
    st.session_state["text_list"].append(text)

with col2:
  if st.button("削除", key=3): 
    st.session_state["text_list"].remove(text)
      
for output_text in st.session_state["text_list"]:
  st.write("", output_text)
  
# 綺麗に並んだテキスト（行数の表示あり）３つが、追加ボタンを押すと増え、削除ボタンを押すと消える
st.subheader("4.綺麗に並んだテキスト（行数の表示あり）３つが、追加ボタンを押すと増え、削除ボタンを押すと消える")
if 'add_container' not in st.session_state:
  st.session_state["add_container"] = 0

col3, col4 = st.columns(2)

with col3:
  if st.button("追加", key=4):
    st.session_state["add_container"] += 1

with col4:
  if st.button("削除", key=5):
    if st.session_state["add_container"] >= 1:
      st.session_state["add_container"] -= 1


def add_container(row_num):
  with st.container():
    col1, col2, col3 = st.columns(3)
    
    with col1:
      st.write(f"This is left side in {row_num+1} row.")
      
    with col2:
      st.write(f"This is middle side in {row_num+1} row.")
      
    with col3:
      st.write(f"This is right side in {row_num+1} row.")
      
for i in range(st.session_state["add_container"]):
  add_container(i)
  
# ボタンを押すとヴィジェットを追加する
st.subheader("5.ボタンを押すとヴィジェットを追加する")

if 'unique_id' not in st.session_state:
  st.session_state["unique_id"] = []

col5, col6 = st.columns(2)

with col5:
  if st.button("追加", key=6):
    st.session_state["unique_id"].append(uuid.uuid1())

with col6:
  if st.button("削除", key=7):
    st.session_state["unique_id"].pop(-1)
    
for unique_id in st.session_state["unique_id"]:
  
  with st.container():
    col7, col8 = st.columns(2)

    with col7:
      slider_value = st.slider(
        "数値",
        min_value=0,
        max_value=14,
        value=0,
        key=unique_id
      )
    with col8:
      st.write("")
      st.write("")
      st.write(slider_value)