# SkillMatch-AI: Resume ATS Analyzer

## Overview

SkillMatch-AI is a web-based Applicant Tracking System (ATS) Resume Analyzer developed using Python and Flask. The application helps job seekers evaluate their resumes against a target job description by identifying matched skills, missing skills, learning recommendations, and resume improvement suggestions.

The system generates an ATS compatibility score, provides actionable recommendations, creates downloadable PDF reports, and stores analysis history for future reference.

---

## Live Demo

https://skillmatch-ai-pdfv.onrender.com

---

## Features

### Resume Analysis
- PDF Resume Upload
- ATS Score Calculation
- Matched Skills Detection
- Missing Skills Analysis

### Intelligent Recommendations
- Learning Recommendations
- Resume Improvement Suggestions
- Skill Gap Analysis

### Resume Evaluation
- Resume Strength Assessment
- Resume Completeness Checker
- Education Detection
- Skills Detection
- Projects Detection
- Certifications Detection
- Experience Detection

### Reporting & Tracking
- PDF Report Generation
- Analysis History Tracking
- Interactive Dashboard
- Skill Analysis Charts
- SQLite Database Storage

---

## Technology Stack

### Frontend
- HTML5
- Bootstrap 5

### Backend
- Python
- Flask

### Database
- SQLite

### Libraries Used
- PyPDF2
- Matplotlib
- ReportLab
- Gunicorn

### Deployment
- Render

---

## System Workflow

1. User uploads a PDF resume.
2. Resume text is extracted using PyPDF2.
3. User enters a job description.
4. ATS engine compares resume content with job requirements.
5. Matched and missing skills are identified.
6. ATS score is calculated.
7. Learning recommendations are generated.
8. Resume improvement suggestions are provided.
9. Resume strength and completeness are evaluated.
10. PDF report is generated.
11. Analysis history is stored in SQLite database.

---

## Project Structure

```text
SkillMatch_AI
│
├── app.py
├── utils.py
├── database.py
├── requirements.txt
├── Procfile
│
├── templates/
│   ├── index.html
│   ├── result.html
│   └── history.html
│
├── static/
│
├── Results/
│
└── ats.db
```

---

## Installation

### Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/SkillMatch-AI.git
cd SkillMatch-AI
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

Windows:

```bash
venv\Scripts\activate
```

Linux/Mac:

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Application

```bash
python app.py
```

Application will run at:

```text
http://127.0.0.1:5000
```

---

## Future Enhancements

- OCR Support for Scanned Resumes
- AI-Based Semantic Skill Matching
- NLP-Based Resume Analysis
- User Authentication System
- Personalized Career Roadmap Generator
- Cloud Database Integration
- Resume Ranking System

---

## Learning Outcomes

Through this project, I gained practical experience in:

- Flask Web Development
- PDF Processing using PyPDF2
- Data Visualization using Matplotlib
- SQLite Database Integration
- PDF Report Generation
- Frontend Development using Bootstrap
- Git & GitHub Version Control
- Cloud Deployment using Render

---

## Author

**Vedhavarshini N**

Electronics and Communication Engineering

SRM Easwari Engineering College, Chennai

Live Demo: https://skillmatch-ai-pdfv.onrender.com

---

## License

This project is developed for educational and learning purposes.
