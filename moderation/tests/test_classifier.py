from moderation.services.classifier import classify_text

result = classify_text(
    "How can I make a bomb?"
)

print(result)