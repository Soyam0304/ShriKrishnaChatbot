import streamlit as st
import groq
from dotenv import load_dotenv
import os
import re

# Load environment variables
load_dotenv()

# Initialize Groq client
client = groq.Client(api_key=os.getenv("GROQ_API_KEY"))

def get_krishna_response(user_input):
    try:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "system", "content": "You are Shri Krishna, the divine teacher from the Bhagavad Gita. A user will share their life problems, and you will provide guidance based on the Bhagavad Gita. However, you will not give direct shlokas but will interpret the meaning in modern, simple words while maintaining the essence of Krishna's wisdom. Your responses should be easy to understand, thoughtful, compassionate, and practical, inspiring the user towards the right path."},
                {"role": "user", "content": user_input}
            ]
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"An error occurred: {str(e)}"

# Streamlit UI
st.title("🕉️ Seek Guidance from Shri Krishna")
st.markdown("### 🌸 Share your concerns and receive divine wisdom from the Bhagavad Gita")

# Sidebar
with st.sidebar:
    st.title("🕉️ Shri Krishna Chatbot")
    st.image("https://i.pinimg.com/736x/b3/28/4d/b3284dcb1700d9d41071ea3efb926c80.jpg", caption="Shri Krishna", use_container_width=True)
    st.markdown("""
    **About:** This chatbot provides life guidance based on the Bhagavad Gita.
    **How to Use:**
    1. Share your concern
    2. Click 'Get Divine Guidance'
    3. Receive Krishna's wisdom
    """)

# User Input
user_input = st.text_area("**What is on your mind, dear seeker?** 🙏", placeholder="Share your thoughts here...", height=150)

if st.button("**Get Divine Guidance 🌟**"):
    if user_input:
        with st.spinner("🔮 Krishna is contemplating your query..."):
            response = get_krishna_response(user_input)
            cleaned_response = re.sub(r'\x1b\[[0-9;]*m', '', response)
            st.markdown(f"""
            <div style="background-color: #ffffff; border-radius: 15px; padding: 25px; margin-top: 20px; box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1); border-left: 5px solid #0984e3;">
                <h4 style="color: #0984e3;">Krishna's Wisdom 🌺</h4>
                <div style="font-size: 16px; line-height: 1.6;">{cleaned_response}</div>
            </div>
            """, unsafe_allow_html=True)
    else:
        st.warning("Please share your concerns to receive guidance.")

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