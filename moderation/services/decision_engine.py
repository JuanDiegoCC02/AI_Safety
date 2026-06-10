def evaluate_risk(scores):

    threat = scores.get("threat", 0)
    toxicity = scores.get("toxicity", 0)
    severe = scores.get("severe_toxicity", 0)

    if threat > 0.80:
        return {
            "risk_level": "CRITICAL",
            "allowed": False,
            "report_generated": True
        }

    if severe > 0.70:
        return {
            "risk_level": "HIGH",
            "allowed": False,
            "report_generated": True
        }

    if toxicity > 0.50:
        return {
            "risk_level": "MEDIUM",
            "allowed": True,
            "report_generated": False
        }

    return {
        "risk_level": "LOW",
        "allowed": True,
        "report_generated": False
    }