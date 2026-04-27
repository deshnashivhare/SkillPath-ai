def is_resume(text):

    resume_keywords = [
        "education",
        "experience",
        "skills",
        "projects",
        "internship",
        "objective",
        "certification",
        "summary"
    ]

    text = text.lower()

    count = 0

    for word in resume_keywords:
        if word in text:
            count += 1

    if count >= 2:
        return True
    else:
        return False
