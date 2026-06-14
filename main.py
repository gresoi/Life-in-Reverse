def show_welcome():
    print("=================================")
    print("        LIFE IN REVERSE")
    print("=================================")
    print("Most programs tell you how to succeed.")
    print("This one shows you what's standing in your way.")
    print()


def choose_category():
    print("Choose a goal category:")
    print("1. Education")
    print("2. Career")
    print("3. Health & Fitness")
    print("4. Skill Learning")
    print("5. Personal Project")
    print()
    category = input("Enter the number of your choice: ")
    return category


def education_questions():
    print("\n--- Education Assessment ---")
    study_hours = float(input("How many hours do you study per week? "))
    schedule = input("How often do you stick to your schedule? (Never/Sometimes/Often/Always): ").capitalize()
    practice = input("How often do you practise what you learn? (Never/Sometimes/Often/Always): ").capitalize()
    distractions = int(input("How many major distractions do you have while studying? (0-10): "))
    procrastination = int(input("How often do you leave work until the last minute? (0-10): "))

    return {
        "study_hours": study_hours,
        "schedule": schedule,
        "practice": practice,
        "distractions": distractions,
        "procrastination": procrastination
    }


def career_questions():
    print("\n--- Career Assessment ---")
    skill_hours = float(input("How many hours per week do you spend building career-related skills? "))
    projects = input("How often do you work on projects related to your desired career? (Never/Sometimes/Often/Always): ").capitalize()
    networking = input("How often do you network with people in your field? (Never/Sometimes/Often/Always): ").capitalize()
    distractions = int(input("How many distractions prevent you from working on your career goals? (0-10): "))
    procrastination = int(input("How often do you delay career-related work? (0-10): "))

    return {
        "skill_hours": skill_hours,
        "projects": projects,
        "networking": networking,
        "distractions": distractions,
        "procrastination": procrastination
    }


def health_questions():
    print("\n--- Health & Fitness Assessment ---")
    exercise_days = int(input("How many days per week do you exercise? (0-7): "))
    eating = input("How often do you follow a healthy eating routine? (Never/Sometimes/Often/Always): ").capitalize()
    sleep = input("How often do you get enough sleep? (Never/Sometimes/Often/Always): ").capitalize()
    unhealthy_habits = int(input("How many unhealthy habits affect your fitness? (0-10): "))
    skip_workouts = int(input("How often do you skip planned workouts? (0-10): "))

    return {
        "exercise_days": exercise_days,
        "eating": eating,
        "sleep": sleep,
        "unhealthy_habits": unhealthy_habits,
        "skip_workouts": skip_workouts
    }


def skill_questions():
    print("\n--- Skill Learning Assessment ---")
    practice_hours = float(input("How many hours per week do you practise your skill? "))
    learning_plan = input("How often do you follow a learning plan? (Never/Sometimes/Often/Always): ").capitalize()
    review = input("How often do you review what you learned? (Never/Sometimes/Often/Always): ").capitalize()
    distractions = int(input("How many distractions interrupt your learning? (0-10): "))
    give_up = int(input("How often do you quit when learning gets difficult? (0-10): "))

    return {
        "practice_hours": practice_hours,
        "learning_plan": learning_plan,
        "review": review,
        "distractions": distractions,
        "give_up": give_up
    }


def project_questions():
    print("\n--- Personal Project Assessment ---")
    work_hours = float(input("How many hours per week do you work on your project? "))
    progress = input("How often do you make progress on the project? (Never/Sometimes/Often/Always): ").capitalize()
    completion = input("How often do you finish tasks you start? (Never/Sometimes/Often/Always): ").capitalize()
    distractions = int(input("How many distractions pull you away from the project? (0-10): "))
    new_ideas = int(input("How often do you abandon work for new ideas? (0-10): "))

    return {
        "work_hours": work_hours,
        "progress": progress,
        "completion": completion,
        "distractions": distractions,
        "new_ideas": new_ideas
    }


