import streamlit as st #for web frontend
from aitextgen import aitextgen #for ai text gen

st.title("""
SofAI
Sofia is a text completion AI made for personal use. 
""")
st.sidebar.markdown("# Sofia's Personal Portal")

# instantiate the model / download
ai = aitextgen()

# create a prompt text for the text generation 
#prompt_text = "Python is awesome"

prompt_text = st.text_input(label = "Prompt",
            value = "Sofia is an evolving AI")

with st.spinner("sofAI is at Work..."):
    # text generation
    gpt_text = ai.generate_one(prompt=prompt_text,
            max_length = 100 )
# print ai generated text

print(gpt_text)
st.text_area(label = "Generated Completion", value = gpt_text)
