from detoxify import Detoxify

model = Detoxify('original')

def classify_text(text):

    result = model.predict(text)

    highest_category = max(
        result,
        key=result.get
    )

    confidence = float(
        round(result[highest_category] * 100, 2)
    )

    return {
        "category": highest_category,
        "confidence": confidence,
        "scores": result
    }