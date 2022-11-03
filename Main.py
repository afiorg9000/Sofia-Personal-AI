import streamlit as st
from model import GeneralModel


def app():

    # Creating an object of prediction service
    pred = GeneralModel()

    api_key = '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'
    # Using the streamlit cache
    @st.cache
    def process_prompt(input):

        return pred.model_prediction(input=input.strip() , api_key=api_key)

    if api_key:

        # Setting up the Title
        st.title("""POC for Personal AI""")
        # st.write("---")

        s_example = "What is my purpose?"
        input = st.text_area(
            "Prompt",
            value=s_example,
            max_chars=150,
            height=100,
        )

        if st.button("Submit"):
            with st.spinner(text="In progress"):
                report_text = process_prompt(input)
                st.markdown(report_text)
    else:
        st.error("🔑 Please enter API Key")