def cal_risk(answers, category):
    risk_score = 0
    risk_reasons = []

    hours_key = {"Education": "study_hours", "Career": "skill_hours",
                 "Skill Learning": "practice_hours", "Personal Project": "work_hours"}

    if category in hours_key:
        hours = answers[hours_key[category]]
        if hours < 3:
            risk_score += 25
            risk_reasons.append("Very low weekly hours")
        elif hours < 7:
            risk_score += 15
            risk_reasons.append("Low weekly hours")

    if "exercise_days" in answers:
        if answers["exercise_days"] <= 1:
            risk_score += 25
            risk_reasons.append("Rarely exercising")
        elif answers["exercise_days"] <= 3:
            risk_score += 12
            risk_reasons.append("Low exercise frequency")

    freq_checks = [
        ("schedule",      "Never follows a schedule",         "Inconsistent schedule"),
        ("practice",      "Never practises what is learned",  "Limited practice"),
        ("projects",      "Never works on career projects",   "Rarely works on projects"),
        ("networking",    "Never networks",                   "Minimal networking"),
        ("eating",        "Never eats healthily",             "Poor eating habits"),
        ("sleep",         "Never gets enough sleep",          "Insufficient sleep"),
        ("learning_plan", "No learning plan",                 "Inconsistent learning plan"),
        ("review",        "Never reviews material",           "Rarely reviews material"),
        ("progress",      "Never makes project progress",     "Infrequent progress"),
        ("completion",    "Never finishes tasks",             "Low task completion"),
    ]

    for key, never_label, sometimes_label in freq_checks:
        if key in answers:
            val = answers[key]
            if val == "Never":
                risk_score += 20
                risk_reasons.append(never_label)
            elif val == "Sometimes":
                risk_score += 10
                risk_reasons.append(sometimes_label)
            elif val == "Often":
                risk_score += 5

    distraction_keys = ["distractions", "unhealthy_habits"]
    for key in distraction_keys:
        if key in answers:
            val = answers[key]
            if val >= 7:
                risk_score += 20
                risk_reasons.append("Very high distractions")
            elif val >= 4:
                risk_score += 10
                risk_reasons.append("Moderate distractions")

    avoidance_keys = {
        "procrastination": "Frequent procrastination",
        "skip_workouts":   "Frequently skips workouts",
        "give_up":         "Tends to quit when things get hard",
        "new_ideas":       "Chases new ideas instead of finishing"
    }

    for key, label in avoidance_keys.items():
        if key in answers:
            val = answers[key]
            if val >= 7:
                risk_score += 20
                risk_reasons.append(label)
            elif val >= 4:
                risk_score += 10
                risk_reasons.append(label)

    seen = []
    unique_reasons = []
    for r in risk_reasons:
        if r not in seen:
            seen.append(r)
            unique_reasons.append(r)

    return min(risk_score, 100), unique_reasons


def get_risk_level(risk_score):
    if risk_score <= 25:
        return "LOW"
    elif risk_score <= 50:
        return "MODERATE"
    elif risk_score <= 75:
        return "HIGH"
    else:
        return "CRITICAL"


def print_report(category, risk_score, risk_level, risk_reasons):
    print("\n=================================")
    print("       FAILURE RISK REPORT")
    print("=================================")
    print("Goal Category:", category)
    print("Risk Score:", risk_score)
    print("Risk Level:", risk_level)

    print("\nMain Risk Factors:")
    if len(risk_reasons) == 0:
        print("- No major risk factors detected")
    else:
        for reason in risk_reasons:
            print("-", reason)

    print("\nReverse Analysis:")
    if risk_level == "LOW":
        print("Your habits are mostly working for your goal. The main risk is complacency — small slips compound over time.")
    elif risk_level == "MODERATE":
        print("You have real strengths here, but clear gaps too. Left unchanged, these will slow your progress significantly.")
    elif risk_level == "HIGH":
        print("Your current habits are working against your goal more than for it. Without changing these patterns, the goal stays a dream.")
    else:
        print("Your habits right now are almost perfectly designed to prevent your goal. The good news: you're aware of it now.")

    print("=================================")


