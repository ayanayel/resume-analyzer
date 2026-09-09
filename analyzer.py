def analyze(cv, job):

    skills = [
        "python",
        "java",
        "c++",
        "javascript",
        "flask",
        "django",
        "html",
        "css",
        "sql",
        "mysql",
        "sqlite",
        "mongodb",
        "git",
        "github",
        "docker",
        "machine learning",
        "deep learning",
        "natural language processing",
        "nlp",
        "computer vision",
        "opencv",
        "tensorflow",
        "pytorch",
        "communication",
        "teamwork",
        "leadership",
        "problem solving"
    ]

    cv = cv.lower()
    job = job.lower()

    cv_skills = []
    job_skills = []

    for skill in skills:

        if skill in cv:
            cv_skills.append(skill)

        if skill in job:
            job_skills.append(skill)

    matched = []

    for skill in job_skills:

        if skill in cv_skills:
            matched.append(skill)

    missing = []

    for skill in job_skills:

        if skill not in cv_skills:
            missing.append(skill)

    if len(job_skills) > 0:
        score = len(matched) / len(job_skills) * 100
    else:
        score = 0

    weaknesses = []

    if len(missing) > 0:
        weaknesses.append(
            "Some skills required by the job are missing."
        )

    if "experience" not in cv:
        weaknesses.append(
            "Your CV does not clearly contain an Experience section."
        )

    if "education" not in cv:
        weaknesses.append(
            "Your CV does not clearly contain an Education section."
        )

    if "project" not in cv:
        weaknesses.append(
            "Your CV does not clearly contain a Projects section."
        )

    if "summary" not in cv and "profile" not in cv:
        weaknesses.append(
            "Your CV does not clearly contain a Summary or Profile section."
        )

    if len(cv) < 300:
        weaknesses.append(
            "Your CV contains limited information."
        )

    recommendations = []

    if missing:
        recommendations.append(
            "Add or highlight the missing skills if you actually have them."
        )

    if "experience" not in cv:
        recommendations.append(
            "Add an Experience section with your previous work or training."
        )

    if "education" not in cv:
        recommendations.append(
            "Add your education information."
        )

    if "project" not in cv:
        recommendations.append(
            "Add projects and explain what you built and which technologies you used."
        )

    if "summary" not in cv and "profile" not in cv:
        recommendations.append(
            "Add a short professional summary related to the target job."
        )

    if len(cv) < 300:
        recommendations.append(
            "Add more useful details about your skills, projects and experience."
        )

    if len(recommendations) == 0:
        recommendations.append(
            "Your CV looks good. Try adding measurable achievements."
        )


    sections = {}

    sections["skills"] = round(score)

    sections["experience"] = 100 if "experience" in cv else 0
    sections["education"] = 100 if "education" in cv else 0
    sections["projects"] = 100 if "project" in cv else 0

    return {
        "score": round(score),
        "matched": matched,
        "missing": missing,
        "weaknesses": weaknesses,
        "recommendations": recommendations,
        "sections": sections
    }