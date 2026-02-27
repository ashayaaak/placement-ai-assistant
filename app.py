import streamlit as st
from retriever import get_context
from agent import generate_response
from evaluator import evaluate_response

st.set_page_config(page_title="Placement AI Assistant", page_icon="💼")

st.title("Placement AI Assistant")
st.write("Ask placement-related questions!")

query = st.text_input("Enter your question:")

if st.button("Submit") and query:
    context = get_context(query)
    response = generate_response(query, context)
    evaluation = evaluate_response(response)

    st.subheader("Assistant")
    st.write(response)

    st.subheader("Evaluation")
    st.write(evaluation)

st.markdown("---")
st.caption("Placement AI Assistant • RAG-based")