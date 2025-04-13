import streamlit as st
from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

# Session state setup
if "quiz" not in st.session_state:
    question_bank = [Question(q["text"], q["answer"]) for q in question_data]
    st.session_state.quiz = QuizBrain(question_bank)
    st.session_state.feedback = ""
    st.session_state.user_answer = ""

quiz = st.session_state.quiz

st.title("🧠 True or False Quiz")

if quiz.still_has_questions():
    current_question = quiz.question_list[quiz.question_number]
    st.subheader(f"Q{quiz.question_number + 1}: {current_question.text}")

    col1, col2 = st.columns(2)
    with col1:
        if st.button("True"):
            st.session_state.user_answer = "True"
    with col2:
        if st.button("False"):
            st.session_state.user_answer = "False"

    if st.session_state.user_answer:
        quiz.question_number += 1
        quiz.check_answer(st.session_state.user_answer, current_question.answer)
        st.session_state.feedback = (
            f"The correct answer was **{current_question.answer}**.\n\n"
            f"Your current score: **{quiz.score}/{quiz.question_number}**"
        )
        st.session_state.user_answer = ""  # Reset for next question
        st.rerun()  

    st.markdown(st.session_state.feedback)
else:
    st.success("🎉 Great! You've completed the quiz.")
    st.write(f"✅ Final Score: **{quiz.score}/{len(quiz.question_list)}**")
    if st.button("Restart"):
        del st.session_state.quiz
        st.rerun() 