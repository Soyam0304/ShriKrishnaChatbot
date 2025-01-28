import streamlit as st
from phi.agent import Agent
from phi.model.groq import Groq
from dotenv import load_dotenv
import io
import sys
import re

# Load environment variables
load_dotenv()

# Custom CSS for styling
st.markdown("""
    <style>
        body {
            background-color: #f4f1de;
            color: #2d3436;
        }
        .stTextInput>div>div>input, .stTextArea>div>div>textarea {
            background-color: #fff !important;
            border-radius: 10px;
            padding: 15px !important;
        }
        .stButton>button {
            background-color: #0984e3 !important;
            color: white !important;
            border-radius: 10px;
            padding: 10px 25px;
            font-size: 18px !important;
            transition: all 0.3s;
        }
        .stButton>button:hover {
            transform: scale(1.05);
            background-color: #0767b1 !important;
        }
        .response-container {
            background-color: #ffffff;
            border-radius: 15px;
            padding: 25px;
            margin-top: 20px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            border-left: 5px solid #0984e3;
        }
        .sidebar .sidebar-content {
            background-color: #dfe6e9;
        }
        h1 {
            color: #2d3436 !important;
            font-family: 'Helvetica Neue', sans-serif;
        }
    </style>
""", unsafe_allow_html=True)

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
with st.sidebar:
    st.title("🕉️ Shri Krishna Chatbot")
    st.markdown("---")
    st.image("https://i.pinimg.com/736x/b3/28/4d/b3284dcb1700d9d41071ea3efb926c80.jpg", 
             caption="Shri Krishna", use_container_width=True)
    st.markdown("""
    <div style="padding: 15px; background-color: #ffffff; border-radius: 10px; margin-top: 20px;">
        <h4 style="color: #0984e3;">About</h4>
        <p style="font-size: 14px;">This divine chatbot provides life guidance based on the eternal wisdom of the Bhagavad Gita. Seek counsel from Lord Krishna himself.</p>
        <h4 style="color: #0984e3; margin-top: 15px;">How to Use</h4>
        <p style="font-size: 14px;">1. Share your concern or question<br>
        2. Click 'Get Divine Guidance'<br>
        3. Receive Krishna's wisdom</p>
    </div>
    """, unsafe_allow_html=True)

# Main interface
st.title("🕉️ Seek Guidance from Shri Krishna")
st.markdown("### 🌸 Share your concerns and receive divine wisdom from the Bhagavad Gita")

# Custom text input area
user_input = st.text_area(
    label="**What is on your mind, dear seeker?** 🙏",
    placeholder="Share your thoughts here...",
    height=150,
    help="Pour your heart out here. Krishna is listening..."
)

col1, col2 = st.columns([1, 0.2])
with col1:
    if st.button("**Get Divine Guidance 🌟**", use_container_width=True):
        if user_input:
            with st.spinner("🔮 Krishna is contemplating your query..."):
                try:
                    # Capture response
                    output_capture = io.StringIO()
                    sys.stdout = output_capture
                    krishna_agent.print_response(user_input, stream=True)
                    sys.stdout = sys.__stdout__
                    
                    # Process response
                    response = output_capture.getvalue()
                    cleaned_response = re.sub(r'\x1b\[[0-9;]*m', '', response)
                    cleaned_response = re.sub(r'[━┃┛┓┏┛]', '', cleaned_response)
                    cleaned_response = cleaned_response.strip()

                    # Display styled response
                    st.markdown(f"""
                    <div class="response-container">
                        <h4 style="color: #0984e3; margin-bottom: 15px;">Krishna's Wisdom 🌺</h4>
                        <div style="font-size: 16px; line-height: 1.6;">
                            {cleaned_response}
                        </div>
                    </div>
                    """, unsafe_allow_html=True)
                    
                except Exception as e:
                    st.error(f"An error occurred: {str(e)}")
        else:
            st.warning("Please share your concerns to receive guidance.")