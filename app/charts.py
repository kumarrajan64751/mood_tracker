# # # # app/charts.py

# # # import pandas as pd
# # # import streamlit as st
# # # import matplotlib.pyplot as plt
# # # from datetime import datetime, timedelta

# # # def show_weekly_charts(df: pd.DataFrame):
# # #     if df.empty:
# # #         st.info("No data yet to display weekly charts.")
# # #         return

# # #     df["timestamp"] = pd.to_datetime(df["timestamp"])
# # #     last_7_days = datetime.now() - timedelta(days=7)
# # #     df_week = df[df["timestamp"] >= last_7_days]

# # #     if df_week.empty:
# # #         st.info("No entries in the last 7 days.")
# # #         return

# # #     # Plot 1: Mood Score Over Time
# # #     fig1, ax1 = plt.subplots()
# # #     ax1.plot(df_week["timestamp"], df_week["mood_score"], marker="o", color="blue")
# # #     ax1.set_title("Mood Score (Last 7 Days)")
# # #     ax1.set_ylabel("Mood (1–10)")
# # #     ax1.set_xlabel("Date")
# # #     ax1.grid(True)
# # #     st.pyplot(fig1)

# # #     # Plot 2: Sleep Duration & Quality
# # #     fig2, ax2 = plt.subplots()
# # #     ax2.bar(df_week["timestamp"], df_week["sleep_hours"], color="purple")
# # #     ax2.set_title("Sleep Hours (Last 7 Days)")
# # #     ax2.set_ylabel("Hours Slept")
# # #     ax2.set_xlabel("Date")
# # #     st.pyplot(fig2)

# # #     # Plot 3: Stress Level Counts
# # #     fig3, ax3 = plt.subplots()
# # #     stress_counts = df_week["stress_level"].value_counts().reindex(["Low", "Medium", "High"], fill_value=0)
# # #     ax3.bar(stress_counts.index, stress_counts.values, color=["green", "orange", "red"])
# # #     ax3.set_title("Stress Levels Distribution")
# # #     ax3.set_ylabel("Count")
# # #     st.pyplot(fig3)
# # import matplotlib.pyplot as plt
# # import seaborn as sns
# # import streamlit as st
# # import pandas as pd

# # def show_weekly_charts(df):
# #     # Ensure timestamp is datetime
# #     df["timestamp"] = pd.to_datetime(df["timestamp"])
# #     df = df.sort_values("timestamp", ascending=False).head(7)
# #     df = df[::-1]  # Reverse to show from oldest to newest

# #     metrics = [
# #         "mood_score", "energy_level", "sleep_hours", "productive_hours",
# #         "social_interaction_score", "screen_time_hours"
# #     ]
# #     titles = {
# #         "mood_score": "Mood Score",
# #         "energy_level": "Energy Level",
# #         "sleep_hours": "Sleep Hours",
# #         "productive_hours": "Productive Hours",
# #         "social_interaction_score": "Social Interaction",
# #         "screen_time_hours": "Screen Time (hrs)"
# #     }

# #     st.markdown("### 📈 Wellness Trends (Last 7 Days)")
# #     for metric in metrics:
# #         fig, ax = plt.subplots(figsize=(6, 2.8))  # Smaller chart size
# #         sns.barplot(data=df, x="timestamp", y=metric, ax=ax, palette="viridis")
# #         ax.set_title(titles[metric])
# #         ax.set_xlabel("Date")
# #         ax.set_ylabel("")
# #         ax.tick_params(axis='x', rotation=45)
# #         st.pyplot(fig)
# import matplotlib.pyplot as plt
# import seaborn as sns
# import streamlit as st
# import pandas as pd

# def show_weekly_charts(df):
#     # Ensure timestamp is datetime
#     df["timestamp"] = pd.to_datetime(df["timestamp"])
#     df = df.sort_values("timestamp", ascending=False).head(7)
#     df = df[::-1]  # Reverse to show from oldest to newest

#     # Format timestamp as two-line label: Date\nHH:MM
#     df["time_label"] = df["timestamp"].dt.strftime('%d-%b\n%H:%M')

#     metrics = [
#         "mood_score", "energy_level", "sleep_hours", "productive_hours",
#         "social_interaction_score", "screen_time_hours"
#     ]
#     titles = {
#         "mood_score": "Mood Score",
#         "energy_level": "Energy Level",
#         "sleep_hours": "Sleep Hours",
#         "productive_hours": "Productive Hours",
#         "social_interaction_score": "Social Interaction",
#         "screen_time_hours": "Screen Time (hrs)"
#     }

#     with st.expander("📊 See Weekly Charts"):
#         st.markdown("### 🧭 Wellness Trends (Last 7 Entries)")
#         for metric in metrics:
#             fig, ax = plt.subplots(figsize=(6, 2.8))
#             sns.barplot(data=df, x="time_label", y=metric, ax=ax, palette="viridis")
#             ax.set_title(titles[metric])
#             ax.set_xlabel("Date")
#             ax.set_ylabel("")
#             ax.tick_params(axis='x', labelrotation=0)
#             st.pyplot(fig)
