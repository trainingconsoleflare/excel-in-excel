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
                "correct_answers": ["10 Million +"],
                "hint": "Excel has 1048576 rows"
            },
            "Excel works with tabular data format": {
                "type": "radio",
                "options": ["Select", "True", "False"],
                "correct_answer": "True",
                "hint": "Excel is primarily designed for working with tabular data."
            },
            "How many columns excel have ? ": {
                "type": "slider",
                "options": list(range(20000)),
                "correct_answer": 16384,
                "hint": "Excel has a maximum of 16,384 columns."
            }
        }
    },
    "Excel Basic Terminology": {
        "video_link": "https://youtu.be/sQgG1htIVCo",
        "share_drive_link": "Link to Excel Formulas notes",
        "questions": {
            "Cell in Excel is formed at the intersection of rows and columns": {
                "type": "radio",
                "options": ["Select", "True", "False"],
                "correct_answer": "True"

            },
            "Active Cell is the cell that we are currently working on": {
                "type": "radio",
                "options": ["Select", "True", "False"],
                "correct_answer": "True"
            },
            "Minimum number of cell to create a range ? ": {
                "type": "slider",
                "options": list(range(1, 6)),  # corrected range
                "correct_answer": 2,
                "hint": 'range means more than one cell'
            },
            "Each formula in excel starts with": {
                "type": "radio",
                "options": ["Select", "=", "==", "--"],
                "correct_answer": "=",
                "hint": 'Each formula in excel always starts with ='
            },
        }
    },
    "Navigation In Excel": {
        "video_link": "https://youtu.be/AxV2HEMD7G0",
        "share_drive_link": "https://arbrecreations-my.sharepoint.com/:b:/g/personal/abhishekm_arbre_in/EWkmqT_bb4tBiItzJ64bFv0BaxyuSbKQ2dw186MDYVjcsg?e=40Qvvc",
        "questions": {
            "Ribbon by default contains how many options": {
                "type": "dropdown",
                "options": ["Select", "7", "9", "11"],
                "correct_answer": "9",
                "hint": 'There are 9 tabs in ribbon.'
            },
            "If a value is at E column and 10th row, What will be its cell reference ? ": {
                "type": "radio",
                "options": ["Select", "10E", "E10"],
                "correct_answer": "E10",
                "hint": 'Cell reference is always the combination of Column and Row name'
            },
            "To apply formulae in each cell , what should we click on": {
                "type": "radio",
                "options": ["Select", "square box", "enter"],
                "correct_answer": "square box",
                "hint": 'Square Box'
            },
        }
    },
    "Working With Tables": {
        "video_link": "https://youtu.be/oco_yyCh7Sc",
        "share_drive_link": "https://arbrecreations-my.sharepoint.com/:b:/g/personal/abhishekm_arbre_in/EarbaAXNDhRMtSaK2OcNZCgBgoWonmTJl4lCXCoJiHeiSg?e=5naQwm",
        "questions": {
            "What option do we use to convert data into an excel table ? ": {
                "type": "dropdown",
                "options": ["Select", "Format as Table", "Table Design", "Format"],
                "correct_answer": "Format as Table",
                "hint": "Under Home tab, There is an option know as format as table, we will always use it to convert it to table"
            },
            "If i want to insert a column anywhere in excel, what will we do": {
                "type": "radio",
                "options": ["Select", "right click and choose insert", "right click and choose add column"],
                "correct_answer": "right click and choose insert"
            },
            "Suppose your manager wants to know the number of orders from Amazon Only.report the number of orders from Amazon.": {
                "type": "dropdown",
                "options": ["Select", "1999", "2000", "950"],
                "correct_answer": "950",
                "hint": "Apply Filter on Retailer."
            }

        }
    },
    "Aggregation and Calculation": {
        "video_link": "https://youtu.be/C-gqG7UelbA",
        "share_drive_link": "https://arbrecreations-my.sharepoint.com/:b:/g/personal/abhishekm_arbre_in/EdjGz6Fn2ZtOvWUXB1_nmNQBZdYXYONhpuGp_YWhK0ItVA?e=ST7RfI",
        "questions": {
            "What option do we use to convert data into an excel table ? ": {
                "type": "dropdown",
                "options": ["Select", "Format as Table", "Table Design", "Format"],
                "correct_answer": "Format as Table",
                "hint": "Under Home tab, There is an option know as format as table, we will always use it to convert it to table"
            },
            "If i want to insert a column anywhere in excel, what will we do": {
                "type": "radio",
                "options": ["Select", "right click and choose insert", "right click and choose add column"],
                "correct_answer": "right click and choose insert"
            },
            "Suppose your manager wants to know the number of orders from Amazon Only.report the number of orders from Amazon.": {
                "type": "dropdown",
                "options": ["Select", "1999", "2000", "950"],
                "correct_answer": "950",
                "hint": "Apply Filter on Retailer."
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
        user_answer = None  # Initialize user_answer variable
        if options["type"] == "multiselect":
            user_answers = st.multiselect("Select all correct answers", options["options"])
            if set(user_answers) == set(options["correct_answers"]):  # Check if the sets match
                score += 1
        elif options["type"] == "radio":
            user_answer = st.radio(f"Select your answer_{i}", options["options"])
            if user_answer is not None:  # Check if user has selected an answer
                if user_answer == options["correct_answer"]:
                    score += 1
                st.write("Your answer is correct!" if user_answer == options["correct_answer"] else "Incorrect answer!")
        elif options["type"] == "slider":
            user_answer = st.slider("Select a value", min_value=0, max_value=len(options["options"]) - 1, step=1)
            if options["options"][user_answer] == options["correct_answer"]:
                score += 1
        elif options["type"] == "dropdown":
            unique_key = f"{selected_topic}_{question}_{i}"  # Unique key for each selectbox
            user_answer = st.selectbox("Select your answer", options["options"], key=unique_key, index=0 if "Select" in options["options"] else 1)  # Set default index based on options
            if user_answer is not None:  # Check if user has selected an answer
                if user_answer == options["correct_answer"]:
                    score += 1
                st.write("Your answer is correct!" if user_answer == options["correct_answer"] else "Incorrect answer!")

        # Validate user's answer
        if user_answer is not None:
            st.write(f"Your answer: {user_answer}")
            if user_answer not in options["options"]:
                st.warning("Invalid answer! Please select a valid option.")

        # Hint box
        if "hint" in options:  # Check if hint is provided
            if st.checkbox(f"Need a hint?_{i}"):
                st.write(options["hint"])

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
