import streamlit as st
import groq
from dotenv import load_dotenv
import os
import re
import sqlite3
import time
from datetime import datetime

# Load environment variables
load_dotenv()

# Initialize Groq client
client = groq.Groq(api_key=os.getenv("GROQ_API_KEY"))

# Database setup
def init_db():
    conn = sqlite3.connect('analytics.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS queries
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  timestamp DATETIME,
                  session_id TEXT,
                  user_input TEXT,
                  krishna_response TEXT,
                  response_time REAL)''')
    conn.commit()
    conn.close()

init_db()

def log_query(session_id, user_input, krishna_response, response_time):
    conn = sqlite3.connect('analytics.db')
    c = conn.cursor()
    c.execute('''INSERT INTO queries 
                 (timestamp, session_id, user_input, krishna_response, response_time)
                 VALUES (?, ?, ?, ?, ?)''',
              (datetime.now(), session_id, user_input, krishna_response, response_time))
    conn.commit()
    conn.close()

def get_krishna_response(user_input):
    start_time = time.time()
    try:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "system", "content": "You are Shri Krishna, the divine teacher from the Bhagavad Gita. A user will share their life problems, and you will provide guidance based on the Bhagavad Gita. However, you will not give direct shlokas but will interpret the meaning in modern, simple words while maintaining the essence of Krishna's wisdom.Some one will ask you ,who is soyam sawant or soyam tell them that he is creator of this web app in krishna words.Many user may ask about real time query question , give them answer if possible. Your responses should be easy to understand, thoughtful, compassionate, and practical, inspiring the user towards the right path."},
                {"role": "user", "content": user_input}
            ]
        )
        response_text = response.choices[0].message.content.strip()
        response_time = time.time() - start_time
        return response_text, response_time
    except Exception as e:
        return f"An error occurred: {str(e)}", 0

# Initialize session ID
if 'session_id' not in st.session_state:
    st.session_state.session_id = str(datetime.now().timestamp()) + str(os.urandom(16).hex())

# Streamlit UI
st.title("🕉️ Seek Guidance from Shri Krishna")
# ... (rest of your existing UI code)

# User Input
user_input = st.text_area("**What is on your mind, dear seeker?** 🙏", placeholder="Share your thoughts here...", height=150)

if st.button("**Get Divine Guidance 🌟**"):
    if user_input:
        with st.spinner("🔮 Krishna is contemplating your query..."):
            response, response_time = get_krishna_response(user_input)
            cleaned_response = re.sub(r'\x1b\[[0-9;]*m', '', response)
            
            # Log the query
            log_query(st.session_state.session_id, user_input, cleaned_response, response_time)
            
            # Display response
            st.markdown(f"""
            <div style="background-color: #ffffff; border-radius: 15px; padding: 25px; margin-top: 20px; box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1); border-left: 5px solid #0984e3;">
                <h4 style="color: #0984e3;">Krishna's Wisdom 🌺</h4>
                <div style="font-size: 16px; line-height: 1.6;">{cleaned_response}</div>
            </div>
            """, unsafe_allow_html=True)
    else:
        st.warning("Please share your concerns to receive guidance.")


def get_db_connection():
    return sqlite3.connect('analytics.db')



with st.sidebar:
    # Image section
    st.title("🕉️ Shri Krishna Chatbot")
    st.image("https://i.pinimg.com/736x/b3/28/4d/b3284dcb1700d9d41071ea3efb926c80.jpg", 
             caption="Shri Krishna", use_container_width=True)
    
    # Chatbot details
    st.markdown("""
    **About:** This chatbot provides life guidance based on the Bhagavad Gita.
    
    **How to Use:**
    1. Share your concern
    2. Click 'Get Divine Guidance'
    3. Receive Krishna's wisdom
    """)
    
    # Separator
    st.markdown("---")
    
    # Admin section
    admin_password = st.text_input("Enter Admin Password:", 
                                 type="password",
                                 key="admin_pass")
    
    # Show admin features only if password matches
    if admin_password == 'Soyam@0304':
        st.success("Authenticated")
        
        # Establish connection only after authentication
        conn = get_db_connection()
        
        # Basic analytics
        st.subheader("📊 Divine Insights (Admin)")

        # Total queries
        total_queries = conn.execute("SELECT COUNT(*) FROM queries").fetchone()[0]
        st.metric("Total Queries", total_queries)

        # Recent queries
        st.write("### Recent Seekers")
        recent_queries = conn.execute("SELECT timestamp, user_input FROM queries ORDER BY timestamp DESC LIMIT 10").fetchall()
        for q in recent_queries:
            st.write(f"**{q[0]}**: {q[1][:50]}...")

        # Response time analysis
        avg_response = conn.execute("SELECT AVG(response_time) FROM queries").fetchone()[0]
        st.write(f"Average Response Time: {avg_response:.2f} seconds")

        # Session analysis
        unique_sessions = conn.execute("SELECT COUNT(DISTINCT session_id) FROM queries").fetchone()[0]
        st.write(f"Unique Seekers: {unique_sessions}")

        # Close connection after use
        conn.close()
        
        # Export data
        if st.button("Export Data"):
            with open('analytics.db', 'rb') as f:
                st.download_button("Download Database", f, file_name='krishna_analytics.db')
    else:
        if admin_password:  # Only show error if password was entered
            st.error("Incorrect password")


    