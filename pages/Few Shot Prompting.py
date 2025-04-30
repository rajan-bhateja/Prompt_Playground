import streamlit as st

st.title("Few Shot Prompting")

st.markdown("""
Few-shot prompting involves giving the model a few examples of input-output pairs before the actual query. This helps the model understand the desired task format and improve accuracy.

📌 Use Case:
Great for classification, translation, formatting, or structured tasks.

🔍 Example:
Text: “I love this movie.” → Sentiment: Positive  
Text: “It was too long and dull.” → Sentiment: Negative  
Text: “Visually great, but the plot was weak.” → Sentiment: ?

🧠 Tip:
Include 2–5 examples that match your goal to guide the model effectively.
""")