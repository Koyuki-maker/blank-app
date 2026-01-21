import streamlit as st
import pandas as pd

st.title("☕🍵 Cafe & Tea Preference Diagnosis")

st.write("Please answer the questions below (1 = low, 5 = high)")

bitterness = st.slider("How much do you like bitterness?", 1, 5, 3)
sweetness = st.slider("How much do you like sweetness?", 1, 5, 3)
aroma = st.slider("How important is aroma?", 1, 5, 3)
richness = st.slider("Do you prefer rich flavors?", 1, 5, 3)
milk = st.slider("How much do you like milk-based drinks?", 1, 5, 3)

if st.button("Diagnose"):
    scores = {
        "Bitterness": bitterness,
        "Sweetness": sweetness,
        "Aroma": aroma,
        "Richness": richness,
        "Milk": milk
    }

    if milk >= 4 and sweetness >= 4:
        result = "Milk & Sweet Type"
        recommendation = "Cafe Latte, Cafe Mocha, Milk Tea"
    elif aroma >= 4:
        result = "Aroma Lover Type"
        recommendation = "Earl Grey, Flavored Tea"
    elif bitterness >= 4 and richness >= 4:
        result = "Bitter & Rich Type"
        recommendation = "Black Coffee, Darjeeling Tea"
    else:
        result = "Light & Balanced Type"
        recommendation = "Americano, Straight Tea"

    st.subheader("🧾 Your Result")
    st.write(f"**Type:** {result}")
    st.write(f"**Recommended Drinks:** {recommendation}")

    df = pd.DataFrame.from_dict(scores, orient="index", columns=["Score"])
    st.bar_chart(df)

