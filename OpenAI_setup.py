import streamlit as st
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

def main():
    st.set_page_config(
    page_title="My Great ChatGPT",
    page_icon="😄"    
    )
    st.header("My Great ChatGPT 😄")

    if "message_history" not in st.session_state:
        st.session_state.message_history = [
            ("system", "You are a helpful assistant.")
        ]

    llm = ChatOpenAI(temperature=0)

    prompt = ChatPromptTemplate.from_messages([
        *st.session_state.message_history,
        ("user", "{user_input}")
    ])

    output_parser = StrOutputParser()

    chain = prompt | llm | output_parser #上記の３つの処理を連続して行う

    
    if user_input := st.chat_input("聞きたいことを入力してね"):
        with st.spinner("ChatGPT is typing ..."):
            response = chain.invoke({"user_input": user_input})
        
        st.session_state.message_history.append(("user", user_input))
        
        st.session_state.message_history.append(("ai", response))
        
    for role, message in st.session_state.get("message_history", []):
        st.chat_message(role).markdown(message)

if __name__ == '__main__':
    main()



        