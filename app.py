import streamlit as st

# Define a dictionary mapping topics to their corresponding questions and video links
topics_data = {
    "What is Excel": {
        "video_link": "https://youtu.be/6guuTX1Ml8U",
        "questions": {
            "How many rows can excel handle": {
                "type": "multiselect",
                "options": ["Select","10 Million +", "11 Million +", "20 Million +"],
                "correct_answers": ["10 Million +"]
            },
            "Excel works with tabular data format": {
                "type": "radio",
                "options": ["Select","True", "False"],
                "correct_answer": "Go to View tab and select Freeze Panes"
            }
        }
    },
    "Excel Formulas": {
        "video_link": "https://youtu.be/sQgG1htIVCo",
        "questions": {
            "What does VLOOKUP function do?": {
                "type": "radio",
                "options": ["Returns the maximum value from a range", "Searches for a value in the first column of a table and returns a value in the same row from another column", "Counts the number of cells that contain numbers"],
                "correct_answer": "Searches for a value in the first column of a table and returns a value in the same row from another column"
            },
            "How do you lock a cell reference in a formula?": {
                "type": "checkbox",
                "options": ["$A$1", "$A1", "A$1", "None of the above"],
                "correct_answers": ["$A$1"]
            }
        }
    }
}

# Sidebar dropdown to select the topic
selected_topic = st.sidebar.selectbox("Select Excel Topic", list(topics_data.keys()))

# Display video for the selected topic
st.header("Excel Topic Video")
if selected_topic:
    st.video(topics_data[selected_topic]["video_link"])

# Display questions for the selected topic
st.header("Practice Questions")
if selected_topic:
    st.header(selected_topic)
    questions = topics_data[selected_topic]["questions"]
    total_questions = len(questions)
    score = 0

    for question, options in questions.items():
        st.subheader(question)
        if options["type"] == "multiselect":
            user_answers = st.multiselect("Select all correct answers", options["options"])
            if user_answers == options["correct_answers"]:
                score += 1
        elif options["type"] == "radio":
            user_answer = st.radio("Select your answer", options["options"])
            if user_answer == options["correct_answer"]:
                score += 1
        elif options["type"] == "checkbox":
            user_answers = st.checkbox("Select correct answers", options["options"])
            if user_answers == options["correct_answers"]:
                score += 1

    st.write(f"Your score: {score}/{total_questions}")
