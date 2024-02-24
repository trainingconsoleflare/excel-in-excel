# import streamlit as st

# # Define a dictionary mapping topics to their corresponding questions, video links, and share drive links
# topics_data = {
#     "What is Excel": {
#         "video_link": "https://youtu.be/6guuTX1Ml8U",
#         "share_drive_link": "https://arbrecreations-my.sharepoint.com/:b:/g/personal/abhishekm_arbre_in/EXcN4q_Pe8hGo1qs0f2QtuYBcKBPSfRINx2wfyVPKRun5Q?e=Tv0OS5",
#         "notes_embed_code": """<iframe loading="lazy" style="position: relative; width: 100%; height: 600px; max-height: 80vh; border: none; padding: 0; margin: 0; overflow: hidden;"
#       src="https:&#x2F;&#x2F;www.canva.com&#x2F;design&#x2F;DAF9sGjoscE&#x2F;tZsnSI4oFVkphT3TH0fNrg&#x2F;view?embed" allowfullscreen="allowfullscreen" allow="fullscreen">
#     </iframe>
#     <a href="https:&#x2F;&#x2F;www.canva.com&#x2F;design&#x2F;DAF9sGjoscE&#x2F;tZsnSI4oFVkphT3TH0fNrg&#x2F;view?utm_content=DAF9sGjoscE&amp;utm_campaign=designshare&amp;utm_medium=embeds&amp;utm_source=link" target="_blank" rel="noopener">Excel Fundamentals</a> by Console Flare""",
#         "questions": {
#             "How many rows can Excel handle?": {
#                 "type": "radio",
#                 "options": ["Select", "10 Million +", "11 Million +", "20 Million +"],
#                 "correct_answer": "10 Million +",
#                 "hint": "Excel has 1048576 rows"
#             },
#             "Excel works with tabular data format": {
#                 "type": "radio",
#                 "options": ["Select", "True", "False"],
#                 "correct_answer": "True",
#                 "hint": "Excel is primarily designed for working with tabular data."
#             },
#             "Excel is a product of": {
#                 "type": "radio",
#                 "options": ["Select", "Microsoft", "Yahoo"],
#                 "correct_answer": "Microsoft",
#                 "hint": "Excel is developed by Microsoft"
#             },
#             "Is there any sector that does not use Excel": {
#                 "type": "radio",
#                 "options": ["Select", "Yes", "No"],
#                 "correct_answer": "No",
#                 "hint": "Excel is used all around the world"
#             },
#         }
#     },
#     "Excel Basic Terminology": {
#         "video_link": "https://youtu.be/sQgG1htIVCo",
#         "share_drive_link": "Link to Excel Formulas notes",
#          "notes_embed_code": """<iframe loading="lazy" style="position: relative; width: 100%; height: 600px; max-height: 80vh; border: none; padding: 0; margin: 0; overflow: hidden;"
#       src="https:&#x2F;&#x2F;www.canva.com&#x2F;design&#x2F;DAF9sGjoscE&#x2F;tZsnSI4oFVkphT3TH0fNrg&#x2F;view?embed" allowfullscreen="allowfullscreen" allow="fullscreen">
#     </iframe>
#     <a href="https:&#x2F;&#x2F;www.canva.com&#x2F;design&#x2F;DAF9sGjoscE&#x2F;tZsnSI4oFVkphT3TH0fNrg&#x2F;view?utm_content=DAF9sGjoscE&amp;utm_campaign=designshare&amp;utm_medium=embeds&amp;utm_source=link" target="_blank" rel="noopener">Excel Fundamentals</a> by Console Flare""",
#         "questions": {
#             "Cell in Excel is formed at the intersection of rows and columns": {
#                 "type": "radio",
#                 "options": ["Select", "True", "False"],
#                 "correct_answer": "True"
#             },
#             "Active Cell is the cell that we are currently working on": {
#                 "type": "radio",
#                 "options": ["Select", "True", "False"],
#                 "correct_answer": "True"
#             },
#             "Minimum number of cells to create a range?": {
#                 "type": "radio",
#                 "options": ["Select","1","2","3","5"],
#                 "correct_answer": "2",
#                 "hint": 'A range consists of more than one cell'
#             },
#             "Each formula in excel starts with": {
#                 "type": "radio",
#                 "options": ["Select", "=", "==", "--"],
#                 "correct_answer": "=",
#                 "hint": 'Each formula in excel always starts with ='
#             },
#         }
#     },
#       "Navigation In Excel": {
#         "video_link": "https://youtu.be/AxV2HEMD7G0",
#         "share_drive_link": "https://arbrecreations-my.sharepoint.com/:b:/g/personal/abhishekm_arbre_in/EWkmqT_bb4tBiItzJ64bFv0BaxyuSbKQ2dw186MDYVjcsg?e=40Qvvc",
#          "notes_embed_code": """<iframe loading="lazy" style="position: relative; width: 100%; height: 600px; max-height: 80vh; border: none; padding: 0; margin: 0; overflow: hidden;"
#       src="https:&#x2F;&#x2F;www.canva.com&#x2F;design&#x2F;DAF9O5RVQ3M&#x2F;MMZIBNN1x7bGa__Pdz4m6w&#x2F;view?embed" allowfullscreen="allowfullscreen" allow="fullscreen">
#     </iframe>
#     <a href="https:&#x2F;&#x2F;www.canva.com&#x2F;design&#x2F;DAF9O5RVQ3M&#x2F;MMZIBNN1x7bGa__Pdz4m6w&#x2F;view?utm_content=DAF9O5RVQ3M&amp;utm_campaign=designshare&amp;utm_medium=embeds&amp;utm_source=link" target="_blank" rel="noopener">Navigating In Excel</a> by Console Flare""",
#         "questions": {
#             "Ribbon by default contains how many options": {
#                 "type": "dropdown",
#                 "options": ["Select", "7", "9", "11"],
#                 "correct_answer": "9",
#                 "hint": 'There are 9 tabs in ribbon.'
#             },
#             "If a value is at E column and 10th row, What will be its cell reference ? ": {
#                 "type": "radio",
#                 "options": ["Select", "10E", "E10"],
#                 "correct_answer": "E10",
#                 "hint": 'Cell reference is always the combination of Column and Row name'
#             },
#             "To apply formulae in each cell , what should we click on": {
#                 "type": "radio",
#                 "options": ["Select", "square box", "enter"],
#                 "correct_answer": "square box",
#                 "hint": 'Square Box'
#             },
#         }
#     },
#     "Working With Tables": {
#         "video_link": "https://youtu.be/oco_yyCh7Sc",
#         "share_drive_link": "https://arbrecreations-my.sharepoint.com/:b:/g/personal/abhishekm_arbre_in/EarbaAXNDhRMtSaK2OcNZCgBgoWonmTJl4lCXCoJiHeiSg?e=5naQwm",
#         "notes_embed_code":"""<iframe loading="lazy" style="position: relative; width: 100%; height: 600px; max-height: 80vh; border: none; padding: 0; margin: 0; overflow: hidden;"
#       src="https:&#x2F;&#x2F;www.canva.com&#x2F;design&#x2F;DAF9TVG7sYU&#x2F;QRQkLgNWY0uj_lkjytJPaQ&#x2F;view?embed" allowfullscreen="allowfullscreen" allow="fullscreen">
#     </iframe>
#     <a href="https:&#x2F;&#x2F;www.canva.com&#x2F;design&#x2F;DAF9TVG7sYU&#x2F;QRQkLgNWY0uj_lkjytJPaQ&#x2F;view?utm_content=DAF9TVG7sYU&amp;utm_campaign=designshare&amp;utm_medium=embeds&amp;utm_source=link" target="_blank" rel="noopener">Working With Tables</a> by Console Flare""",
#         "questions": {
#             "What option do we use to convert data into an excel table ? ": {
#                 "type": "dropdown",
#                 "options": ["Select", "Format as Table", "Table Design", "Format"],
#                 "correct_answer": "Format as Table",
#                 "hint": "Under Home tab, There is an option know as format as table, we will always use it to convert it to table"
#             },
#             "If i want to insert a column anywhere in excel, what will we do": {
#                 "type": "radio",
#                 "options": ["Select", "right click and choose insert", "right click and choose add column"],
#                 "correct_answer": "right click and choose insert"
#             },
#             "Suppose your manager wants to know the number of orders from Amazon Only.report the number of orders from Amazon.": {
#                 "type": "dropdown",
#                 "options": ["Select", "1999", "2000", "950"],
#                 "correct_answer": "950",
#                 "hint": "Apply Filter on Retailer."
#             }

