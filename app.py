import streamlit as st
import cv2
import os
from PIL import Image
from qa_funcs import generate_answer, extract_text_txt, extract_text_pdf, extract_text_docx
from streamlit_lottie import st_lottie
import requests


def load_lottieurl(url: str):
    r = requests.get(url) #Make a request to a web page, and return the status code:
    if r.status_code != 200: #200 is the HTTP status code for "OK", a successful response.
        return None
    return r.json() 


st.set_page_config(
    page_title="Question And Answering",
    page_icon="✨",
    layout="centered",
    initial_sidebar_state="auto",
     menu_items={ #Configure the menu that appears on the top-right side of this app.
            'About': 'https://www.linkedin.com/in/harsh-kashyap-79b87b193/', #A markdown string to show in the About dialog. Used my linkedIn id
     }
)


upload_path = "uploads/"
download_path = "downloads/"


side1 = load_lottieurl("https://assets10.lottiefiles.com/packages/lf20_1a8dx7zj.json") #get the animated gif from file
side2 = load_lottieurl("https://assets2.lottiefiles.com/packages/lf20_l5qvxwtf.json") #get the animated gif from file

with st.sidebar:
    st_lottie(side1, key="Side1", height=200) #change the size to height 400
format_type = st.sidebar.selectbox('Apply Question and Answering on? 🎯',["Plain Text","Documents"])
with st.sidebar:
    st_lottie(side2, key="Side2", height=200) 
dashboard1 = load_lottieurl("https://assets1.lottiefiles.com/packages/lf20_au4zdsr8.json") #get the animated gif from file
st_lottie(dashboard1, key="Dashboard1", height=400) #change the size to height 400

st.title("Deep Question and Answering System 🗣")
st.markdown("##") 

#return the animated gif


if format_type == "Plain Text":
    text = st.text_area("Enter your text here: 🎯", height=300)
    ques_text = st.text_area("Enter your Question: 🙋",height=50)
    if st.button("Run"):
        if ques_text is not None and text is not None and ques_text != "" and text != "":
            with st.spinner(f"Fetching your Answer... 💫"):
                ans = generate_answer(text,ques_text)
                st.markdown("Here's the answer 🗣")
                st.balloons()
                st.success('✅ '+ans)
        elif (ques_text is None or ques_text == "") and (text is not None or text != ""):
            st.warning('⚠ Please enter your question! 😯')
        elif (ques_text is not None or ques_text != "") and (text is None or text == "" ):
            st.warning('⚠ Please enter your plain text! 😯')
        else:
            st.warning('⚠ Text fields missing! 😯')

if format_type == "Documents":
    st.info('Supports all popular document formats 📄 - TXT, PDF, DOCX 😉')
    uploaded_file = st.file_uploader("Upload Document 📃", type=["txt","pdf","docx"])
    if uploaded_file is not None:
        with open(os.path.join(upload_path,uploaded_file.name),"wb") as f:
            f.write((uploaded_file).getbuffer())
        if uploaded_file.name.endswith('.txt') or uploaded_file.name.endswith('.TXT'):
            with st.spinner(f"Working... 💫"):
                uploaded_txt_file = os.path.abspath(os.path.join(upload_path,uploaded_file.name))
                downloaded_txt_file = os.path.abspath(os.path.join(download_path,str("processed_"+uploaded_file.name)))
                txt = extract_text_txt(uploaded_txt_file,downloaded_txt_file)

        if uploaded_file.name.endswith('.pdf') or uploaded_file.name.endswith('.PDF'):
            with st.spinner(f"Working... 💫"):
                uploaded_pdf_file = os.path.abspath(os.path.join(upload_path,uploaded_file.name))
                txt = extract_text_pdf(uploaded_pdf_file)

        if uploaded_file.name.endswith('.docx') or uploaded_file.name.endswith('.DOCX'):
            with st.spinner(f"Working... 💫"):
                uploaded_docx_file = os.path.abspath(os.path.join(upload_path,uploaded_file.name))
                txt = extract_text_docx(uploaded_docx_file)

    else:
        st.warning('⚠ Please upload your document 😯')

    ques_text = st.text_area("Enter your Question: 🙋",height=50)
    if st.button("Run"):
        if (ques_text is not None and ques_text != ""):
            with st.spinner(f"Getting your Answer... 💫"):
                    ans = generate_answer(str(txt),ques_text)
                    st.markdown("Here's the answer 🗣")
                    st.balloons()
                    st.success('✅ '+ans)
        else:
            st.warning('⚠ Please enter your question! 😯')


st.markdown("<br><hr><center>Made with ❤️ by <a href='https://www.linkedin.com/in/harsh-kashyap/'><strong>Harsh Kashyap</strong></a></center><hr>", unsafe_allow_html=True)
