import streamlit as st
from llm_utils import get_sql_from_question
from db_utils import query_db

st.set_page_config(page_title="GenAI E-commerce Chatbot", layout="centered")

st.title("🛍️ GenAI SQL Chatbot")
st.write("Ask anything about your e-commerce data.")

# Session chat history
if "chat" not in st.session_state:
    st.session_state.chat = []

# Chat input
question = st.text_input("Ask your question:")

if st.button("Submit") and question:
    with st.spinner("Thinking..."):
        # Get SQL from Gemini
        sql = get_sql_from_question(question)

        # Query the database
        result_df = query_db(sql)

        # Save to chat history
        st.session_state.chat.append({
            "question": question,
            "sql": sql,
            "result": result_df
        })

# Show conversation history
for chat in reversed(st.session_state.chat):
    st.markdown(f"**🧠 You:** {chat['question']}")
    st.markdown(f"**🧾 SQL:**\n```sql\n{chat['sql']}\n```")
    st.markdown("**📊 Result:**")
    st.dataframe(chat['result'], use_container_width=True)
