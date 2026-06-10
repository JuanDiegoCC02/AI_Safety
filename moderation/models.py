from django.db import models

# Create your models here.

class ModerationResult(models.Model):

    text = models.TextField()

    category = models.CharField(
        max_length=50,
        default="unknown"
    )

    risk_level = models.CharField(
        max_length=20,
        default="LOW"
    )

    confidence = models.FloatField(default=0)

    allowed = models.BooleanField(default=True)

    decision = models.CharField(
        max_length=20,
        default="ALLOW"
    )

    report_generated = models.BooleanField(
        default=False
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.category