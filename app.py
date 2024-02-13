import streamlit as st

# Define a dictionary mapping topics to their corresponding questions and video links
topics_data = {
    "What is Excel": {
        "video_link": "https://youtu.be/6guuTX1Ml8U",
        "questions": {
            "How many rows can Excel handle?": {
                "type": "multiselect",
                "options": ["Select", "10 Million +", "11 Million +", "20 Million +"],
                "correct_answers": ["10 Million +"]
            },
            "Excel works with tabular data format": {
                "type": "radio",
                "options": ["Select", "True", "False"],
                "correct_answer": "True"
            },
            "What is the best feature of Excel?": {
                "type": "text",
                "correct_answer": "Pivot tables"
            },
            "On a scale of 1 to 10, how much do you like Excel?": {
                "type": "slider",
                "options": list(range(11)),
                "correct_answer": 10
            }
        }
    },
    "Excel Formulas": {
        "video_link": "https://youtu.be/sQgG1htIVCo",
        "questions": {
            "What does VLOOKUP function do?": {
                "type": "radio",
                "options": ["Select", "Returns the maximum value from a range", "Searches for a value in the first column of a table and returns a value in the same row from another column", "Counts the number of cells that contain numbers"],
                "correct_answer": "Searches for a value in the first column of a table and returns a value in the same row from another column"
            },
            "How do you lock a cell reference in a formula?": {
                "type": "multiselect",  # Change to multiselect for checkboxes
                "options": ["$A$1", "$A1", "A$1", "None of the above"],
                "correct_answers": ["$A$1"]
            },
            "What is the Excel function to count cells?": {
                "type": "dropdown",
                "options": ["Select", "COUNT", "COUNTA", "COUNTIF"],
                "correct_answer": "COUNT"
            }
        }
    }
}

# Initialize session state variables
if 'topic_idx' not in st.session_state:
    st.session_state.topic_idx = 0

# Sidebar dropdown to select the topic
selected_topic = st.sidebar.selectbox("Select Excel Topic", list(topics_data.keys()), index=st.session_state.topic_idx)

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
        elif options["type"] == "checkbox":  # Change this to multiselect
            user_answers = st.multiselect("Select correct answers", options["options"])
            if user_answers == options["correct_answers"]:
                score += 1
        elif options["type"] == "text":
            user_answer = st.text_input("Your answer:")
            if user_answer.lower() == options["correct_answer"].lower():
                score += 1
        elif options["type"] == "slider":
            user_answer = st.slider("Select a value", min_value=0, max_value=len(options["options"]) - 1, step=1)
            if options["options"][user_answer] == options["correct_answer"]:
                score += 1
        elif options["type"] == "dropdown":
            user_answer = st.selectbox("Select your answer", options["options"])
            if user_answer == options["correct_answer"]:
                score += 1

    st.write(f"Your score: {score}/{total_questions}")

# Layout for "Next" and "Back" buttons
col1, col2, _ = st.columns([1, 7, 1])

# Button to go to the next topic
next_topic_idx = st.session_state.topic_idx + 1
if next_topic_idx < len(topics_data):
    if col2.button("Next", key="next_button", on_click=lambda: st.session_state.update(topic_idx=next_topic_idx)):
        st.session_state.topic_idx = next_topic_idx


# Button to go to the previous topic
prev_topic_idx = st.session_state.topic_idx - 1
if prev_topic_idx >= 0:
    if col1.button("Back", key="back_button", on_click=lambda: st.session_state.update(topic_idx=prev_topic_idx)):
        st.session_state.topic_idx = prev_topic_idx
