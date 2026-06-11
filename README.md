# 🚀 AI Content Moderation & Text Evaluation API

A production-oriented backend application built with **Django REST Framework**, **PostgreSQL**, and **Natural Language Processing (NLP)** technologies to evaluate text quality, detect harmful content, classify risk levels, and generate moderation insights through a RESTful API.

This platform combines grammar analysis, semantic similarity, toxicity detection, and automated risk assessment to support modern content moderation workflows.

---

## ✨ Features

### 📝 Text Evaluation

* Grammar analysis using LanguageTool
* Semantic similarity evaluation using Sentence Transformers
* Automated scoring engine
* Quality classification:

  * 🟢 Excellent
  * 🔵 Good
  * 🟡 Average
  * 🔴 Poor

### 🛡️ Content Moderation

* Toxicity Detection
* Threat Detection
* Severe Toxicity Analysis
* Obscene Content Detection
* Insult Detection
* Identity Attack Detection

### ⚠️ Risk Assessment Engine

* Automated risk classification
* Multi-factor scoring system
* Moderation decisions
* Incident report generation

Risk Levels:

| Level       | Description                        |
| ----------- | ---------------------------------- |
| 🟢 LOW      | Safe content                       |
| 🟡 MEDIUM   | Potentially harmful content        |
| 🟠 HIGH     | Dangerous content requiring review |
| 🔴 CRITICAL | Severe threat detected             |

### 💾 Data Persistence

* PostgreSQL integration
* Evaluation history storage
* Moderation records
* Statistical analytics

### 📚 API Documentation

* OpenAPI 3.0
* Swagger UI
* ReDoc

---

## 🏗️ Technology Stack

### Backend

* Python
* Django
* Django REST Framework
* PostgreSQL

### 🤖 Artificial Intelligence & NLP

* LanguageTool
* Sentence Transformers
* Cosine Similarity
* Machine Learning Classification Models

### 📖 Documentation

* drf-spectacular
* Swagger UI
* ReDoc

### 🧪 Testing

* Django Test Framework
* Automated API Testing

---

## 🏛️ Architecture

```text
Client
   │
   ▼
Django REST API
   │
   ├── Views
   ├── Serializers
   ├── Services Layer
   │      ├── Evaluation Engine
   │      ├── Toxicity Classifier
   │      ├── Risk Assessment Engine
   │      └── Incident Reporting
   │
   └── PostgreSQL Database
```

The application follows a **service-oriented architecture**, promoting separation of concerns, maintainability, scalability, and testability.

---

## 🔥 Core Capabilities

### 📊 Evaluation Module

Analyze textual responses and generate:

* Grammar Score
* Semantic Relevance Score
* Final Evaluation Score
* Quality Classification
* Processing Metrics

### 🛡️ Moderation Module

Analyze user-generated content and generate:

* Toxicity Metrics
* Threat Indicators
* Risk Classification
* Moderation Decisions
* Incident Reports

---

## 📡 Example Response

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

## 📑 API Documentation

```text
/api/docs/
/api/redoc/
/api/schema/
```

---

## 🎯 Engineering Concepts Demonstrated

* REST API Design
* Service-Oriented Architecture
* NLP Integration
* Machine Learning Inference
* Risk Assessment Systems
* Content Moderation Pipelines
* Data Persistence
* API Documentation
* Automated Testing
* Backend Performance Monitoring

---

## 🚧 Future Improvements

* JWT Authentication
* Role-Based Access Control (RBAC)
* Audit Logging
* Docker Support
* CI/CD Pipelines
* Cloud Deployment
* Real-Time Moderation Dashboard
* Model Versioning

---

## 👨‍💻 Author

**Juan Diego Corella Camacho**

Full Stack Developer | Telecommunications & Systems Engineering

Focused on backend development, API design, artificial intelligence integration, and scalable software solutions.
