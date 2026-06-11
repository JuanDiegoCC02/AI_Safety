def evaluate_risk(scores):
    threat = scores.get("threat", 0.0)
    toxicity = scores.get("toxicity", 0.0)
    severe = scores.get("severe_toxicity", 0.0)
    obscene = scores.get("obscene", 0.0)
    insult = scores.get("insult", 0.0)
    identity_attack = scores.get("identity_attack", 0.0)

    reasons = []

    # Collect explanations
    if threat >= 0.50:
        reasons.append("Threat detected")

    if toxicity >= 0.50:
        reasons.append("High toxicity detected")

    if severe >= 0.50:
        reasons.append("Severe toxic content detected")

    if obscene >= 0.50:
        reasons.append("Obscene language detected")

    if insult >= 0.50:
        reasons.append("Insulting language detected")

    if identity_attack >= 0.50:
        reasons.append("Identity attack detected")

    # Risk classification
    if threat >= 0.80:
        return {
            "risk_level": "CRITICAL",
            "allowed": False,
            "report_generated": True,
            "reason": "Critical threat detected",
            "reasons": reasons
        }

    if threat >= 0.50 or severe >= 0.70:
        return {
            "risk_level": "HIGH",
            "allowed": False,
            "report_generated": True,
            "reason": "High-risk content detected",
            "reasons": reasons
        }

    if toxicity >= 0.50:
        return {
            "risk_level": "MEDIUM",
            "allowed": True,
            "report_generated": False,
            "reason": "Potentially harmful content detected",
            "reasons": reasons
        }

    return {
        "risk_level": "LOW",
        "allowed": True,
        "report_generated": False,
        "reason": "Content considered safe",
        "reasons": ["No significant risk indicators detected"]
    }