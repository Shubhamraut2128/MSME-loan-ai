# MSME Loan AI 🚀
 
[![Streamlit](https://img.shields.io/badge/Streamlit-1.54-orange)]([https://streamlit.io/](https://msme-loan-ai-6nsmbpn9lq33o9bfvg2tiw.streamlit.app/)  

A production-ready AI system for **MSME loan eligibility, risk scoring, and policy-based decisioning**.  
It combines **FastAPI backend**, **ML risk assessment models**, **RAG-based policy explanations**, and a **Streamlit frontend**.

---

## 🗂 Project Structure
```
msme-loan-ai/
├── app/ # Backend (FastAPI)
│ ├── main.py # FastAPI entry point
│ ├── config.py # Configuration & constants
│ ├── api/
│ │ └── routes.py # API endpoints
│ ├── services/
│ │ ├── document_parser.py # Document extraction / OCR
│ │ ├── risk_model.py # ML risk scoring
│ │ ├── rag_engine.py # Policy explanation engine (RAG)
│ │ └── decision_engine.py # Combines risk + policy for final decision
│ ├── models/
│ │ └── trained_model.pkl # ML model (use Git LFS if >100MB)
│ └── data/
│ └── rbi_policies/ # RBI policy documents for RAG engine
├── frontend/ # Frontend (Streamlit)
│ └── app.py # Streamlit interface
├── requirements.txt # Python dependencies
└── README.md # Project overview

```
---

## ⚙️ Installation

1. **Clone the repository**

```bash
git clone https://github.com/<your-username>/msme-loan-ai.git
cd msme-loan-ai

Create and activate a virtual environment

python -m venv venv
# Windows
venv\Scripts\activate
# Linux / Mac
source venv/bin/activate

Install dependencies

pip install -r requirements.txt
🚀 Run Backend (FastAPI)
uvicorn app.main:app --reload

Access APIs at http://127.0.0.1:8000

Example endpoint:

POST /apply_loan
{
  "applicant_name": "John Doe",
  "business_turnover": 2500000,
  "documents": ["doc1.pdf", "doc2.pdf"]
}
🎨 Run Frontend (Streamlit)
streamlit run frontend/app.py

Open the URL in your browser (http://localhost:8501)

Upload documents, view risk scores, and see loan decisions + policy explanations.
```
📦 Dependencies

fastapi – Backend framework

uvicorn – ASGI server for FastAPI

pandas / numpy – Data processing

scikit-learn – ML risk scoring

streamlit – Frontend UI

transformers (optional) – For RAG-based policy explanations

tqdm – Progress bars

Full list available in requirements.txt.

---
📝 Decision Logic

The final loan decision is determined by:

def final_decision(risk_score, eligibility_answer):
    if risk_score < 40 and "eligible" in eligibility_answer.lower():
        return "Approved"
    elif risk_score < 60:
        return "Review Required"
    else:
        return "Rejected"

Risk score <40 and eligible → Approved

Risk score 40–59 → Review Required

Risk score ≥60 → Rejected

---

⚡ Deployment

Streamlit Cloud, Heroku, or any cloud server can host the app.

Ensure requirements.txt includes uvicorn for ASGI apps.

Keep repo size small: exclude venv/ and track large ML models via Git LFS.

Ensure trained_model.pkl is available either in the repo (via LFS) or downloaded at runtime.

---
👨‍💻 Author

Shubham Raut – Data Scientist
