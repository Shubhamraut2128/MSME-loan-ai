from fastapi import APIRouter
from app.services.risk_model import predict_risk
from app.services.rag_engine import build_rag
from app.services.decision_engine import final_decision

router = APIRouter()
qa_system = build_rag()

@router.post("/evaluate")
def evaluate_loan(data: dict):
    risk = predict_risk(data)
    explanation = qa_system.run("Is this MSME eligible as per RBI norms?")
    decision = final_decision(risk, explanation)

    return {
        "risk_score": risk,
        "explanation": explanation,
        "final_decision": decision
    }