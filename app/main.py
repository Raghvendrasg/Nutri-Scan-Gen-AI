import streamlit as st
from dotenv import load_dotenv
import os

# Load .env before other imports that need env vars
load_dotenv()

from ui_components import show_header, upload_image_ui, prompt_input_ui, display_results
from gpt_handler import analyze_image

def main():
    show_header()
    uploaded_file = upload_image_ui()
    prompt = prompt_input_ui()

    if st.button("Submit",type="primary"):
        if uploaded_file is not None and prompt.strip():
            with st.spinner("Analyzing image..."):
                result = analyze_image(uploaded_file, prompt)
            # display_results(result)
            display_results(result, uploaded_file)
        else:
            st.error("Please upload an image and enter a prompt.")

if __name__ == "__main__":
    main()
