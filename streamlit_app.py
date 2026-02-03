import streamlit as st
import pandas as pd
from supabase import create_client

# ===============================
# Supabase 接続設定
# ===============================
try:
    url = st.secrets["SUPABASE_URL"]
    key = st.secrets["SUPABASE_KEY"]
    supabase = create_client(url, key)
except Exception as e:
    st.error("Supabase に接続できません。secrets.toml を確認してください。")
    st.stop()

# ===============================
# アプリUI
# ===============================
st.title("🕵️ 推理スタイル診断アプリ")
st.write("以下の質問に1〜5で答えてください。")

logic = st.slider("Q1. 論理的に考えるのが得意", 1, 5, 3)
intuition = st.slider("Q2. 直感を信じる", 1, 5, 3)
collaboration = st.slider("Q3. 話し合いながら考える", 1, 5, 3)
calm = st.slider("Q4. 冷静に判断できる", 1, 5, 3)
evidence = st.slider("Q5. 証拠を重視する", 1, 5, 3)

# ===============================
# 診断ボタン
# ===============================
if st.button("🔍 診断する"):

    if logic >= 4 and evidence >= 4:
        character = "江戸川コナン型（論理・分析）"
    elif intuition >= 4:
        character = "怪盗キッド型（直感・発想）"
    elif calm >= 4 and logic >= 3:
        character = "灰原哀型（慎重・内省）"
    elif collaboration >= 4:
        character = "毛利蘭型（共感・行動）"
    else:
        character = "安室透型（多角的・戦略）"

    # Supabase 保存
    try:
        supabase.table("detective_results").insert({
            "logic": logic,
            "intuition": intuition,
            "collaboration": collaboration,
            "calm": calm,
            "evidence": evidence,
            "character": character
        }).execute()

        st.success("診断結果を保存しました！")

    except Exception as e:
        st.error("診断結果の保存に失敗しました")
        st.error(e)
        st.stop()

    # 結果表示
    st.subheader("🧾 診断結果")
    st.write(character)

    df = pd.DataFrame(
        {
            "スコア": [logic, intuition, collaboration, calm, evidence]
        },
        index=["論理性", "直感", "協調性", "冷静さ", "証拠重視"]
    )

    st.bar_chart(df)

# ===============================
# 履歴表示
# ===============================
st.divider()
st.subheader("📊 過去の診断履歴（最新10件）")

data = (
    supabase
    .table("detective_results")
    .select("*")
    .order("created_at", desc=True)
    .limit(10)
    .execute()
)

if data.data:
    for r in data.data:
        st.write(
            f"{r['created_at']}｜{r['character']} "
            f"(論理:{r['logic']}, 直感:{r['intuition']})"
        )
else:
    st.write("まだ診断履歴がありません。")
