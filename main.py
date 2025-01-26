import streamlit as st
from phi.agent import Agent
from phi.model.groq import Groq
from dotenv import load_dotenv
import io
import sys
import re

# Load environment variables
load_dotenv()

# Define Shri Krishna Chatbot Agent
krishna_agent = Agent(
    name="Shri Krishna Chatbot",
    model=Groq(id="llama-3.3-70b-versatile"),
    instructions=[
        "You are Shri Krishna, the divine teacher from the Bhagavad Gita.",
        "A user will share their life problems, and you will provide guidance based on the Bhagavad Gita.",
        "However, you will not give direct shlokas but will interpret the meaning in modern, simple words ",
        "while maintaining the essence of Krishna's wisdom.",
        "Your responses should be easy to understand , and give responses in simple words ",
        "Your responses should be thoughtful, compassionate, and practical, inspiring the user towards the right path.",
        "Please provide answers as simple paragraphs, without using tables, bullet points, or any special formatting.",
        "Avoid breaking the answer into sections or structured formats. It should be a continuous, natural response."
    ],
    show_tool_calls=False,
    markdown=True,
)

# Streamlit UI: Sidebar with info and image
st.sidebar.title("About Shri Krishna Chatbot")
st.sidebar.write("This chatbot provides life guidance based on the teachings of the Bhagavad Gita.")
st.sidebar.write("Ask questions, and Shri Krishna will help you find clarity and wisdom through his divine teachings.")
st.sidebar.image("D:/GenAi-Projects/RAG/e8aefd868653c7ce76ce512f8825042d.jpg", caption="Shri Krishna", use_container_width=True)

# Main title and prompt
st.title("Shri Krishna Chatbot")
st.write("Ask Shri Krishna for guidance on your life problems based on the Bhagavad Gita.")

user_input = st.text_area("What is troubling you?", "", height=140)
if st.button("Get Guidance"):
    if user_input:
        with st.spinner("Thinking..."):
            try:
                output_capture = io.StringIO()
                sys.stdout = output_capture
                krishna_agent.print_response(user_input, stream=True)
                sys.stdout = sys.__stdout__  # Reset stdout
                
                response = output_capture.getvalue()

                # Clean the response to remove unwanted formatting and box characters
                cleaned_response = re.sub(r'\x1b\[[0-9;]*m', '', response)  # Remove color codes
                cleaned_response = re.sub(r'━|┃|┛|┓|┏|┛', '', cleaned_response)
                cleaned_response = re.sub(r'^.*?(\n|$)', '', cleaned_response)  # Remove box characters

                # Display cleaned and formatted response
                st.write(cleaned_response.strip())  # Strip extra spaces at the beginning/end
            except Exception as e:
                st.error(f"An error occurred: {str(e)}")
    else:
        st.error("Please enter your problem to get guidance.")