FIXES = {
    "Very low weekly hours":            "Block at least 1 hour daily in your calendar. Treat it like a class you cannot skip.",
    "Low weekly hours":                 "Add one extra session per week until you hit 7+ hours. Small increases stick better.",
    "Rarely exercising":                "Start with 3 days a week. Pick the same time each day so it becomes automatic.",
    "Low exercise frequency":           "Add one more workout day this week. Consistency beats intensity at this stage.",
    "Never follows a schedule":         "Write tomorrow's plan tonight. Even a rough one beats none.",
    "Inconsistent schedule":            "Pick two non-negotiable time slots per week and protect them.",
    "Never practises what is learned":  "End every study session with one small practice task, even 10 minutes.",
    "Limited practice":                 "Add a practice block right after your learning session while it is fresh.",
    "Never works on career projects":   "Start one small project this week. It does not have to be perfect.",
    "Rarely works on projects":         "Dedicate one weekend hour to a career project. One hour compounds fast.",
    "Never networks":                   "Message one person in your field this week. Just one.",
    "Minimal networking":               "Comment on or reach out to someone in your field once a week.",
    "Never eats healthily":             "Fix one meal a day first. Do not overhaul everything at once.",
    "Poor eating habits":               "Prep one healthy meal in advance each week to reduce bad choices.",
    "Never gets enough sleep":          "Set a fixed bedtime and stick to it even on weekends.",
    "Insufficient sleep":               "Move your bedtime 30 minutes earlier this week.",
    "No learning plan":                 "Write down three things you want to learn this month. That is your plan.",
    "Inconsistent learning plan":       "Review your learning plan every Sunday and adjust for the week ahead.",
    "Never reviews material":           "Spend the last 5 minutes of every session reviewing what you just did.",
    "Rarely reviews material":          "Add a 15-minute weekly review slot to go over what you learned.",
    "Never makes project progress":     "Commit to one tiny task per day. Done is better than perfect.",
    "Infrequent progress":              "Break your project into smaller tasks. Finishing small things builds momentum.",
    "Never finishes tasks":             "Before starting anything new, finish the last thing on your list.",
    "Low task completion":              "Limit yourself to three tasks per day so your list stays finishable.",
    "Very high distractions":           "Identify your top two distractions and remove them physically before starting work.",
    "Moderate distractions":            "Use a 25-minute focus block with your phone face-down in another room.",
    "Frequent procrastination":         "Start with two minutes. Seriously — just open the thing and begin.",
    "Frequently skips workouts":        "Lay out your workout clothes the night before. Lower the barrier to start.",
    "Tends to quit when things get hard": "When you want to quit, do five more minutes. That habit rewires everything.",
    "Chases new ideas instead of finishing": "Write new ideas in a list to revisit later. Then return to what you were doing."
}

WEEK_PLANS = {
    "LOW": [
        "Week 1: Audit what is working and lock in those habits.",
        "Week 2: Identify the one area that could slip and build a safeguard.",
        "Week 3: Increase your weekly hours or intensity by 10%.",
        "Week 4: Review your progress and set a goal for next month."
    ],
    "MODERATE": [
        "Week 1: Fix your single biggest risk factor from the list above.",
        "Week 2: Build a simple weekly schedule and follow it for 7 days.",
        "Week 3: Add one accountability measure — a person, an app, anything.",
        "Week 4: Compare week 4 to week 1 and note what actually changed."
    ],
    "HIGH": [
        "Week 1: Cut your top distraction completely. Just for one week.",
        "Week 2: Add structure — same time, same place, every session.",
        "Week 3: Focus only on consistency. Hours do not matter yet, showing up does.",
        "Week 4: Reflect honestly. If nothing changed, the problem is commitment not strategy."
    ],
    "CRITICAL": [
        "Week 1: Pick one habit only. Not five. One. Work on it every single day.",
        "Week 2: Add a second habit only after week 1 felt easy.",
        "Week 3: Remove something from your life that is actively blocking you.",
        "Week 4: Measure where you started vs now. Progress will be small but real."
    ]
}


def print_roadmap(risk_level, risk_reasons):
    print("\n=================================")
    print("         YOUR 30-DAY ROADMAP")
    print("=================================")

    print("\nHabit Fixes:")
    fixes_shown = []
    for reason in risk_reasons:
        if reason in FIXES and reason not in fixes_shown:
            print(f"\n  {reason}:")
            print(f"  -> {FIXES[reason]}")
            fixes_shown.append(reason)

    print("\nWeek by Week:")
    for week in WEEK_PLANS[risk_level]:
        print(" ", week)

    print("\n=================================\n")


def main():
    show_welcome()

    category = choose_category()

    categories = {
        "1": "Education",
        "2": "Career",
        "3": "Health & Fitness",
        "4": "Skill Learning",
        "5": "Personal Project"
    }

    if category not in categories:
        print("Invalid choice. Please restart and enter a number from 1 to 5.")
        return

    category_name = categories[category]

    if category == "1":
        answers = education_questions()
    elif category == "2":
        answers = career_questions()
    elif category == "3":
        answers = health_questions()
    elif category == "4":
        answers = skill_questions()
    else:
        answers = project_questions()

    risk_score, risk_reasons = cal_risk(answers, category_name)
    risk_level = get_risk_level(risk_score)

    print_report(category_name, risk_score, risk_level, risk_reasons)

    print("\nWould you like a personalised 30-day roadmap based on your results?")
    choice = input("Type yes or no: ").strip().lower()

    if choice == "yes":
        print_roadmap(risk_level, risk_reasons)
    else:
        print("\nYour report above is your starting point. Good luck.\n")


if __name__ == "__main__":
    main()