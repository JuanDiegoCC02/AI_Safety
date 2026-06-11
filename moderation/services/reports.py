from datetime import datetime


def generate_incident_report(text, scores, risk_result):
    return {
        "timestamp": datetime.utcnow().isoformat(),
        "text": text,
        "risk_level": risk_result["risk_level"],
        "allowed": risk_result["allowed"],
        "reason": risk_result["reason"],
        "reasons": risk_result["reasons"],
        "scores": {
            "toxicity": scores.get("toxicity", 0),
            "threat": scores.get("threat", 0),
            "severe_toxicity": scores.get("severe_toxicity", 0),
            "obscene": scores.get("obscene", 0),
            "insult": scores.get("insult", 0),
            "identity_attack": scores.get("identity_attack", 0),
        }
    }