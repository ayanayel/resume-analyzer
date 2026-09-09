from flask import Flask, render_template, request, redirect
from analyzer import analyze
from nlp_utils import extract_text_from_file
from database import save_analysis, get_analyses, delete_analysis

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/analyze", methods=["POST"])
def analyze_route():

    job = request.form.get("job_description", "")
    resume_text = request.form.get("resume_text", "")
    resume_file = request.files.get("resume_file")

    if resume_file and resume_file.filename:

        resume_text = extract_text_from_file(
            resume_file,
            resume_file.filename
        )

    if not resume_text.strip():
        return "Please upload a CV or paste your CV text."

    result = analyze(resume_text, job)

    save_analysis(
        result["score"],
        result["matched"],
        result["missing"],
        result["weaknesses"]
    )

    return render_template(
        "result.html",
        result=result
    )


@app.route("/history")
def history():

    analyses = get_analyses()

    total = len(analyses)

    if total > 0:
        avg_score = round(sum(a[1] for a in analyses) / total)
        best_score = max(a[1] for a in analyses)
    else:
        avg_score = 0
        best_score = 0

    return render_template(
        "history.html",
        analyses=analyses,
        total=total,
        avg_score=avg_score,
        best_score=best_score
    )


@app.route("/delete/<int:id>", methods=["POST"])
def delete(id):

    delete_analysis(id)

    return redirect("/history")


if __name__ == "__main__":
    app.run(debug=True)