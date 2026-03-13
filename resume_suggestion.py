def generate_suggestions(missing_skills):

    suggestions = []

    for skill in missing_skills[:5]:

        suggestions.append(
        f"Consider adding {skill} to improve your resume."
        )

    return suggestions