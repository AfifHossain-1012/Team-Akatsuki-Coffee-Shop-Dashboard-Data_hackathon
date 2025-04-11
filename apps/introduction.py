import streamlit as st

def app():
    # Title and Vision
    st.title("Introduction")
    st.subheader("My Vision")
    st.write(
        """
        My vision is to transform raw sales data into meaningful insights that help the coffee shop make smarter, 
        data-driven decisions. I believe that data can not only improve operations but also enhance customer satisfaction, 
        loyalty, and profitability. Through this project, I aim to support informed decision-making by uncovering 
        actionable insights from data.
        """
    )

    # Personal Introduction Section
    st.subheader("About Me")
    st.write("Get to know the creator behind this dashboard:")

    # Display personal details
    col1, col2 = st.columns([1, 3])

    with col1:
        st.image("images/Afif Hossain Irfan.jpg", width=140, use_container_width=True, caption="Afif Hossain Irfan")

    with col2:
        st.markdown("### Afif Hossain Irfan")
        st.write("**Role**: Project Creator, Data Researcher, Analyst, Programmer, and Dashboard Designer")
        st.write(
            """
            I led this project independently, taking charge of data research, cleaning, analysis, and visualization. 
            I developed the interactive dashboard using Streamlit and focused on creating an intuitive interface that turns 
            complex data into clear and actionable insights. From data processing to user experience, I handled all aspects 
            of the project to ensure alignment with my vision of enabling data-driven decision making.
            """
        )
        st.write("**Key Skills**: Data Analysis, Python Programming, Streamlit, Visualization, UI Design, Strategic Planning")

    st.markdown("---")

    # Closing Statement
    st.subheader("My Commitment")
    st.write(
        """
        I combined my skills and passion for data to create a tool that uncovers hidden patterns, empowering the 
        coffee shop to make smarter decisions. This project reflects my dedication to blending technical expertise 
        with impactful storytelling. I'm excited about the possibilities this dashboard opens up. Now, let’s dive into the analysis!
        """
    )
