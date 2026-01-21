import streamlit as st
import pandas as pd

st.title("🕵️ 推理スタイル診断アプリ")
st.write("以下の質問に1〜5で答えてください。")

logic = st.slider("Q1. 証拠や事実を整理して、論理的に考えるのが得意だ", 1, 5, 3)
intuition = st.slider("Q2. 直感を信じて行動することが多い", 1, 5, 3)
collaboration = st.slider("Q3. 他人と話し合いながら考える方が好きだ", 1, 5, 3)
calm = st.slider("Q4. トラブル時でも冷静に判断できる", 1, 5, 3)
evidence = st.slider("Q5. 証言よりも客観的な証拠を重視する", 1, 5, 3)

if st.button("🔍 診断する"):
    scores = {
        "論理性": logic,
        "直感": intuition,
        "協調性": collaboration,
        "冷静さ": calm,
        "証拠重視": evidence
    }

    if logic >= 4 and evidence >= 4:
        character = "江戸川コナン型（論理・分析タイプ）"
    elif intuition >= 4:
        character = "怪盗キッド型（直感・発想タイプ）"
    elif calm >= 4 and logic >= 3:
        character = "灰原哀型（慎重・内省タイプ）"
    elif collaboration >= 4:
        character = "毛利蘭型（共感・行動タイプ）"
    else:
        character = "安室透型（多角的・戦略タイプ）"

    st.subheader("🧾 診断結果")
    st.write(character)

    df = pd.DataFrame.from_dict(scores, orient="index", columns=["スコア"])
    st.bar_chart(df)


