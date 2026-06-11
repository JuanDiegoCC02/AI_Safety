from rest_framework import serializers
from .models import ModerationResult

from .services.classifier import classify_text
from .services.decision_engine import evaluate_risk

# Create your serializers here.

class ModerationResultSerializer(serializers.ModelSerializer):

    class Meta:
        model = ModerationResult
        fields = '__all__'

        read_only_fields = (
            'category',
            'confidence',
            'toxicity_score',
            'threat_score',
            'severe_toxicity_score',
            'obscene_score',
            'insult_score',
            'identity_attack_score',
            'risk_level',
            'allowed',
            'report_generated',
            'created_at',
        )

    def create(self, validated_data):

        text = validated_data['text']

        classification = classify_text(text)

        decision = evaluate_risk(
            classification['scores']
        )

        return ModerationResult.objects.create(

            text=text,

            category=classification['category'],
            confidence=classification['confidence'],

            toxicity_score=float(
                classification['scores']['toxicity']
            ),

            threat_score=float(
                classification['scores']['threat']
            ),

            severe_toxicity_score=float(
                classification['scores']['severe_toxicity']
            ),

            obscene_score=float(
                classification['scores']['obscene']
            ),

            insult_score=float(
                classification['scores']['insult']
            ),

            identity_attack_score=float(
                classification['scores']['identity_attack']
            ),

            risk_level=decision['risk_level'],
            allowed=decision['allowed'],
            report_generated=decision['report_generated']
        )