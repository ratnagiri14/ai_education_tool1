import streamlit as st
from openai import OpenAI
import pandas as pd
import os
import io
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

# ---------- Setup ----------
st.set_page_config(page_title="AI Autism Support Toolkit", page_icon="🧠", layout="wide")

api_key = st.secrets.get("OPENAI_API_KEY")
if not api_key:
    st.error("OpenAI API key not found. Create `.streamlit/secrets.toml` and add `OPENAI_API_KEY = \"your_openai_api_key_here\"`.")
    st.stop()

client = OpenAI(api_key=api_key)

# ---------- PDF Function ----------
def create_pdf(text):
    buffer = io.BytesIO()
    doc = SimpleDocTemplate(buffer)
    styles = getSampleStyleSheet()
    content = []

    for line in text.split("\n"):
        content.append(Paragraph(line, styles["Normal"]))
        content.append(Spacer(1, 8))

    doc.build(content)
    buffer.seek(0)
    return buffer

# ---------- Simple Login ----------
st.sidebar.title("🧠 AI Autism Support Toolkit")

username = st.sidebar.text_input("Username")
password = st.sidebar.text_input("Password", type="password")

if username == "ratna" and password == "1234":
    st.sidebar.success("Login successful")
else:
    st.sidebar.warning("Please login")
    st.stop()

# ---------- Menu ----------
tool = st.sidebar.selectbox(
    "Menu",
    [
        "Home",
        "Reading Comprehension",
        "Inference Practice",
        "WH Questions",
        "Cause and Effect",
        "Vocabulary Builder",
        "Social Story Generator",
        "Visual Schedule Generator",
        "Behavior Support Plan",
        "IEP Goal Generator",
        "Parent Progress Tracker"
    ]
)

# ---------- AI Helper ----------
def ask_ai(prompt):
    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content

# ---------- Download Buttons ----------
def show_downloads(text, filename):
    st.download_button("📄 Download TXT", text, file_name=f"{filename}.txt")

    pdf = create_pdf(text)
    st.download_button(
        "📥 Download PDF",
        data=pdf,
        file_name=f"{filename}.pdf",
        mime="application/pdf"
    )

# ---------- Home ----------
if tool == "Home":
    st.title("Welcome! 👋")
    st.info("This AI toolkit helps parents, teachers, and homeschool families create autism-friendly learning materials.")

    st.subheader("Tools Included")
    st.write("""
    ✅ Reading comprehension  
    ✅ Inference practice  
    ✅ WH questions  
    ✅ Cause and effect  
    ✅ Vocabulary practice  
    ✅ Social stories  
    ✅ Visual schedules  
    ✅ Behavior support plans  
    ✅ IEP goals  
    ✅ Parent progress tracker  
    """)

# ---------- Reading Comprehension ----------
elif tool == "Reading Comprehension":
    st.title("📚 Reading Comprehension")

    topic = st.text_input("Topic", "The Life Cycle of a Butterfly")
    grade = st.selectbox("Grade Level", ["1st Grade", "2nd Grade", "3rd Grade", "4th Grade", "5th Grade", "6th Grade"])
    level = st.selectbox("Reading Level", ["Easy", "Medium", "Hard"])
    questions = st.slider("Number of Questions", 3, 10, 5)

    if st.button("Generate Passage"):
        prompt = f"""
        Create an autism-friendly reading comprehension worksheet.

        Topic: {topic}
        Grade: {grade}
        Level: {level}
        Number of questions: {questions}

        Include:
        1. Short passage
        2. WH questions
        3. Multiple choice questions
        4. Inference questions
        5. Vocabulary words
        6. Answer key
        """

        result = ask_ai(prompt)
        st.write(result)
        show_downloads(result, "reading_comprehension")

# ---------- Inference Practice ----------
elif tool == "Inference Practice":
    st.title("💡 Inference Practice")
    st.write("Read the situation and answer what you can understand from clues.")

    grade = st.selectbox("Grade Level", ["1st Grade", "2nd Grade", "3rd Grade", "4th Grade", "5th Grade"])
    difficulty = st.selectbox("Difficulty Level", ["Easy", "Medium", "Hard"])
    number = st.slider("Number of Questions", 3, 10, 5)
    theme = st.selectbox("Theme", ["Everyday Life", "School", "Home", "Friendship", "Weather", "Animals"])

    if st.button("Generate Inference Practice"):
        prompt = f"""
        Create autism-friendly inference practice.

        Grade: {grade}
        Difficulty: {difficulty}
        Theme: {theme}
        Number of questions: {number}

        Include:
        1. Short situation
        2. Inference questions
        3. 3 answer choices for each question
        4. Correct answer
        5. Simple explanation

        Use simple clear language.
        """

        result = ask_ai(prompt)
        st.write(result)
        show_downloads(result, "inference_practice")

# ---------- WH Questions ----------
elif tool == "WH Questions":
    st.title("❓ WH Questions Generator")

    story = st.text_area("Paste short story")

    if st.button("Create WH Questions"):
        prompt = f"""
        Create autism-friendly WH questions from this story:

        {story}

        Include:
        5 Who questions
        5 What questions
        5 Where questions
        5 When questions
        5 Why questions
        Answer key
        """

        result = ask_ai(prompt)
        st.write(result)
        show_downloads(result, "wh_questions")

# ---------- Cause and Effect ----------
elif tool == "Cause and Effect":
    st.title("🔄 Cause and Effect")

    topic = st.text_input("Topic", "Daily life")
    level = st.selectbox("Level", ["Easy", "Medium", "Hard"])

    if st.button("Create Cause and Effect Practice"):
        prompt = f"""
        Create autism-friendly cause and effect practice.

        Topic: {topic}
        Level: {level}

        Include:
        10 cause and effect examples
        10 fill in the blank questions
        Picture ideas
        Answer key
        """

        result = ask_ai(prompt)
        st.write(result)
        show_downloads(result, "cause_effect")

