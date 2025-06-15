# app/app.py

import streamlit as st
import pandas as pd
import os
import json
import datetime
from streamlit_lottie import st_lottie

from insights import generate_daily_insight
from session_control import check_last_submission_time, update_last_submission_time
from charts import show_weekly_charts

# ─── File Paths ─────────────────────────────────────────────
BASE_DIR = os.path.dirname(__file__)
DATA_DIR = os.path.join(BASE_DIR, "..", "data")
ASSETS_DIR = os.path.join(BASE_DIR, "assets")
USER_LOG_PATH = os.path.join(DATA_DIR, "user_logs.csv")
# Initialize CSV if it doesn't exist or is empty
if not os.path.exists(USER_LOG_PATH) or os.path.getsize(USER_LOG_PATH) == 0:
    pd.DataFrame(columns=[
        "date", "name", "mood_score", "emotion_label", "stress_level",
        "sleep_hours", "sleep_quality", "energy_level", "productive_hours",
        "social_interaction_score", "steps_walked", "physical_activity_duration",
        "screen_time_hours", "outside_time_minutes", "junk_food_intake", "trigger_event"
    ]).to_csv(USER_LOG_PATH, index=False)

LOTTIE_PATH = os.path.join(ASSETS_DIR, "lottie_mood.json")

# ─── Config ─────────────────────────────────────────────────
st.set_page_config(page_title="Mood Tracker", page_icon="🧠", layout="centered")
st.markdown("""
    <style>
        /* Hide Streamlit header and footer */
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}

        /* Optional: Remove whitespace around the app */
        .block-container {
            padding-top: 1rem;
            padding-bottom: 1rem;
        }
            <div style="font-size: 1.15rem; line-height: 1.6; color: #333;">
        {insight}
    </div>
    </style>
""", unsafe_allow_html=True)
st.markdown("<h1 style='text-align: center;'>🧠 Daily Mood Tracker</h1>", unsafe_allow_html=True)


# ─── Load Animation ─────────────────────────────────────────
def load_lottiefile(path: str):
    with open(path, "r") as f:
        return json.load(f)

st_lottie(load_lottiefile(LOTTIE_PATH), height=200)

# ─── Session Lock ───────────────────────────────────────────
if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)

if not os.path.exists(USER_LOG_PATH):
    df_init = pd.DataFrame(columns=[
        "timestamp", "mood_score", "emotion_label", "stress_level", "sleep_hours",
        "sleep_quality", "energy_level", "productive_hours", "social_interaction_score",
        "steps_walked", "physical_activity_duration", "screen_time_hours",
        "outside_time_minutes", "junk_food_intake", "trigger_event"
    ])
    df_init.to_csv(USER_LOG_PATH, index=False)

# if not check_last_submission_time():
#     st.warning("🕒 You've already submitted in the last 20 hours. Please come back later.")
#     st.stop()

# ─── Daily Form ─────────────────────────────────────────────
st.subheader("📋 Log your day")
with st.form("daily_log"):
    mood_score = st.slider("How do you feel today? (1–10)", 1, 10, 5)
    emotion_label = st.multiselect("Which emotions describe your day?", [
        "Happy", "Sad", "Angry", "Anxious", "Excited", "Calm", "Tired", "Lonely"])
    stress_level = st.selectbox("Stress level:", ["Low", "Medium", "High"])
    sleep_hours = st.slider("Sleep hours last night:", 0, 12, 7)
    sleep_quality = st.selectbox("Sleep quality:", ["Poor", "OK", "Good"])
    energy_level = st.slider("Energy level today:", 1, 10, 5)
    productive_hours = st.slider("How many hours were you productive?", 0, 12, 5)
    social_interaction_score = st.slider("Social connection today (1–10):", 1, 10, 5)
    steps_walked = st.number_input("Estimated steps walked:", 0, 50000, 4000)
    physical_activity_duration = st.slider("Physical activity (minutes):", 0, 180, 30)
    screen_time_hours = st.slider("Screen time today (excluding work):", 0, 10, 3)
    outside_time_minutes = st.slider("Time spent outdoors (minutes):", 0, 180, 30)
    junk_food_intake = st.radio("Did you eat junk food today?", ["Yes", "No"])
    trigger_event = st.text_input("Any significant event or mood trigger today? (Optional)")

    submitted = st.form_submit_button("Submit Entry")

# ─── Save Data + Generate Insight ───────────────────────────
if submitted:
    now = datetime.datetime.now()
    data = {
        "timestamp": now,
        "mood_score": mood_score,
        "emotion_label": ", ".join(emotion_label),
        "stress_level": stress_level,
        "sleep_hours": sleep_hours,
        "sleep_quality": sleep_quality,
        "energy_level": energy_level,
        "productive_hours": productive_hours,
        "social_interaction_score": social_interaction_score,
        "steps_walked": steps_walked,
        "physical_activity_duration": physical_activity_duration,
        "screen_time_hours": screen_time_hours,
        "outside_time_minutes": outside_time_minutes,
        "junk_food_intake": junk_food_intake,
        "trigger_event": trigger_event,
    }
    df = pd.read_csv(USER_LOG_PATH)
    df = pd.concat([df, pd.DataFrame([data])], ignore_index=True)
    df.to_csv(USER_LOG_PATH, index=False)
    update_last_submission_time()

    st.success("✅ Entry submitted successfully!")
    st.divider()
    st.subheader("🔍 Your Daily Insight")
    insight = generate_daily_insight(data)
    st.markdown(insight)

    st.divider()
    st.subheader("📊 Weekly Overview")
    show_weekly_charts(df)

  
st.markdown("<div style='height: 80px;'></div>", unsafe_allow_html=True)
st.markdown("""
    <hr style="margin-top: 30px; margin-bottom: 10px;">
    <p style='text-align: center; color: gray; font-size: 20px;'>
        Made with ❤️ to support your mental well-being
    </p>
""", unsafe_allow_html=True)

