# app/insights.py

def generate_daily_insight(entry: dict) -> str:
    insights = []

    # Mood
    if entry["mood_score"] >= 8:
        insights.append("😊 You're feeling great today! Keep it up.")
    elif entry["mood_score"] >= 5:
        insights.append("🙂 Your mood is average — maybe a short walk or talking to a friend could help.")
    else:
        insights.append("😔 You're feeling low. Take some time to rest and do something that makes you happy.")

    # Stress
    if entry["stress_level"] == "High":
        insights.append("⚠️ High stress detected. Consider practicing deep breathing or journaling.")
    elif entry["stress_level"] == "Medium":
        insights.append("😐 Some stress today — try a relaxing break or light exercise.")
    else:
        insights.append("🧘‍♂️ Low stress — nice work managing your day!")

    # Sleep
    if entry["sleep_hours"] < 5 or entry["sleep_quality"] == "Poor":
        insights.append("💤 You may need better sleep. Avoid screens before bed and try to sleep earlier.")
    elif entry["sleep_hours"] >= 7 and entry["sleep_quality"] == "Good":
        insights.append("✅ Great sleep habits — well rested!")

    # Productivity
    if entry["productive_hours"] >= 6:
        insights.append("💼 Productive day! Make sure to balance it with rest.")
    elif entry["productive_hours"] < 3:
        insights.append("🕓 You had a light day — maybe plan a focused session tomorrow.")

    # Activity
    if entry["physical_activity_duration"] >= 30:
        insights.append("🏃‍♂️ Great job staying active!")
    else:
        insights.append("📌 Try to include at least 30 minutes of physical activity for better health.")

    # Social
    if entry["social_interaction_score"] < 4:
        insights.append("👥 Low social interaction — consider reaching out to someone close.")
    elif entry["social_interaction_score"] >= 8:
        insights.append("🥳 You stayed well-connected — awesome!")

    # Screen time
    screen = entry["screen_time_hours"]
    if screen <= 1:
        insights.append("📵 Excellent screen discipline!")
    elif screen <= 3:
        insights.append("📱 Screen time is okay, but try taking breaks.")
    else:
        insights.append("⚠️ High screen usage — try reducing non-work screen time.")

    # Junk food
    if entry["junk_food_intake"] == "Yes":
        insights.append("🍔 Try to limit junk food tomorrow for better mood and energy.")

    # Outdoors
    if entry["outside_time_minutes"] >= 30:
        insights.append("🌤️ Fresh air is great — keep spending time outdoors.")
    elif entry["outside_time_minutes"] < 10:
        insights.append("🌱 Try to step outside tomorrow, even briefly.")

    return "  \n".join(insights)
