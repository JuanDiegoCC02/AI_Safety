def evaluate_risk(scores):

    threat = scores.get("threat", 0.0)
    toxicity = scores.get("toxicity", 0.0)
    severe = scores.get("severe_toxicity", 0.0)

    reasons = []

    if threat >= 0.50:
        reasons.append("Threat detected")

    if toxicity >= 0.50:
        reasons.append("High toxicity detected")

    if severe >= 0.50:
        reasons.append("Severe toxic content detected")

    risk_score = (
        threat * 0.5 +
        toxicity * 0.3 +
        severe * 0.2
    )

    if risk_score >= 0.80:
        return {
            "risk_score": round(risk_score, 2),
            "risk_level": "CRITICAL",
            "allowed": False,
            "report_generated": True,
            "reason": "Critical content detected",
            "reasons": reasons
        }

    if risk_score >= 0.60:
        return {
            "risk_score": round(risk_score, 2),
            "risk_level": "HIGH",
            "allowed": False,
            "report_generated": True,
            "reason": "High-risk content detected",
            "reasons": reasons
        }

    if risk_score >= 0.30:
        return {
            "risk_score": round(risk_score, 2),
            "risk_level": "MEDIUM",
            "allowed": True,
            "report_generated": False,
            "reason": "Potentially harmful content",
            "reasons": reasons
        }

    return {
        "risk_score": round(risk_score, 2),
        "risk_level": "LOW",
        "allowed": True,
        "report_generated": False,
        "reason": "Content considered safe",
        "reasons": ["No significant risk indicators detected"]
    }