from .classifier import classify_text
from .risk_service import evaluate_risk
from .reports import generate_incident_report


def analyze_content(text):

    scores = classify_text(text)

    risk_result = evaluate_risk(scores)

    report_id = None

    if risk_result["report_generated"]:

        report = generate_incident_report(
            text=text,
            risk_result=risk_result
        )

        report_id = report.id

    return {
        **scores,
        **risk_result,
        "incident_report_id": report_id
    }