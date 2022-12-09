# 📄  Question Answering System
A simple Q&A webapp made using streamlit to process text built using RoBerTa Model from Huggingface Transformers 🤗.

![plain_text](https://user-images.githubusercontent.com/29462447/152040979-3746ce6e-fbd5-4c00-8b6b-50b526a9ba6b.gif)

![pdf](https://user-images.githubusercontent.com/29462447/152040990-2fc3645a-4a7b-4a1b-a308-4b3ceae85407.gif)


## Installation:
* Simply run the command ***pip install -r requirements.txt*** to install the dependencies.

## Usage:
1. Clone this repository and install the dependencies as mentioned above.
2. Run the command: 
```
streamlit run app.py
```
3. Navigate to http://localhost:8501 in your web-browser.
4. Streamlit allows us to upload files of **max. 200MB**. If you want to have more size for uploading audio files, execute the command :
```
streamlit run app.py --server.maxUploadSize=1028
```

## Results:
1. Perform Q&A on random text on the fly!
![plain_text](https://user-images.githubusercontent.com/29462447/152040979-3746ce6e-fbd5-4c00-8b6b-50b526a9ba6b.gif)


2. Upload your document ***(supports PDFs, Word Files, Text files)*** and perform Q&A:

![docx](https://user-images.githubusercontent.com/29462447/152041322-1ed4e76f-614c-40ec-b9e6-b2274f77ff87.gif)
![pdf](https://user-images.githubusercontent.com/29462447/152040990-2fc3645a-4a7b-4a1b-a308-4b3ceae85407.gif)