#         }
#     },
#     "Aggregation and Calculation": {
#         "video_link": "https://youtu.be/C-gqG7UelbA",
#         "share_drive_link": "https://arbrecreations-my.sharepoint.com/:b:/g/personal/abhishekm_arbre_in/EdjGz6Fn2ZtOvWUXB1_nmNQBZdYXYONhpuGp_YWhK0ItVA?e=ST7RfI",
#         "notes_embed_code":"""<iframe loading="lazy" style="position: relative; width: 100%; height: 600px; max-height: 80vh; border: none; padding: 0; margin: 0; overflow: hidden;"
#       src="https:&#x2F;&#x2F;www.canva.com&#x2F;design&#x2F;DAF9UfqWTpE&#x2F;1D8vEErXwvnv7QD8ita-eg&#x2F;view?embed" allowfullscreen="allowfullscreen" allow="fullscreen">
#     </iframe>
#     <a href="https:&#x2F;&#x2F;www.canva.com&#x2F;design&#x2F;DAF9UfqWTpE&#x2F;1D8vEErXwvnv7QD8ita-eg&#x2F;view?utm_content=DAF9UfqWTpE&amp;utm_campaign=designshare&amp;utm_medium=embeds&amp;utm_source=link" target="_blank" rel="noopener">Aggregation and Calculation</a> by Console Flare""",
#         "questions": {
#             "What option do we use to convert data into an excel table ? ": {
#                 "type": "dropdown",
#                 "options": ["Select", "Format as Table", "Table Design", "Format"],
#                 "correct_answer": "Format as Table",
#                 "hint": "Under Home tab, There is an option know as format as table, we will always use it to convert it to table"
#             },
#             "If i want to insert a column anywhere in excel, what will we do": {
#                 "type": "radio",
#                 "options": ["Select", "right click and choose insert", "right click and choose add column"],
#                 "correct_answer": "right click and choose insert"
#             },
#             "Suppose your manager wants to know the number of orders from Amazon Only.report the number of orders from Amazon.": {
#                 "type": "dropdown",
#                 "options": ["Select", "1999", "2000", "950"],
#                 "correct_answer": "950",
#                 "hint": "Apply Filter on Retailer."
#             }

