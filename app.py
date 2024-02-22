import streamlit as st

# Define a dictionary mapping topics to their corresponding questions, video links, and share drive links
topics_data = {
    "What is Excel": {
        "video_link": "https://youtu.be/6guuTX1Ml8U",
        "share_drive_link": "https://arbrecreations-my.sharepoint.com/:b:/g/personal/abhishekm_arbre_in/EXcN4q_Pe8hGo1qs0f2QtuYBcKBPSfRINx2wfyVPKRun5Q?e=Tv0OS5",
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
            
            "How many columns excel have ? ": {
                "type": "slider",
                "options": list(range(20000)),
                "correct_answer": 16384
            }
        }
    },
    "Excel Basic Terminology": {
        "video_link": "https://youtu.be/sQgG1htIVCo",
        "share_drive_link": "Link to Excel Formulas notes",
        "questions": {
            "Cell in Excel is formed at the intersection of rows and columns": {
                "type": "radio",
                "options": ["Select", "True","False"],
                "correct_answer": "True"
            },
            "Active Cell is the cell that we are currently working on": {
                "type": "radio",
                "options": ["Select", "True", "False"],
                "correct_answer": "True"
            },
             "Minimum number of cell to create a range ? ": {
                "type": "slider",
                "options": list(range(4)),
                "correct_answer": 2
            },
            "Each formula in excel starts with": {
                "type": "radio",
                "options": ["Select", "=", "==","--"],
                "correct_answer": "="
            },
            
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

# Display share drive link for the selected topic
st.header("Excel Notes")
if selected_topic:
    st.write(f"Notes for {selected_topic}: [{topics_data[selected_topic]['share_drive_link']}]({topics_data[selected_topic]['share_drive_link']})")

# Display questions for the selected topic
st.header("Practice Questions")
if selected_topic:
    st.header(selected_topic)
    questions = topics_data[selected_topic]["questions"]
    total_questions = len(questions)
    score = 0

    for i, (question, options) in enumerate(questions.items()):
        st.subheader(question)
        if options["type"] == "multiselect":
            user_answers = st.multiselect("Select all correct answers", options["options"])
            if user_answers == options["correct_answers"]:
                score += 1
        elif options["type"] == "radio":
            user_answer = st.radio(f"Select your answer_{i}", options["options"])
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

    st.title(f"Your score: {score}/{total_questions}")

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
