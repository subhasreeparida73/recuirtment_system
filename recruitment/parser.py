import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

SKILLS = [
    "python", "django", "flask", "sql", "mongodb", "javascript", "react",
    "machine learning", "nlp", "deep learning", "pandas", "numpy",
    "git", "tensorflow", "pytorch", "api", "docker", "kubernetes",'C'
]

def clean_text(text):
    text = re.sub(r'\s+', ' ', text)
    text = re.sub(r'[^\w\s]', '', text)
    return text.lower()

def parse_resume(text, job_keywords):
    text = clean_text(text)
    tokens = word_tokenize(text)
    words = [word for word in tokens if word not in stopwords.words('english')]

    # Extract skills
    skills_found = [skill for skill in SKILLS if skill in words]

    # Extract years of experience
    experience = re.findall(r'(\d{1,2})\s*(?:\+)?\s*(?:years|yrs)\s*(?:of)?\s*(?:experience|exp)?', text)
    experience_years = max(map(int, experience)) if experience else 0

    # Scoring based on keyword match
    job_keywords = clean_text(job_keywords).split()
    matched_keywords = [kw for kw in job_keywords if kw in words]
    score = (len(matched_keywords) / len(job_keywords)) * 100 if job_keywords else 0

    return {
        "skills": ", ".join(set(skills_found)),
        "experience_years": experience_years,
        "score": round(score, 2)
    }
    print("Experience matches:",text)