#         }
#     },
#     "Totals and Subtotals": {
#         "video_link": "https://youtu.be/XV_ZUj-y7g0",
#         "share_drive_link": "https://arbrecreations-my.sharepoint.com/:b:/g/personal/abhishekm_arbre_in/EdjGz6Fn2ZtOvWUXB1_nmNQBZdYXYONhpuGp_YWhK0ItVA?e=ST7RfI",
#         "notes_embed_code":"""<iframe loading="lazy" style="position: relative; width: 100%; height: 600px; max-height: 80vh; border: none; padding: 0; margin: 0; overflow: hidden;"
#       src="https:&#x2F;&#x2F;www.canva.com&#x2F;design&#x2F;DAF9UfqWTpE&#x2F;1D8vEErXwvnv7QD8ita-eg&#x2F;view?embed" allowfullscreen="allowfullscreen" allow="fullscreen">
#     </iframe>
#     <a href="https:&#x2F;&#x2F;www.canva.com&#x2F;design&#x2F;DAF9UfqWTpE&#x2F;1D8vEErXwvnv7QD8ita-eg&#x2F;view?utm_content=DAF9UfqWTpE&amp;utm_campaign=designshare&amp;utm_medium=embeds&amp;utm_source=link" target="_blank" rel="noopener">Aggregation and Calculation</a> by Console Flare""",
#         "questions": {
#             "What option do we use to convert data into an excel table ? ": {
#                 "type": "dropdown",
#                 "options": ["Select", "Format as Table", "Table Design", "Format"],
#                 "correct_answer": "Format as Table",
#                 "hint": "Under Home tab, There is an option know as format as table, we will always use it to convert it to table"
#             },
#             "If i want to insert a column anywhere in excel, what will we do": {
#                 "type": "radio",
#                 "options": ["Select", "right click and choose insert", "right click and choose add column"],
#                 "correct_answer": "right click and choose insert"
#             },
#             "Suppose your manager wants to know the number of orders from Amazon Only.report the number of orders from Amazon.": {
#                 "type": "dropdown",
#                 "options": ["Select", "1999", "2000", "950"],
#                 "correct_answer": "950",
#                 "hint": "Apply Filter on Retailer."
#             }

