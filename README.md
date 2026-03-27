<div align="center">

# 🤖 AI-HR-Agent (Team ET)

![AI Banner](https://raw.githubusercontent.com/Sanskriti21Barve/AI-HR-Agent-/main/agenticai1.png)

**An Agentic AI workflow for autonomous HR onboarding, featuring real-time document extraction and a secure audit trail.**

[![Python](https://img.shields.io/badge/Python-3.12+-blue?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io/)
[![Gemini AI](https://img.shields.io/badge/Google_Gemini-1.5_Flash-8E75B2?style=for-the-badge&logo=google-gemini&logoColor=white)](https://aistudio.google.com/)

[🚀 Setup & Run](#-setup--run-instructions) • [🛠️ Tech Stack](#-tech-stack) • [🌟 Key Features](#-key-features)

</div>

---

## 🎯 About the Project
**AI-HR-Agent** automates the tedious part of HR onboarding. Using **Gemini 1.5 Flash**, it "reads" employee ID cards to instantly verify identity and log the process for corporate compliance.

---

## 🛠️ Tech Stack

| Technology | Purpose |
| :--- | :--- |
| <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" width="30"> **Python** | Core Backend Logic |
| <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/streamlit/streamlit-original.svg" width="30"> **Streamlit** | Dashboard UI/UX |
| <img src="https://www.gstatic.com/lamda/images/favicon_v1_15011f02930615bfc441.svg" width="30"> **Gemini 1.5 Flash** | AI Vision Extraction |
| <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/git/git-original.svg" width="30"> **Git & GitHub** | Version Control |

---

## ⚙️ Setup & Run Instructions

### 1️⃣ Install Dependencies
Ensure you have Python installed, then run:
```bash
pip install streamlit google-generativeai python-dotenv

2️⃣ Configure API Key
Create a file named .env in the root folder and add your Gemini API key:

Code snippet
GEMINI_API_KEY=your_actual_api_key_here
3️⃣ Run the Application
Start the Team ET dashboard with this command:

Bash
streamlit run app.py
4️⃣ Test with Samples
Upload the provided james.png from the repository to see the AI agent verify a user in real-time.

🌟 Key Features
⚡ AI Extraction: Instantly pulls Name, Dept, and Role from IDs.

📜 Audit Trail: Every action is logged in audit_log.txt for HR records.

🛡️ Secure: Uses .gitignore to keep your private API keys safe.

🎉 UI Celebrations: Interactive success balloons upon verification.

<div align="center">
