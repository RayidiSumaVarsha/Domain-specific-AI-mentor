# AI Chatbot Mentor – Domain-Specific Intelligent Learning Assistant

AI Chatbot Mentor is an interactive, AI-powered mentoring application designed to provide **focused, module-specific learning assistance** across multiple technical domains.  
Unlike generic AI chatbots, this system strictly responds **only within the selected module**, ensuring accurate, relevant, and distraction-free mentorship.

The application is built using **Streamlit** for the user interface and **LangChain** for LLM orchestration, enabling controlled, conversational intelligence with domain restrictions.

---

## 🚀 Project Overview

AI Chatbot Mentor acts as a **personalized AI mentor** that guides users in a selected technical domain.  
Once a module is chosen, the chatbot behaves as a dedicated mentor for that module and refuses to answer questions outside its scope.

This project highlights:
- Domain-restricted AI behavior
- Session-based conversation memory
- Chat history export for offline learning
- Clean and simple UI design

---

## 👋 Welcome Screen

When the application starts, users are greeted with the following message:

> **Welcome to AI Chatbot Mentor**  
> Your personalized AI learning assistant.  
> Please select a learning module to begin your mentoring session.

---

## 📌 Available Learning Modules

Users can select **one module per session** from the following list:

- Python  
- SQL  
- Power BI  
- Exploratory Data Analysis (EDA)  
- Machine Learning (ML)  
- Deep Learning (DL)  
- Generative AI (Gen AI)  
- Agentic AI  

---

## 🎯 Module-Specific Mentor Interface

After selecting a module, the application opens a **dedicated chat interface** for that module.

### Example (Python Module):
> **Welcome to Python AI Mentor 🐍**  
> I am your dedicated mentor for Python.  
> How can I help you today?

The same structure applies to all other modules.

---

## 🧠 Question Handling Logic

### ✅ Relevant Questions
- The AI mentor answers **only questions related to the selected module**
- Responses are clear, structured, and educational
- Conversation context is preserved throughout the session

### ❌ Irrelevant Questions
If the user asks a question outside the selected module, the chatbot strictly responds with:

> *Sorry, I don’t know about this question. Please ask something related to the selected module.*

This ensures **strict domain control** and avoids hallucinated or misleading responses.

---

## 💬 Conversation Flow

- Full chat history is maintained during the session
- Each user query and AI response is appended to the conversation log
- Context is preserved for continuous and coherent mentoring
- The session ends when the user types **“bye”**

---

## 📥 Download Chat History (Key Feature)

The application provides a **Download Conversation** option at any point during the chat.

### Features:
- Downloads the **entire conversation**
- Includes both **user queries and AI responses**
- File format: **`.txt` only**
- Useful for:
  - Revision
  - Notes
  - Offline learning
  - Portfolio documentation

⚠️ This feature is **mandatory** and a core highlight of the project.

---

## ✅ Functional Requirements

- Module-based AI mentoring  
- Strict domain-specific responses  
- Rejection of irrelevant questions  
- Session-based conversation memory  
- Chat history download option (`.txt`)  
- Simple and clean Streamlit UI  

---

## 🏗️ Technical Architecture

### 🧠 Backend Logic
- **LangChain**
  - Module-specific prompt templates
  - Domain restriction rules
  - Conversation memory management

### 🖥️ Frontend
- **Streamlit**
  - Module selection interface
  - Chat-style user interface
  - Download button for conversation history

---

## 🛠️ Tech Stack

| Component | Technology |
|---------|-----------|
| Frontend | Streamlit |
| AI Orchestration | LangChain |
| LLM | Open-source / API-based (configurable) |
| File Export | Text (`.txt`) |

---

## 📚 Expected Learning Outcomes

By completing this project, learners will understand:

- How to build **domain-restricted AI chatbots**
- Prompt engineering for controlled responses
- Using LangChain with conversation memory
- Designing interactive Streamlit applications
- Implementing chat export functionality
- Structuring real-world AI mentor systems

---

## 🏁 Conclusion

AI Chatbot Mentor demonstrates how intelligent systems can be designed to deliver **focused, reliable, and learner-centric AI mentorship**.  
By enforcing strict domain control and providing practical features like conversation download, this project bridges the gap between generic chatbots and real-world educational AI assistants.

---

## 📌 How to Run the Project

```bash
# Install dependencies
pip install -r requirements.txt

# Run the Streamlit app
streamlit run app.py
