import streamlit as st
from graph.workflow import graph

st.title("FinPilot AI")
query = st.text_input(
    "Ask me anything"
)
if st.button("Submit"):
    result = graph.invoke(
        {
            "query": query
        }
    )
    st.write(result["response"])