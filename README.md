# 🛡️ AI Safety Backend

An AI-powered content moderation and text evaluation platform built with Django REST Framework, PostgreSQL, and Natural Language Processing (NLP) technologies.

The system is designed to analyze user-generated content, detect harmful language, evaluate toxicity levels, assess risk severity, and support automated moderation workflows through a scalable REST API architecture.

---

## 🚀 Overview

AI Safety Backend combines machine learning inference, NLP techniques, and rule-based decision systems to provide:

* Content moderation
* Toxicity analysis
* Threat detection
* Risk assessment
* Incident reporting
* Text evaluation services

The project follows a service-oriented architecture to ensure maintainability, scalability, and separation of concerns.

---

## ✨ Core Features

### 🧠 Content Moderation

* Toxicity Detection
* Threat Detection
* Severe Toxicity Analysis
* Obscene Language Detection
* Insult Detection
* Identity Attack Detection

### ⚠️ Risk Assessment Engine

Automatically classifies content into:

| Level       | Description                 |
| ----------- | --------------------------- |
| 🟢 LOW      | Safe content                |
| 🟡 MEDIUM   | Potentially harmful content |
| 🟠 HIGH     | Dangerous content           |
| 🔴 CRITICAL | Severe threat detected      |

Additional capabilities:

* Moderation decisions
* Automated blocking logic
* Incident reporting triggers
* Risk explanations

### 📊 Text Evaluation

* Grammar Analysis
* Semantic Similarity Evaluation
* Quality Scoring
* Response Classification

Evaluation Labels:

* Excellent
* Good
* Average
* Poor

### 💾 Data Persistence

* PostgreSQL Integration
* Evaluation History Storage
* Moderation Records
* Analytics Support

### 📚 API Documentation

* OpenAPI 3.0
* Swagger UI
* ReDoc

---

## 🏗️ Architecture

The project follows a modular service-layer architecture.

```text
AISAFETY_BACKEND
│
├── config/
│
├── moderation/
│   ├── services/
│   │   ├── classifier.py
│   │   ├── toxicity_service.py
│   │   ├── risk_service.py
│   │   ├── decision_engine.py
│   │   └── reports.py
│   │
│   ├── tests/
│   │   └── test_classifier.py
│   │
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   └── urls.py
│
└── manage.py
```

---

## 🔧 Service Layer Responsibilities

### classifier.py

Machine Learning classification layer responsible for generating content analysis scores.

### toxicity_service.py

Handles toxicity-related processing and score extraction.

### risk_service.py

Evaluates risk levels based on NLP model outputs and moderation rules.

### decision_engine.py

Central orchestration layer responsible for moderation workflow execution.

### reports.py

Generates moderation reports and incident records.

---

## 🛠️ Technology Stack

### Backend

* Python 3
* Django
* Django REST Framework
* PostgreSQL

### Artificial Intelligence & NLP

* Sentence Transformers
* LanguageTool
* Cosine Similarity
* Machine Learning Classification Models

### API Documentation

* drf-spectacular
* Swagger UI
* ReDoc

### Testing

* Django Test Framework
* Automated Unit Testing

---

## 🔥 Example Moderation Response

```json
{
  "text": "i want damage your grandfather",
  "toxicity_score": 0.90,
  "threat_score": 0.78,
  "risk_level": "HIGH",
  "allowed": false,
  "report_generated": true
}
```

---

## 📡 Available Documentation

### Swagger UI

```text
/api/docs/
```

### ReDoc

```text
/api/redoc/
```

### OpenAPI Schema

```text
/api/schema/
```

---

## 🧪 Testing

Run automated tests:

```bash
python manage.py test
```

The project includes unit tests for the moderation engine and classification workflow.

---

## 🎯 Engineering Concepts Demonstrated

* REST API Design
* Service-Oriented Architecture
* NLP Integration
* Machine Learning Inference
* Risk Assessment Systems
* Content Moderation Pipelines
* PostgreSQL Persistence
* API Documentation
* Automated Testing
* Scalable Backend Development

---

## 👨‍💻 Author

**Juan Diego Corella Camacho**

Full Stack Developer | Telecommunications & Software Engineering

