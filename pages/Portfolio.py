import streamlit as st
import info
import pandas as pd

#About Me
def about_me_section():
    st.header("About Me")
    st.image(info.profile_picture, width = 200)
    st.write(info.about_me)
    st.write("---")
about_me_section()

#Sidebar Links
def links_section():
    st.sidebar.header("Links")
    st.sidebar.text("Connect with me on Linkedin")
    linkedin_link = f'<a href="{info.my_linkedin_url}"><img src="{info.linkedin_image_url}" alt="LinkedIn" width = "75" height = "75"></a>'
    # v: in order to generate a hyperlinked, html needed using following function (first input is the variable that genereates the link
    st.sidebar.markdown(linkedin_link, unsafe_allow_html=True)
    st.sidebar.text("Check out my work!")
    instagram_link = f'<a href="{info.my_instagram_url}"><img src="{info.instagram_image_url}" alt="Instagram" width = "65" height = "65"></a>'
    st.sidebar.markdown(instagram_link, unsafe_allow_html=True)
    st.sidebar.text("Or email me!")
    email_html = f'<a href="{info.my_email_address}"><img src="{info.email_image_url}" alt="Email" width = "75" height = "75"></a>'
    st.sidebar.markdown(email_html, unsafe_allow_html=True)
links_section()

#Education
def education_section(education_data, course_data):
    st.header("Education")
    st.subheader(f"**{education_data['Institution']}**")
    st.write(f"**Degree:** {education_data['Degree']}")
    st.write(f"**Graduation Date:** {education_data['Graduation Date']}")
    st.write(f"**GPA:** {education_data['GPA']}")
    coursework = pd.DataFrame(course_data)
    st.dataframe(coursework, column_config={
        "code": "Course Code",
        "names": "Course Names",
        "semester_taken": "Semester Taken",
        "skills": "What I Learned"},
                 #this assigns all the information in the list in course_data and assigns them to columns
        hide_index = True,
            #hide_index shows the ranking/order of the rows defined by teh columns
        )
    st.write("---")
    
education_section(info.education_data, info.course_data)

#Professional Experience
def experience_section(experience_data):
    st.header("Professional Experience")
    for job_title,(job_description, image) in experience_data.items():
        #an expander creaed an expandable dropdown menu
        expander = st.expander(f"{job_title}")
        expander.image(image, width = 250)
        for bullet in job_description:
            expander.write(bullet)
    st.write("---")

experience_section(info.experience_data)

#Projects
def project_section(projects_data):
    st.header("Projects")
    #calling the two parts in the loop splits the defined projects_data where it is divided by the comma
    for project_name, project_description in projects_data.items():
        expander = st.expander(f"{project_name}")
        expander.write(project_description)
    st.write("---")
    
project_section(info.projects_data)


#skills
def skills_section(software_data, spoken_data):
    st.header("Skills")
    st.subheader("Software/Languages")
    for skill, percentage in software_data.items():
        st.write(f"{skill} {info.software_icons.get(skill)}")
        st.progress(percentage)
    st.subheader("Spoken Languages")
    for spoken, proficiency in spoken_data.items():
        st.write(f"{spoken} {info.spoken_icons.get(spoken)}: {proficiency}")
    st.write("---")
    
skills_section(info.software_data, info.spoken_data)


#activities
def activities_section(leadership_data, activity_data):
    st.header("Activities")
    #tab function in streamlit allows an openable tab that contains sub information
    tab1, tab2 = st.tabs(["Leadership", "Community Service"])
    #the with function will now only add the informaton in tab 1
    with tab1:
        st.subheader("Leadership")
        for title, (details, image) in leadership_data.items():
            expander = st.expander(f"{title}")
            expander.image(image, width = 250)
            for bullet in details:
                expander.write(bullet)
    with tab2:
        st.subheader("Community Service")
        for title, details in activity_data.items():
            expander = st.expander(f"{title}")
            for bullets in details:
                expander.write(bullets)

    st.write("---")
activities_section(info.leadership_data, info.activity_data)
    




    
