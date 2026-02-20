def final_decision(risk_score, eligibility_answer):
    # Validate inputs
    if risk_score is None or eligibility_answer is None:
        return {"status": "Error", "reason": "Missing input values"}

    # Normalize eligibility_answer
    eligibility = eligibility_answer.lower()

    # Decision logic
    if risk_score < 40 and "eligible" in eligibility:
        return {"status": "Approved", "reason": "Low risk & policy eligibility confirmed"}
    elif risk_score < 60:
        return {"status": "Review Required", "reason": "Moderate risk, manual review needed"}
    else:
        return {"status": "Rejected", "reason": "High risk or ineligible per policy"}