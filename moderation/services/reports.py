from moderation.models import IncidentReport


def generate_incident_report(text, risk_result):

    report = IncidentReport.objects.create(
        text=text,
        risk_level=risk_result["risk_level"],
        reason=risk_result["reason"]
    )

    return report