import streamlit as st
import pdfplumber
from langchain.llms import Ollama
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

# 🧠 Load local LLaMA2 model via Ollama
llm = Ollama(model="llama2")

# 📄 Function to read PDF content
def extract_text_from_pdf(file):
    with pdfplumber.open(file) as pdf:
        return ''.join([page.extract_text() or '' for page in pdf.pages]).strip()

# 🧠 Prompt Template
template = """
You are an AI Resume Advisor.

Given the following resume and job description, do the following:
1. Rate the resume out of 100 for ATS match and explain the score.
2. Extract and list all technical and soft skills from the resume.
3. List missing or weak skills compared to the job description.
4. Recommend 5 new skills to learn.
5. Suggest 2 relevant projects and a roadmap for each.

Resume:
{resume}

Job Description:
{jd}
"""

prompt = PromptTemplate(input_variables=["resume", "jd"], template=template)
chain = LLMChain(llm=llm, prompt=prompt)

# 🚀 Streamlit UI
st.title("🧠 AI Resume Analyzer")

uploaded_file = st.file_uploader("Upload your resume (PDF)", type=["pdf"])
jd_input = st.text_area("Paste Job Description here", height=300)

if st.button("🔍 Analyze Resume"):
    if uploaded_file and jd_input:
        with st.spinner("Analyzing ..."):
            resume_text = extract_text_from_pdf(uploaded_file)
            result = chain.run(resume=resume_text, jd=jd_input)
            st.success("✅ Analysis Complete")
            st.markdown("### 🧠 AI Feedback")
            st.write(result)

            st.download_button(
                "📥 Download Analysis",
                result,
                file_name="resume_analysis.txt",
                mime="text/plain"
            )
    else:
        st.warning("Please upload a resume and paste a job description.")
