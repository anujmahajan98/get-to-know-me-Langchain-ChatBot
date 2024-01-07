from typing import Set

from backend.core import run_llm
import streamlit as st
from streamlit_chat import message
from PIL import Image
from io import BytesIO
import base64

# def add_bg_from_local(image_file):
#     with open(image_file, "rb") as image_file:
#         encoded_string = base64.b64encode(image_file.read())
#     st.markdown(
#     f"""
#     <style>
#     .stApp {{
#         background-image: url(data:{"jpeg"};base64,{encoded_string.decode()});
#         background-size: cover
#     }}
#     </style>
#     """,
#     unsafe_allow_html=True
#     )
# background_image = "bg2.jpeg"
# add_bg_from_local(background_image)

# Load your profile image
profile_image = Image.open("Untitled design.png")

# Display profile image in the sidebar
st.sidebar.image(profile_image, use_column_width=True)

# Add LinkedIn, Github, and LeetCode links with icons
st.sidebar.markdown(
    """
    💻 MS CS @ IUB  

    🧳 Actively looking for full time SDE / SWE / Full Stack / Data Science roles starting from May 2024      

    📧 : anujmaha@iu.edu / anujsmahajan1998@gmail.com  

    📞 : +1 8126029653   
      
    🎯 I am a strong Full Stack and Software developer with diverse skills and currently exploring AWS and GenAI.       

    [![](https://content.linkedin.com/content/dam/me/business/en-us/amp/brand-site/v2/bg/LI-Bug.svg.original.svg)](https://www.linkedin.com/in/anujmaha/)   
    [![GitHub](https://img.icons8.com/material-outlined/48/000000/github.png)](https://github.com/anujmahajan98)    
    [Leetocde](https://leetcode.com/anujmah/)    
    """
)

st.header("Get to know Anuj 👨🏻‍💻")
st.header("Ask anything related to me ")

if "user_prompt_history" not in st.session_state:
    st.session_state["user_prompt_history"] = []

if "chat_answers_history" not in st.session_state:
    st.session_state["chat_answers_history"] = []

if "chat_history" not in st.session_state:
    st.session_state["chat_history"] = []



prompt = st.text_input("Prompt", placeholder="eg. Is it a good choice to hire him as SDE ?, What is his work experience ?...")


if prompt:
    with st.spinner("Generating response..."):
        generated_response = run_llm(
            query=prompt, chat_history=st.session_state["chat_history"]
        )
        
        formatted_response = (
            f"{generated_response['answer']}"
        )

        st.session_state.user_prompt_history.append(prompt)
        st.session_state.chat_answers_history.append(formatted_response)
        st.session_state.chat_history.append((prompt, generated_response["answer"]))

if st.session_state["chat_answers_history"]:
    for generated_response, user_query in zip(
        st.session_state["chat_answers_history"],
        st.session_state["user_prompt_history"],
    ):
        message(
            user_query,
            is_user=True,
            avatar_style="adventurer",
            seed=123,
        )
        # message(generated_response)
        st.write(
            f'<div style="word-wrap: break-word;">{generated_response}</div>',
            unsafe_allow_html=True,
        )