#         }
#     },
#     "Data Validation": {
#         "video_link": "https://youtu.be/4Q-aWCRouis",
#         "share_drive_link": "https://arbrecreations-my.sharepoint.com/:b:/g/personal/abhishekm_arbre_in/EdjGz6Fn2ZtOvWUXB1_nmNQBZdYXYONhpuGp_YWhK0ItVA?e=ST7RfI",
#         "notes_embed_code":"""<iframe loading="lazy" style="position: relative; width: 100%; height: 600px; max-height: 80vh; border: none; padding: 0; margin: 0; overflow: hidden;"
#       src="https:&#x2F;&#x2F;www.canva.com&#x2F;design&#x2F;DAF9bFAd4wQ&#x2F;GJpB2Hxu2eyjRDlrsbdFLw&#x2F;view?embed" allowfullscreen="allowfullscreen" allow="fullscreen">
#     </iframe>
#     <a href="https:&#x2F;&#x2F;www.canva.com&#x2F;design&#x2F;DAF9bFAd4wQ&#x2F;GJpB2Hxu2eyjRDlrsbdFLw&#x2F;view?utm_content=DAF9bFAd4wQ&amp;utm_campaign=designshare&amp;utm_medium=embeds&amp;utm_source=link" target="_blank" rel="noopener">Data Validation</a> by Console Flare""",
#         "questions": {
#             "What option do we use to convert data into an excel table ? ": {
#                 "type": "dropdown",
#                 "options": ["Select", "Format as Table", "Table Design", "Format"],
#                 "correct_answer": "Format as Table",
#                 "hint": "Under Home tab, There is an option know as format as table, we will always use it to convert it to table"
#             },
#             "If i want to insert a column anywhere in excel, what will we do": {
#                 "type": "radio",
#                 "options": ["Select", "right click and choose insert", "right click and choose add column"],
#                 "correct_answer": "right click and choose insert"
#             },
#             "Suppose your manager wants to know the number of orders from Amazon Only.report the number of orders from Amazon.": {
#                 "type": "dropdown",
#                 "options": ["Select", "1999", "2000", "950"],
#                 "correct_answer": "950",
#                 "hint": "Apply Filter on Retailer."
#             }

#         }
#     }

 
    
    
#     # Other topics follow...

# }

# # Function to display questions and get user answers
# def display_questions(questions):
#     score = 0
#     for i, (question, options) in enumerate(questions.items()):
#         st.subheader(question)
#         user_answer = None  # Initialize user_answer variable
#         if options["type"] == "multiselect":
#             user_answers = st.multiselect("Select all correct answers", options["options"])
#             if set(user_answers) == set(options["correct_answers"]):  # Check if the sets match
#                 st.success("Correct!")
#                 score += 1
#             elif "Select" not in user_answers:  # Don't show incorrect if default is not selected
#                 st.error("Incorrect!")
#         elif options["type"] == "radio":
#             radio_key = f"{question}_radio_{i}"
#             user_answer = st.radio("Select your answer", options["options"],key=radio_key)
#             if user_answer == options["correct_answer"]:
#                 st.success("Correct!")
#                 score += 1
#             elif user_answer != "Select":  # Don't show incorrect if default is not selected
#                 st.error("Incorrect!")
#         elif options["type"] == "slider":
#             user_answer = st.slider("Select a value", min_value=0, max_value=len(options["options"]) - 1, step=1)
#             if options["options"][user_answer] == options["correct_answer"]:
#                 st.success("Correct!")
#                 score += 1
#             elif user_answer != 0:  # Don't show incorrect if default is not selected
#                 st.error("Incorrect!")
#         elif options["type"] == "dropdown":
#             user_answer = st.selectbox("Select your answer", options["options"])
#             if user_answer == options["correct_answer"]:
#                 st.success("Correct!")
#                 score += 1
#             elif user_answer != "Select":  # Don't show incorrect if default is not selected
#                 st.error("Incorrect!")

