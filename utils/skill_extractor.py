from database.db import get_cursor
import re

def extract_skills(tokens):
    cursor = get_cursor()

    # get skills from DB
    cursor.execute("SELECT name FROM skills")
    db_skills = [row[0].lower().strip() for row in cursor.fetchall()]

    # join full resume text
    full_text = " ".join(tokens).lower()

    # normalize text
    full_text = re.sub(r'[^a-z0-9.+# ]', ' ', full_text)

    detected = set()

    # 🔥 DB-based matching
    for skill in db_skills:
        skill_clean = skill.lower().replace(".", "").replace(" ", "")
        text_clean = full_text.replace(".", "").replace(" ", "")

        if skill_clean in text_clean:
            detected.add(skill)

    # 🔥 EXTRA fallback skills (IMPORTANT)
    extra_skills = [
        "python", "java", "react", "node", "nodejs", "express",
        "mongodb", "mysql", "html", "css", "javascript",
        "tensorflow", "docker", "aws", "flask", "django"
    ]

    for word in tokens:
        if word.lower() in extra_skills:
            detected.add(word.lower())

    print("FULL TEXT:", full_text[:300])
    print("DB SKILLS:", db_skills[:10])
    print("DETECTED SKILLS:", detected)

    return list(detected)
