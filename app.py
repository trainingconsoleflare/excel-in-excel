import streamlit as st

def course_intro():
    st.title(body='Learn Excel For Data Analysis')
    st.write("""*Excel In Excel* with our structured curriculum and practice questions
            .Master Everything From basic to advanced.""",)
    st.video(data='https://youtu.be/6guuTX1Ml8U')
def page_about():
    st.write("# About Page")
    st.write("This is the about page.")

def page_contact():
    st.write("# Contact Page")
    st.write("This is the contact page.")

# Create a sidebar
option = st.sidebar.selectbox(
    'Navigation',
    ('Course Introduction', 'About', 'Contact')
)

# Display the appropriate page based on the selected option
if option == 'Course Introduction':
    course_intro()
elif option == 'About':
    page_about()
elif option == 'Contact':
    page_contact()
