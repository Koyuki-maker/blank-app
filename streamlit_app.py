import streamlit as st
from supabase import create_client

# Supabase 接続
supabase = create_client(
    st.secrets["SUPABASE_URL"],
    st.secrets["SUPABASE_KEY"]
)

st.title("📝 Todo リスト管理アプリ")

# 新規 Todo 追加
task = st.text_input("新しいタスクを入力")

if st.button("追加"):
    if task:
        supabase.table("todos").insert({
            "task": task,
            "done": False
        }).execute()
        st.success("追加しました！")
        st.rerun()

st.divider()

# Todo 一覧表示
rows = supabase.table("todos").select("*").order(
    "created_at", desc=True
).execute()

for row in rows.data:
    st.write("✅" if row["done"] else "⬜", row["task"])


