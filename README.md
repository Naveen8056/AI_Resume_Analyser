# AI-Resume-Analyser
A local, privacy-preserving AI tool that analyzes resumes against job descriptions using LLaMA 2 via Ollama and LangChain.
It provides ATS scoring, skill gap analysis, project suggestions, and downloadable feedback — all without using cloud APIs.

🚀 Features:

  ✅ Upload resume as PDF and input a job description
  
  ✅ Analyze resume suitability using a local LLaMA 2 model
  
  ✅ Get ATS score and explain skill matches/mismatches
  
  ✅ Recommend new skills + projects with step-by-step roadmaps
  
  ✅ Download full analysis as .txt feedback report
  
  🔒 Runs completely offline — no API keys required

# Tech Stack
| Component  | Tool/Library                                            |
| ---------- | ------------------------------------------------------- |
| LLM        | [LLaMA 2](https://ollama.com/library/llama2) via Ollama |
| Framework  | [LangChain](https://docs.langchain.com/)                |
| UI         | [Streamlit](https://streamlit.io)                       |
| PDF Parser | `pdfplumber`                                            |

📦 Installation

✅ 1. Clone the Repository

       git clone https://github.com/Naveen8056/AI-Resume-analyzer.git cd AI-Resume-analyzer
    
✅ 2. Install Dependencies

       pip install -r requirements.txt
    
✅ 3. Install Ollama and Pull LLaMA 2

        # Install Ollama (if not installed)
        curl -fsSL https://ollama.com/install.sh | sh
        # Pull LLaMA 2 model
        ollama pull llama2
    
🧠 Usage

1.Run the local LLaMA model in a separate terminal:

       ollama run llama2
    
2.Start the Streamlit app:

       streamlit run app.py
    
3.In your browser:

        1.Upload a resume in PDF format.
        2.Paste a job description.
        3.Click "Analyze Resume" to view and download feedback.
    
📥 Output Includes:

✅ ATS Score with Explanation

✅ Skills in Resume & Skills Missing

✅ Skill Recommendations

✅ 2 Suggested Projects with Learning Roadmaps

✅ Option to Download Feedback as .txt





