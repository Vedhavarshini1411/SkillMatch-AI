import re


def clean(text):

    text = text.lower()

    text = re.sub(r'[^a-z0-9\s]', ' ', text)

    text = re.sub(r'\s+', ' ', text)

    return text


# Learning Recommendations
def get_recommendations(missing):

    skill_courses = {
        "python": "Learn Python Programming",
        "flask": "Learn Flask Fundamentals",
        "git": "Learn Git & GitHub",
        "sql": "Practice SQL Queries",
        "mysql": "Learn MySQL Database",
        "docker": "Learn Docker Basics",
        "aws": "Learn AWS Cloud",
        "html": "Practice HTML",
        "css": "Practice CSS",
        "javascript": "Learn JavaScript"
    }

    recommendations = []

    for skill in missing:

        if skill.lower() in skill_courses:

            recommendations.append(
                skill_courses[skill.lower()]
            )

        else:

            recommendations.append(
                f"Learn {skill}"
            )

    return recommendations


# Resume Improvement Suggestions
def generate_suggestions(missing):

    suggestions = []

    for skill in missing:

        suggestions.append(
            f"Add projects, certifications, or experience related to {skill}"
        )

    return suggestions


# Resume Strength Level
def get_strength(score):

    if score <= 40:
        return "Beginner ⭐"

    elif score <= 70:
        return "Intermediate ⭐⭐"

    else:
        return "Strong Candidate ⭐⭐⭐"


# Resume Completeness Checker
def check_resume_completeness(resume_text):

    resume_text = resume_text.lower()

    completeness = {
        "Education": "education" in resume_text,
        "Skills": "skill" in resume_text,
        "Projects": "project" in resume_text,
        "Certifications": "certification" in resume_text,
        "Experience": "experience" in resume_text
    }

    return completeness


# Main ATS Function
def final_ats_score(resume_text, jd_text):

    resume_text = clean(resume_text)

    jd_text = clean(jd_text)

    resume_words = set(resume_text.split())

    jd_words = set(jd_text.split())

    if len(jd_words) == 0:

        return (
            0,
            set(),
            set(),
            [],
            []
        )

    matched = resume_words.intersection(jd_words)

    missing = jd_words - resume_words

    score = (len(matched) / len(jd_words)) * 100

    recommendations = get_recommendations(missing)

    suggestions = generate_suggestions(missing)

    return (
        round(score, 2),
        matched,
        missing,
        recommendations,
        suggestions
    )