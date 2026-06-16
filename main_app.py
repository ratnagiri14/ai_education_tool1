import streamlit as st

st.markdown("""
<style>
.main {
    background-color: #f7fbff;
}

h1, h2, h3 {
    color: #2b4c7e;
}

.stButton>button {
    background-color: #4f8df7;
    color: white;
    border-radius: 10px;
    height: 3em;
    width: 100%;
    font-size: 16px;
}

.stDownloadButton>button {
    background-color: #28a745;
    color: white;
    border-radius: 10px;
    height: 3em;
    width: 100%;
}

[data-testid="stSidebar"] {
    background-color: #eaf3ff;
}

.card {
    background-color: white;
    padding: 20px;
    border-radius: 15px;
    box-shadow: 2px 2px 10px #d9e2ec;
    margin-bottom: 20px;
}
</style>
""", unsafe_allow_html=True)

tool = st.sidebar.radio(
    "Menu",
    ["Home", "Reading Comprehension", "Inference Practice", "WH Questions", "Cause and Effect", "Vocabulary Builder", "Social Story Generator", "Visual Schedule Generator", "Behavior Support Tool", "IEP Goal Generator", "Parent Progress Tracker"],
    index=0,
)

if tool == "Home":
    st.title("🧠 AI Autism Support Toolkit")

    st.markdown("""
    <div class="card">
    <h3>Welcome!</h3>
    <p>This app helps parents, teachers, and homeschool families create autism-friendly learning materials.</p>
    </div>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        <div class="card">
        <h3>📚 Reading</h3>
        <p>Create reading comprehension, WH questions, and vocabulary practice.</p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="card">
        <h3>💡 Thinking Skills</h3>
        <p>Create inference, cause and effect, and reasoning practice.</p>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class="card">
        <h3>📈 Progress</h3>
        <p>Track scores, notes, progress charts, and monthly summaries.</p>
        </div>
        """, unsafe_allow_html=True)
