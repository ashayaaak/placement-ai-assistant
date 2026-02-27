def generate_response(query, context):
    query_lower = query.lower()

    placement_keywords = [
        "interview", "aptitude", "resume", "role",
        "career", "skills", "placement", "job", "become"
    ]

    # Handle unrelated queries
    if not any(word in query_lower for word in placement_keywords):
        return (
            "This assistant is designed for placement support only.\n"
            "Please ask about interviews, skills, aptitude, resumes, or job roles."
        )

    # Skill gap feature
    if "become" in query_lower or "skills" in query_lower:
        return skill_gap_analysis(query)

    elif "interview" in query_lower:
        return "Interview Questions:\n" + context

    elif "aptitude" in query_lower:
        return "Aptitude Practice:\n" + context

    elif "resume" in query_lower:
        return (
            "Resume Tips:\n"
            "- Add technical projects\n"
            "- Highlight internships\n"
            "- Use action verbs\n"
        )

    elif "role" in query_lower or "job" in query_lower:
        return "Job Roles Info:\n" + context

    else:
        return "Helpful Information:\n" + context


# ⭐ Unique Feature Function
def skill_gap_analysis(query):
    roles = {
        "data scientist": ["python", "machine learning", "statistics", "sql", "data visualization", "deep learning"],
        "software developer": ["java", "dsa", "oop", "databases", "system design"],
        "ai engineer": ["python", "deep learning", "nlp", "tensorflow", "pytorch", "mlops"],
    }

    query_lower = query.lower()
    user_skills = []

    for skill in ["python", "sql", "java", "machine learning", "statistics"]:
        if skill in query_lower:
            user_skills.append(skill)

    selected_role = None
    for role in roles:
        if role in query_lower:
            selected_role = role
            break

    if not selected_role:
        return "Please mention the role you want to become."

    required_skills = roles[selected_role]
    missing_skills = [s for s in required_skills if s not in user_skills]

    roadmap = "\n".join([f"Step {i+1}: Learn {skill}" for i, skill in enumerate(missing_skills)])

    return f"""
Target Role: {selected_role.title()}

Your Skills: {', '.join(user_skills) if user_skills else 'None detected'}

Missing Skills: {', '.join(missing_skills)}

🗺️ Roadmap:
{roadmap}

Suggested Projects:
• Build portfolio projects
• Upload to GitHub
• Participate in coding contests
"""