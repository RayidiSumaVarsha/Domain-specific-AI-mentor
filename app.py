import streamlit as st
import os
from dotenv import load_dotenv

# LangChain Imports for Google Gemini
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate

# Load Environment Variables
load_dotenv()

# --- CONFIGURATION ---
st.set_page_config(
    page_title="AI Mentor",
    page_icon="🎓",
    layout="centered"
)

# ==========================================================
# 🎨 CARTOON + PASTEL CSS WITH STRONG ANIMATIONS
# ==========================================================
st.markdown("""
<style>

/* ---------------- ANIMATIONS ---------------- */

@keyframes bounceIn {
    0% { transform: scale(0.7); opacity: 0; }
    60% { transform: scale(1.08); opacity: 1; }
    100% { transform: scale(1); }
}

@keyframes wiggle {
    0% { transform: rotate(0deg); }
    25% { transform: rotate(2deg); }
    50% { transform: rotate(-2deg); }
    75% { transform: rotate(2deg); }
    100% { transform: rotate(0deg); }
}

@keyframes float {
    0% { transform: translateY(0px); }
    50% { transform: translateY(-6px); }
    100% { transform: translateY(0px); }
}

/* ---------------- BACKGROUND ---------------- */

.stApp {
    background: radial-gradient(circle at top left, #fde2ff, #e0f2fe, #fef9c3);
    font-family: "Comic Sans MS", "Segoe UI", sans-serif;
    animation: bounceIn 0.8s ease-out;
}

/* ---------------- TITLES ---------------- */

h1 {
    color: #7c3aed;
    text-shadow: 3px 3px 0 #fde68a;
    animation: bounceIn 0.9s ease-out;
}

h2, h3 {
    color: #2563eb;
}

/* ---------------- SIDEBAR ---------------- */

section[data-testid="stSidebar"] {
    background: #fff7ed;
    border-right: 4px dashed #fb7185;
}

/* ---------------- BUTTONS ---------------- */

.stButton > button {
    background: #a7f3d0;
    border: 4px solid #34d399;
    border-radius: 22px;
    padding: 0.6rem 1.8rem;
    font-size: 16px;
    font-weight: bold;
    box-shadow: 6px 6px 0 #34d399;
    transition: all 0.2s ease;
}

.stButton > button:hover {
    animation: wiggle 0.4s;
    background: #6ee7b7;
    cursor: pointer;
}



/* ---------------- CHAT BUBBLES ---------------- */

[data-testid="stChatMessage"] {
    background: #ffffff;
    border-radius: 22px;
    padding: 16px;
    margin-bottom: 14px;
    box-shadow: 6px 6px 0 #e879f9;
    animation: bounceIn 0.4s ease-out;
}

/* USER bubble */
[data-testid="stChatMessage"][aria-label="user"] {
    background: #dcfce7;
    border: 4px solid #22c55e;
}

/* ASSISTANT bubble */
[data-testid="stChatMessage"][aria-label="assistant"] {
    background: #fce7f3;
    border: 4px solid #ec4899;
}

/* ---------------- CAPTION ---------------- */

.stCaption {
    font-weight: bold;
    color: #6b21a8;
    animation: float 3s ease-in-out infinite;
}

</style>
""", unsafe_allow_html=True)

# ==========================================================
# SESSION STATE
# ==========================================================
if "page" not in st.session_state:
    st.session_state.page = "landing"
if "messages" not in st.session_state:
    st.session_state.messages = []
if "module" not in st.session_state:
    st.session_state.module = None
if "experience" not in st.session_state:
    st.session_state.experience = None

# --- HELPER FUNCTIONS ---
def reset_app():
    st.session_state.page = "landing"
    st.session_state.messages = []
    st.session_state.module = None
    st.session_state.experience = None

def get_llm_response(user_input, module, experience):
    try:
        system_text = f"""
        You are an expert AI Mentor strictly for the domain: {module}.
        You have {experience} years of professional experience.

        RULES:
        1. Answer ONLY questions related to {module}.
        2. If the topic is outside scope, reply exactly:
           "Sorry, I don't know about this question. Please ask something related to the selected module."
        3. Keep answers concise, structured, and beginner-friendly.
        4. Greet politely if the user greets you.
        5. Say goodbye politely if the user says bye
        """

        prompt_template = ChatPromptTemplate.from_messages([
            ("system", system_text),
            ("user", "{input}")
        ])

        llm = ChatGoogleGenerativeAI(
            model="gemini-2.5-flash",
            temperature=0.7,
            google_api_key=os.getenv("gemini")
        )

        chain = prompt_template | llm
        response = chain.invoke({"input": user_input})

        return response.content

    except Exception as e:
        return f"❌ Error connecting to Google Gemini: {str(e)}"

# --- SIDEBAR ---
with st.sidebar:
    st.header("⚙️ Settings")

    if st.session_state.page == "chat" and st.session_state.messages:
        chat_str = "\n".join(
            [f"{msg['role'].upper()}: {msg['content']}" for msg in st.session_state.messages]
        )
        st.download_button("📥 Download Chat (.txt)", chat_str, "mentorship_session.txt")

    st.divider()

    if st.button("🔄 Reset / Start Over"):
        reset_app()
        st.rerun()

# --- PAGE 1: LANDING PAGE ---
if st.session_state.page == "landing":
    st.title("🎓 AI Mentor")
    st.caption("A calm, animated learning companion powered by Generative AI")

    selected_module = st.selectbox(
        "Select Learning Module:",
        ["Python", "SQL", "Machine Learning", "Deep Learning", "Generative AI", "EDA"],
        index=None,
        placeholder="Choose a domain..."
    )

    experience_level = st.number_input(
        "Enter Experience Level (Years):",
        min_value=0,
        max_value=30,
        value=None,
        step=1
    )

    if st.button("Start Mentorship 🚀"):
        if selected_module and experience_level is not None:
            st.session_state.module = selected_module
            st.session_state.experience = experience_level
            st.session_state.page = "chat"
            st.rerun()
        else:
            st.error("⚠️ Please select both a Module and Experience Level.")

# --- PAGE 2: CHAT INTERFACE ---
elif st.session_state.page == "chat":
    st.title(f"📘 {st.session_state.module} Mentor")
    st.caption(f"Persona: {st.session_state.experience} years experience")

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if user_input := st.chat_input("Ask your question…"):
        with st.chat_message("user"):
            st.markdown(user_input)
        st.session_state.messages.append({"role": "user", "content": user_input})

        with st.chat_message("assistant"):
            with st.spinner("Thinking…"):
                response_text = get_llm_response(
                    user_input,
                    st.session_state.module,
                    st.session_state.experience
                )
                st.markdown(response_text)
                st.session_state.messages.append(
                    {"role": "assistant", "content": response_text}
                )