#         # Validate user's answer
#         if user_answer is not None:
#             st.write(f"Your answer: {user_answer}")
#             if user_answer not in options["options"]:
#                 st.warning("Invalid answer! Please select a valid option.")

#         # Hint box
#         if "hint" in options:  # Check if hint is provided
#             if st.checkbox(f"Need a hint?_{i}"):
#                 st.write(options["hint"])

#     st.title(f"Your score: {score}/{len(questions)}")


# # Main code
# st.set_page_config(layout="wide")  # Optimize layout for mobile devices
# st.title("Excel Learning App")

# # Sidebar dropdown to select the topic
# selected_topic = st.sidebar.selectbox("Select Excel Topic", list(topics_data.keys()))

# # Display video for the selected topic
# st.header(selected_topic)
# if selected_topic:
#     st.video(topics_data[selected_topic]["video_link"])

# # Display share drive link for the selected topic
# st.header("Excel Notes")
# if selected_topic:
#     st.write(f"Notes for {selected_topic}:")
#     st.write(topics_data[selected_topic]["notes_embed_code"], unsafe_allow_html=True)

# # Display questions for the selected topic
# st.header("Practice Questions")
# if selected_topic:
#     display_questions(topics_data[selected_topic]["questions"])


#-----------------------------------------------------Version 2 ------------------------------------------------------------

import streamlit as st

