from resume_parser import extract_resume_text
import re
import json

def extract_candidate_info(text):
    email_pattern = r"[A-Za-z0-9.+%+-]+@[A-Za-z0-9.-]+\.[a-zA-Z]{2,}"
    email = re.findall(email_pattern,text)
    email = email[0] if email else "Not found"

    phone_pattern = r"^\+?[1-9]{1,3}\d{7,14}$"
    phone = re.findall(phone_pattern,text)
    phone = phone[0] if phone else "Not found"

    predefined_skills = [
    # Programming Languages
    "Python", "Java", "C", "C++", "C#", "Go", "Rust", "JavaScript", "TypeScript", "PHP", "Ruby", "Kotlin", "Swift", "R", "MATLAB",

    # Web Development
    "HTML", "CSS", "React", "Angular", "Vue.js", "Next.js", "Node.js", "Express.js", "Django", "Flask", "Spring Boot", "ASP.NET",

    # Databases
    "SQL", "MySQL", "PostgreSQL", "MongoDB", "SQLite", "Oracle", "Redis", "Firebase",

    # Cloud & DevOps
    "AWS", "Azure", "Google Cloud", "Docker", "Kubernetes", "Jenkins", "Terraform", "Git", "GitHub", "GitLab", "CI/CD",

    # Data Science & AI
    "Pandas", "NumPy", "Matplotlib", "Seaborn", "Scikit-learn", "TensorFlow", "Keras", "PyTorch", "Hugging Face", "NLTK", "OpenCV",

    # Cybersecurity
    "Penetration Testing", "Kali Linux", "Metasploit", "Wireshark", "Burp Suite", "OWASP", "Cryptography",

    # Mobile Development
    "Android", "iOS", "React Native", "Flutter", "Xamarin",

    # Other Relevant Skills
    "Machine Learning", "Deep Learning", "Artificial Intelligence", "Data Analysis", "Big Data", "Hadoop", "Spark",
    "Agile", "Scrum", "Problem Solving", "Leadership"
    ]
    found_skills = [skill for skill in predefined_skills if skill.lower() in text.lower()] 

    exp_pattern = r"(\d+)\s*(?:\+?\s*)?(?:years?|yrs?)"
    experience = re.findall(exp_pattern, text)
    experience = experience[0] + " years" if experience else "Not found"

    candidate = {
        "email": email,
        "phone": phone,
        "skills": found_skills,
        "experience": experience
    }
    return candidate

if __name__ == "__main__":
    resume_path = "avanthika_resume.pdf"
    text = extract_resume_text(resume_path)
    candidate_info = extract_candidate_info(text)
    print(json.dumps(candidate_info, indent=4))

    with open("candidate_info.json", "w") as f:
        json.dump(candidate_info, f, indent=4)

