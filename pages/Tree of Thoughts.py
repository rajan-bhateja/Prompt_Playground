import streamlit as st

st.title('Tree of Thoughts (TOT)')

st.markdown("""
Tree of Thoughts (ToT) extends Chain of Thought prompting by exploring multiple reasoning paths (or “thought branches”) and selecting the best one. It’s useful for creative writing, problem solving, and strategy tasks.

📌 Concept:
- Think of each possible solution as a branch in a tree.
- The model explores several options, evaluates them, and chooses the best or combines ideas.

🔍 Example:
  “Come up with three different strategies to increase user engagement in a mobile app. Then, choose the most effective one and explain why.”

🧠 ToT encourages breadth and depth before decision-making.
""")