# Define a dictionary mapping topics to their corresponding questions, video links, and share drive links
topics_data = {
    "What is Excel": {
        "video_link": "https://youtu.be/6guuTX1Ml8U",
        "share_drive_link": "https://arbrecreations-my.sharepoint.com/:b:/g/personal/abhishekm_arbre_in/EXcN4q_Pe8hGo1qs0f2QtuYBcKBPSfRINx2wfyVPKRun5Q?e=Tv0OS5",
        "notes_embed_code": """<iframe loading="lazy" style="position: relative; width: 100%; height: 600px; max-height: 80vh; border: none; padding: 0; margin: 0; overflow: hidden;"
      src="https:&#x2F;&#x2F;www.canva.com&#x2F;design&#x2F;DAF9sGjoscE&#x2F;tZsnSI4oFVkphT3TH0fNrg&#x2F;view?embed" allowfullscreen="allowfullscreen" allow="fullscreen">
    </iframe>
    <a href="https:&#x2F;&#x2F;www.canva.com&#x2F;design&#x2F;DAF9sGjoscE&#x2F;tZsnSI4oFVkphT3TH0fNrg&#x2F;view?utm_content=DAF9sGjoscE&amp;utm_campaign=designshare&amp;utm_medium=embeds&amp;utm_source=link" target="_blank" rel="noopener">Excel Fundamentals</a> by Console Flare""",
        "questions": {
            "How many rows can Excel handle?": {
                "type": "radio",
                "options": ["Select", "10 Million +", "11 Million +", "20 Million +"],
                "correct_answer": "10 Million +",
                "hint": "Excel has 1048576 rows"
            },
            "Excel works with tabular data format": {
                "type": "radio",
                "options": ["Select", "True", "False"],
                "correct_answer": "True",
                "hint": "Excel is primarily designed for working with tabular data."
            },
            "Excel is a product of": {
                "type": "radio",
                "options": ["Select", "Microsoft", "Yahoo"],
                "correct_answer": "Microsoft",
                "hint": "Excel is developed by Microsoft"
            },
            "Is there any sector that does not use Excel": {
                "type": "radio",
                "options": ["Select", "Yes", "No"],
                "correct_answer": "No",
                "hint": "Excel is used all around the world"
            },
        }
    },
    "Excel Basic Terminology": {
        "video_link": "https://youtu.be/sQgG1htIVCo",
        "share_drive_link": "Link to Excel Formulas notes",
         "notes_embed_code": """<iframe loading="lazy" style="position: relative; width: 100%; height: 600px; max-height: 80vh; border: none; padding: 0; margin: 0; overflow: hidden;"
      src="https:&#x2F;&#x2F;www.canva.com&#x2F;design&#x2F;DAF9sGjoscE&#x2F;tZsnSI4oFVkphT3TH0fNrg&#x2F;view?embed" allowfullscreen="allowfullscreen" allow="fullscreen">
    </iframe>
    <a href="https:&#x2F;&#x2F;www.canva.com&#x2F;design&#x2F;DAF9sGjoscE&#x2F;tZsnSI4oFVkphT3TH0fNrg&#x2F;view?utm_content=DAF9sGjoscE&amp;utm_campaign=designshare&amp;utm_medium=embeds&amp;utm_source=link" target="_blank" rel="noopener">Excel Fundamentals</a> by Console Flare""",
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
            "Minimum number of cells to create a range?": {
                "type": "radio",
                "options": ["Select","1","2","3","5"],
                "correct_answer": "2",
                "hint": 'A range consists of more than one cell'
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
         "notes_embed_code": """<iframe loading="lazy" style="position: relative; width: 100%; height: 600px; max-height: 80vh; border: none; padding: 0; margin: 0; overflow: hidden;"
      src="https:&#x2F;&#x2F;www.canva.com&#x2F;design&#x2F;DAF9O5RVQ3M&#x2F;MMZIBNN1x7bGa__Pdz4m6w&#x2F;view?embed" allowfullscreen="allowfullscreen" allow="fullscreen">
    </iframe>
    <a href="https:&#x2F;&#x2F;www.canva.com&#x2F;design&#x2F;DAF9O5RVQ3M&#x2F;MMZIBNN1x7bGa__Pdz4m6w&#x2F;view?utm_content=DAF9O5RVQ3M&amp;utm_campaign=designshare&amp;utm_medium=embeds&amp;utm_source=link" target="_blank" rel="noopener">Navigating In Excel</a> by Console Flare""",
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
        "notes_embed_code":"""<iframe loading="lazy" style="position: relative; width: 100%; height: 600px; max-height: 80vh; border: none; padding: 0; margin: 0; overflow: hidden;"
      src="https:&#x2F;&#x2F;www.canva.com&#x2F;design&#x2F;DAF9TVG7sYU&#x2F;QRQkLgNWY0uj_lkjytJPaQ&#x2F;view?embed" allowfullscreen="allowfullscreen" allow="fullscreen">
    </iframe>
    <a href="https:&#x2F;&#x2F;www.canva.com&#x2F;design&#x2F;DAF9TVG7sYU&#x2F;QRQkLgNWY0uj_lkjytJPaQ&#x2F;view?utm_content=DAF9TVG7sYU&amp;utm_campaign=designshare&amp;utm_medium=embeds&amp;utm_source=link" target="_blank" rel="noopener">Working With Tables</a> by Console Flare""",
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
        "notes_embed_code":"""<iframe loading="lazy" style="position: relative; width: 100%; height: 600px; max-height: 80vh; border: none; padding: 0; margin: 0; overflow: hidden;"
      src="https:&#x2F;&#x2F;www.canva.com&#x2F;design&#x2F;DAF9UfqWTpE&#x2F;1D8vEErXwvnv7QD8ita-eg&#x2F;view?embed" allowfullscreen="allowfullscreen" allow="fullscreen">
    </iframe>
    <a href="https:&#x2F;&#x2F;www.canva.com&#x2F;design&#x2F;DAF9UfqWTpE&#x2F;1D8vEErXwvnv7QD8ita-eg&#x2F;view?utm_content=DAF9UfqWTpE&amp;utm_campaign=designshare&amp;utm_medium=embeds&amp;utm_source=link" target="_blank" rel="noopener">Aggregation and Calculation</a> by Console Flare""",
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
    "Totals and Subtotals": {
        "video_link": "https://youtu.be/XV_ZUj-y7g0",
        "share_drive_link": "https://arbrecreations-my.sharepoint.com/:b:/g/personal/abhishekm_arbre_in/EdjGz6Fn2ZtOvWUXB1_nmNQBZdYXYONhpuGp_YWhK0ItVA?e=ST7RfI",
        "notes_embed_code":"""<iframe loading="lazy" style="position: relative; width: 100%; height: 600px; max-height: 80vh; border: none; padding: 0; margin: 0; overflow: hidden;"
      src="https:&#x2F;&#x2F;www.canva.com&#x2F;design&#x2F;DAF9UfqWTpE&#x2F;1D8vEErXwvnv7QD8ita-eg&#x2F;view?embed" allowfullscreen="allowfullscreen" allow="fullscreen">
    </iframe>
    <a href="https:&#x2F;&#x2F;www.canva.com&#x2F;design&#x2F;DAF9UfqWTpE&#x2F;1D8vEErXwvnv7QD8ita-eg&#x2F;view?utm_content=DAF9UfqWTpE&amp;utm_campaign=designshare&amp;utm_medium=embeds&amp;utm_source=link" target="_blank" rel="noopener">Aggregation and Calculation</a> by Console Flare""",
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
    "Data Validation": {
        "video_link": "https://youtu.be/4Q-aWCRouis",
        "share_drive_link": "https://arbrecreations-my.sharepoint.com/:b:/g/personal/abhishekm_arbre_in/EdjGz6Fn2ZtOvWUXB1_nmNQBZdYXYONhpuGp_YWhK0ItVA?e=ST7RfI",
        "notes_embed_code":"""<iframe loading="lazy" style="position: relative; width: 100%; height: 600px; max-height: 80vh; border: none; padding: 0; margin: 0; overflow: hidden;"
      src="https:&#x2F;&#x2F;www.canva.com&#x2F;design&#x2F;DAF9bFAd4wQ&#x2F;GJpB2Hxu2eyjRDlrsbdFLw&#x2F;view?embed" allowfullscreen="allowfullscreen" allow="fullscreen">
    </iframe>
    <a href="https:&#x2F;&#x2F;www.canva.com&#x2F;design&#x2F;DAF9bFAd4wQ&#x2F;GJpB2Hxu2eyjRDlrsbdFLw&#x2F;view?utm_content=DAF9bFAd4wQ&amp;utm_campaign=designshare&amp;utm_medium=embeds&amp;utm_source=link" target="_blank" rel="noopener">Data Validation</a> by Console Flare""",
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

 
    
    
    # Other topics follow...

}

# Function to display questions and get user answers
def display_questions(questions):
    score = 0
    for i, (question, options) in enumerate(questions.items()):
        st.subheader(question)
        user_answer = None  # Initialize user_answer variable
        if options["type"] == "multiselect":
            user_answers = st.multiselect("Select all correct answers", options["options"])
            if set(user_answers) == set(options["correct_answers"]):  # Check if the sets match
                st.success("Correct!")
                score += 1
            elif "Select" not in user_answers:  # Don't show incorrect if default is not selected
                st.error("Incorrect!")
        elif options["type"] == "radio":
            radio_key = f"{question}_radio_{i}"
            user_answer = st.radio("Select your answer", options["options"],key=radio_key)
            if user_answer == options["correct_answer"]:
                st.success("Correct!")
                score += 1
            elif user_answer != "Select":  # Don't show incorrect if default is not selected
                st.error("Incorrect!")
        elif options["type"] == "slider":
            user_answer = st.slider("Select a value", min_value=0, max_value=len(options["options"]) - 1, step=1)
            if options["options"][user_answer] == options["correct_answer"]:
                st.success("Correct!")
                score += 1
            elif user_answer != 0:  # Don't show incorrect if default is not selected
                st.error("Incorrect!")
        elif options["type"] == "dropdown":
            user_answer = st.selectbox("Select your answer", options["options"])
            if user_answer == options["correct_answer"]:
                st.success("Correct!")
                score += 1
            elif user_answer != "Select":  # Don't show incorrect if default is not selected
                st.error("Incorrect!")

        # Validate user's answer
        if user_answer is not None:
            st.write(f"Your answer: {user_answer}")
            if user_answer not in options["options"]:
                st.warning("Invalid answer! Please select a valid option.")

        # Hint box
        if "hint" in options:  # Check if hint is provided
            if st.checkbox(f"Need a hint?_{i}"):
                st.write(options["hint"])

    st.title(f"Your score: {score}/{len(questions)}")


# Main code
st.set_page_config(layout="wide")  # Optimize layout for mobile devices
st.title("Excel Learning App")

# Sidebar dropdown to select topics
selected_topic = st.sidebar.selectbox("Select Topic", list(topics_data.keys()))

# Display topic video
st.sidebar.video(topics_data[selected_topic]["video_link"])

# Display topic notes
st.sidebar.subheader("Notes")
notes_embed_code = topics_data[selected_topic]["notes_embed_code"]
st.sidebar.markdown(notes_embed_code, unsafe_allow_html=True)

# Display topic questions
st.sidebar.subheader("Questions")
display_questions(topics_data[selected_topic]["questions"])

