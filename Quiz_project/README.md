
[![GitHub repo](https://img.shields.io/badge/Repo-Python--Mini--Projects-blue?logo=github)](https://github.com/Mullaivendan9894/Python-Mini-Projects)
[![Python](https://img.shields.io/badge/Python-3.8+-blue?logo=python)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Built%20with-Streamlit-ff4b4b?logo=streamlit&logoColor=white)](https://streamlit.io)

# 🧠 Python Quiz App

This is a simple interactive **True/False Quiz App** built using **Object-Oriented Programming (OOP)** in Python and deployed with **Streamlit** for a clean web-based interface.

---

## 🚀 Features

- Object-oriented design using custom classes
- Randomized question order
- Tracks score and progress
- Automatically stops on incorrect answer
- Streamlit-based UI for ease of use

---

## 📁 Project Structure
<pre> ``` 📂 Quiz_Project/ 
├── 📄 app.py # Streamlit UI 
├── 📄 main.py # Console-based quiz 
├── 📄 quiz_brain.py # Handles quiz logic 
├── 📄 question_model.py # Question class definition 
├── 📄 data.py # Contains question data ``` </pre>


---

## 🧩 How It Works

1. The app loads questions from `data.py`.
2. Each question is wrapped in a `Question` object.
3. The `QuizBrain` class handles quiz flow and scoring.
4. The Streamlit interface collects user answers interactively.
5. On the first incorrect answer, the quiz ends and shows the score.

---

## ▶️ Getting Started

### Prerequisites

- Python 3.8 or higher
- Streamlit installed

### Install Dependencies

<pre> pip install streamlit </pre>

<pre> streamlit run app.py </pre>
