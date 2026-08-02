def get_recommendation(score):
    if score >= 90:
        return "Excellent Match - Highly Recommended"
    elif score >= 80:
        return "Strong Candidate - Recommended"
    elif score >= 70:
        return "Good Candidate - Consider for Interview"
    elif score >= 60:
        return "Average Match - Needs Skill Improvement"
    elif score >= 40:
        return "Below Average - Significant Skill Gap"
    else:
        return "Not Recommended"