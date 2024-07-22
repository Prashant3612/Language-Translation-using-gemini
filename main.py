import os
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import google.generativeai as genai 
from langchain.schema.output_parser import StrOutputParser
from langchain.prompts import ChatPromptTemplate
import streamlit as st
load_dotenv()


st.set_page_config(
    page_title="Translator"  
)
with open('style.css') as f:
    css = f.read()

st.title("Languge Translation with gemini")

st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)

genai.configure(api_key=os.environ["GOOGLE_API_KEY"])

input=st.text_input("Enter the text :")
language=st.text_input("Enter Language")

styled_button = f"<button style='color: black; background-color: white; border: 1px solid #ddd;' class='st-emotion-cache-7ym5gk'>Hover Me!</button>"


model=ChatGoogleGenerativeAI(model="gemini-pro", temperature=0.7)

if st.button("Translate"):
    st.spinner("Loading...")
    prompt_template=ChatPromptTemplate.from_template(
    """
    You are a language translation tool. Auto-detect the input language and convert the {text} into {language} language.

    If {language} provided is not a valid language. Return the output "Not a valid Language"

    """
    )
    chain=prompt_template|model|StrOutputParser()
    result=chain.invoke({"text":input,"language":language})
    # st.markdown(result, unsafe_allow_html=True)
    colored_text = f"<span style='color:red'>{result}</span>"
    st.write(colored_text,unsafe_allow_html=True)



