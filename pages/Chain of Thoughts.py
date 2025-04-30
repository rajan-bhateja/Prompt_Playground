import streamlit as st

st.title('Chain of Thoughts (COT)')

st.markdown("""
Chain of Thought (CoT) prompting encourages the model to “think aloud” by breaking down reasoning into steps. This improves performance on tasks requiring logic, math, or multi-step reasoning.

📌 How it works:
- Instead of asking directly for an answer, prompt the model to explain its reasoning first.
- Example:
  Prompt: “If Lily has 3 apples and gives 1 to John, how many does she have left? Think step by step.”

🔍 Result:
  “Lily starts with 3 apples. She gives away 1 apple. So she has 3 - 1 = 2 apples left.”
""")