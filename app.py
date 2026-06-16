import streamlit as st

st.set_page_config(page_title="AI Autism Support Toolkit", page_icon="🧩", layout="wide")

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

with st.sidebar:
    st.markdown("# AI Autism Support Toolkit")
    st.write("---")

    st.subheader("Login")
    username = st.text_input("Username", value="ratna")
    password = st.text_input("Password", type="password")
    login_button = st.button("Login")

    if login_button:
        if username and password:
            st.session_state.logged_in = True
            st.success("Login successful")
        else:
            st.error("Please enter both username and password.")

    if st.session_state.logged_in:
        st.write("---")
        page = st.radio(
            "Menu",
            [
                "Home",
                "Reading Comprehension",
                "Inference Practice",
                "WH Questions",
                "Cause & Effect",
                "Vocabulary Builder",
                "Social Story Generator",
                "Visual Schedule Generator",
                "Behavior Support Tool",
                "IEP Goal Generator",
                "Parent Progress Tracker",
            ],
            index=0,
        )
    else:
        page = "Home"

    st.write("---")
    st.markdown("#### Remember")
    st.write("Small steps every day lead to big progress.")

if page == "Home":
    st.markdown("# Welcome to AI Autism Support Toolkit 👋")
    st.write("Create personalized learning materials and track progress with the power of AI.")

    col1, col2, col3 = st.columns(3)
    col1.info("**Create Learning Materials**\nGenerate reading worksheets, questions, stories, and more in seconds.")
    col2.success("**Track Progress**\nTrack scores, notes, and visualize progress over time.")
    col3.warning("**Support**\nSupport learning, communication, behavior, and daily routines.")

    st.markdown("### Popular Tools")
    tool_rows = [
        ["Reading Comprehension", "Inference Practice", "WH Questions", "Cause & Effect"],
        ["Vocabulary Builder", "Social Story Generator", "Visual Schedule Generator", "Behavior Support Tool"],
        ["IEP Goal Generator", "Parent Progress Tracker", "", ""],
    ]

    for row in tool_rows:
        cols = st.columns(4)
        for col, tool_name in zip(cols, row):
            if tool_name:
                col.markdown(f"### {tool_name}")
                if tool_name == "Reading Comprehension":
                    col.write("Create passages with questions and answers.")
                elif tool_name == "Inference Practice":
                    col.write("Build inference skills with fun prompts.")
                elif tool_name == "WH Questions":
                    col.write("Generate who, what, where, when, why, how questions.")
                elif tool_name == "Cause & Effect":
                    col.write("Create cause and effect activities.")
                elif tool_name == "Vocabulary Builder":
                    col.write("Build vocabulary with meanings and sentences.")
                elif tool_name == "Social Story Generator":
                    col.write("Create personalized social stories.")
                elif tool_name == "Visual Schedule Generator":
                    col.write("Generate visual schedules for daily routines.")
                elif tool_name == "Behavior Support Tool":
                    col.write("Get behavior strategies and support plans.")
                elif tool_name == "IEP Goal Generator":
                    col.write("Generate measurable IEP goals.")
                elif tool_name == "Parent Progress Tracker":
                    col.write("Track progress, view charts, and get AI summaries.")

else:
    st.markdown(f"# {page}")
    st.write("This tool page is coming soon. Use the Home tab to explore the toolkit.")
