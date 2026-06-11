from django.db import models

# Create your models here.

class ModerationResult(models.Model):

    text = models.TextField()

    category = models.CharField(max_length=50)
    confidence = models.FloatField(default=0)

    toxicity_score = models.FloatField(default=0)
    threat_score = models.FloatField(default=0)
    severe_toxicity_score = models.FloatField(default=0)
    obscene_score = models.FloatField(default=0)
    insult_score = models.FloatField(default=0)
    identity_attack_score = models.FloatField(default=0)

    risk_level = models.CharField(max_length=20)
    allowed = models.BooleanField(default=True)
    report_generated = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)



class IncidentReport(models.Model):
    text = models.TextField()

    risk_level = models.CharField(max_length=20)

    reason = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.risk_level} - {self.created_at}"