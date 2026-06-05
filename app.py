from flask import Flask, render_template, request
import matplotlib
matplotlib.use('Agg')

import PyPDF2
import matplotlib.pyplot as plt
import os
from reportlab.pdfgen import canvas

from utils import (
    final_ats_score,
    get_strength,
    check_resume_completeness
)

from database import create_table, save_result, get_history

app = Flask(__name__)

create_table()


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/analyze', methods=['POST'])
def analyze():

    file = request.files['resume_file']
    jd_text = request.form.get('jd', '')

    resume_text = ""

    if file.filename.endswith(".pdf"):

        reader = PyPDF2.PdfReader(file)

        for page in reader.pages:

            page_text = page.extract_text()

            if page_text:
                resume_text += page_text

    else:
        return "Please upload PDF file only"

    # ATS Analysis
    score, matched, missing, recommendations, suggestions = final_ats_score(
        resume_text,
        jd_text
    )

    # Resume Strength
    strength = get_strength(score)

    # Resume Completeness
    completeness = check_resume_completeness(
        resume_text
    )

    # Save History
    save_result(file.filename, score)

    # Create Pie Chart
    chart = create_pie_chart(score)

    # Generate PDF Report
    pdf_report = generate_pdf(
        score,
        matched,
        missing
    )

    return render_template(
        "result.html",
        score=score,
        matched=matched,
        missing=missing,
        recommendations=recommendations,
        suggestions=suggestions,
        strength=strength,
        completeness=completeness,
        chart=chart,
        pdf_report=pdf_report
    )


@app.route('/history')
def history():

    records = get_history()

    return render_template(
        "history.html",
        records=records
    )


def create_pie_chart(score):

    score = max(0, min(score, 100))

    plt.figure(figsize=(4, 4))

    plt.pie(
        [score, 100 - score],
        labels=["Matched", "Missing"],
        autopct="%1.1f%%",
        colors=["green", "red"]
    )

    if not os.path.exists("static"):
        os.makedirs("static")

    path = "static/chart.png"

    plt.savefig(path)
    plt.close()

    return path


def generate_pdf(score, matched, missing):

    if not os.path.exists("static"):
        os.makedirs("static")

    pdf_path = "static/ATS_Report.pdf"

    c = canvas.Canvas(pdf_path)

    c.setFont("Helvetica-Bold", 18)
    c.drawString(180, 800, "ATS Resume Report")

    c.setFont("Helvetica", 12)

    c.drawString(50, 760, f"ATS Score: {score}%")

    c.drawString(50, 720, "Matched Skills:")

    y = 700

    for skill in matched:
        c.drawString(70, y, f"- {skill}")
        y -= 20

    y -= 20

    c.drawString(50, y, "Missing Skills:")

    y -= 20

    for skill in missing:
        c.drawString(70, y, f"- {skill}")
        y -= 20

    c.save()

    return pdf_path


if __name__ == "__main__":
    app.run(debug=True)