# ---------- Vocabulary ----------
elif tool == "Vocabulary Builder":
    st.title("📝 Vocabulary Builder")

    words = st.text_area("Enter words", "happy\nsad\nlarge\nsmall")
    level = st.selectbox("Level", ["Easy", "Medium", "Hard"])

    if st.button("Create Vocabulary Practice"):
        prompt = f"""
        Create autism-friendly vocabulary practice.

        Words:
        {words}

        Level: {level}

        Include:
        Meaning
        Simple sentence
        Synonym
        Antonym
        Fill in the blank
        Answer key
        """

        result = ask_ai(prompt)
        st.write(result)
        show_downloads(result, "vocabulary_practice")

# ---------- Social Story ----------
elif tool == "Social Story Generator":
    st.title("📖 Social Story Generator")

    child_name = st.text_input("Child Name", "Arjun")
    situation = st.text_input("Situation", "Going to the doctor")
    level = st.selectbox("Reading Level", ["Very Simple", "Simple", "Medium"])

    if st.button("Create Social Story"):
        prompt = f"""
        Create a positive autism-friendly social story.

        Child name: {child_name}
        Situation: {situation}
        Reading level: {level}

        Use:
        Short sentences
        First person language
        Calm words
        8 to 10 steps
        Happy ending
        """

        result = ask_ai(prompt)
        st.write(result)
        show_downloads(result, "social_story")

# ---------- Visual Schedule ----------
elif tool == "Visual Schedule Generator":
    st.title("📅 Visual Schedule Generator")

    routine = st.selectbox("Routine", ["Morning Routine", "Bathing Routine", "Homework Routine", "Bedtime Routine"])
    steps = st.text_area("Steps", "Wake up\nBrush teeth\nGet dressed\nEat breakfast")

    if st.button("Create Visual Schedule"):
        prompt = f"""
        Create an autism-friendly visual schedule.

        Routine: {routine}
        Steps:
        {steps}

        For each step include:
        1. Short instruction
        2. Simple picture idea
        3. Parent prompt
        """

        result = ask_ai(prompt)
        st.write(result)
        show_downloads(result, "visual_schedule")

# ---------- Behavior Support ----------
elif tool == "Behavior Support Plan":
    st.title("🛡️ Behavior Support Plan")

    behavior = st.text_input("Behavior", "Biting shirt")
    setting = st.text_input("Where/When", "During homework")
    trigger = st.text_area("Possible Trigger", "Hard work, waiting, noise, tired")

    if st.button("Create Support Plan"):
        prompt = f"""
        Create a parent-friendly autism behavior support plan.

        Behavior: {behavior}
        Setting: {setting}
        Possible trigger: {trigger}

        Include:
        What behavior may mean
        Prevention ideas
        Replacement skill
        Calm-down strategy
        Visual support idea

        Do not diagnose.
        """

        result = ask_ai(prompt)
        st.write(result)
        show_downloads(result, "behavior_support_plan")

# ---------- IEP Goals ----------
elif tool == "IEP Goal Generator":
    st.title("🎯 IEP Goal Generator")

    age = st.text_input("Student Age")
    grade = st.text_input("Grade")
    skill = st.selectbox("Skill Area", ["Reading", "Speech", "Social Skills", "Writing", "Math", "Life Skills", "Behavior"])
    current_level = st.text_area("Current Level")

    if st.button("Generate IEP Goals"):
        prompt = f"""
        Create 3 SMART IEP goals.

        Age: {age}
        Grade: {grade}
        Skill area: {skill}
        Current level: {current_level}

        Include:
        Goal statement
        Short-term objectives
        Progress measurement
        Parent-friendly language
        """

        result = ask_ai(prompt)
        st.write(result)
        show_downloads(result, "iep_goals")

# ---------- Progress Tracker ----------
elif tool == "Parent Progress Tracker":
    st.title("📈 Parent Progress Tracker")

    child = st.text_input("Child Name", "Arjun")
    skill = st.text_input("Skill Practiced", "Reading comprehension")
    date = st.date_input("Date")
    score = st.slider("Score", 1, 5, 3)
    notes = st.text_area("Notes")

    file_name = "progress_notes.csv"

    if st.button("Save Progress Note"):
        new_data = pd.DataFrame([{ 
            "Child": child,
            "Date": date,
            "Skill": skill,
            "Score": score,
            "Notes": notes
        }])

        if os.path.exists(file_name):
            old_data = pd.read_csv(file_name)
            all_data = pd.concat([old_data, new_data], ignore_index=True)
        else:
            all_data = new_data

        all_data.to_csv(file_name, index=False)
        st.success("Progress note saved!")

    if os.path.exists(file_name):
        data = pd.read_csv(file_name)
        st.subheader("Saved Progress Notes")
        st.dataframe(data)

        st.download_button(
            "Download CSV",
            data.to_csv(index=False),
            file_name="progress_notes.csv",
            mime="text/csv"
        )

        st.subheader("Progress Chart")
        data["Date"] = pd.to_datetime(data["Date"])

        skill_choice = st.selectbox("Choose Skill", data["Skill"].unique())
        filtered = data[data["Skill"] == skill_choice].sort_values("Date")

        st.line_chart(filtered, x="Date", y="Score")

        if st.button("Create Monthly AI Summary"):
            prompt = f"""
            Create a parent-friendly monthly progress summary.

            Progress data:
            {data.to_string()}

            Include:
            Strengths
            Improving skills
            Challenges
            Next month goals
            Home practice ideas
            """

            summary = ask_ai(prompt)
            st.write(summary)
            show_downloads(summary, "monthly_progress_summary")
