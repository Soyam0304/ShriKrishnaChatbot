# Shri Krishna Chatbot

A life guidance chatbot powered by the teachings of the Bhagavad Gita. This chatbot is designed to offer modern, simple, and thoughtful advice based on the wisdom of Shri Krishna. Users can ask life problems, and the chatbot will provide insightful responses inspired by the Bhagavad Gita.

## Features

- **Guidance Based on Bhagavad Gita**: The chatbot provides life guidance using the teachings of Shri Krishna.
- **User-Friendly Interface**: Simple and intuitive UI built with Streamlit.
- **Personalized Responses**: Get personalized responses to your life problems based on Krishna's wisdom.
- **Image Sidebar**: The sidebar includes an image of Shri Krishna along with some background information.
- **Real-Time Chat Interaction**: Instant responses to users' queries for quick problem-solving.
- **Thoughtful and Compassionate Responses**: The chatbot responds with compassion and understanding, providing practical life advice.
- **Streamlined Experience**: No complex navigation or steps; a single input and output for simplicity.
- **Responsive Design**: The interface is responsive and adapts well to various screen sizes.
- **Simple and Elegant Visuals**: The design focuses on a clean, minimalistic interface for a better user experience.
- **No External APIs**: The chatbot doesn’t rely on any external APIs for generating responses, making it independent and efficient.

## Tech Stack

- **Python**: The core programming language used for developing the chatbot.
- **Streamlit**: Used to build the interactive user interface.
- **Phi-Agent**: Used to integrate and generate responses from the chatbot model.
- **Groq**: Used as the underlying model for generating responses.
- **.env File**: Used to manage sensitive environment variables.

## Installation

Follow these steps to set up the project locally:

1. **Clone the repository**:

    ```bash
    git clone https://github.com/<your-username>/shri-krishna-chatbot.git
    ```

2. **Navigate to the project directory**:

    ```bash
    cd shri-krishna-chatbot
    ```

3. **Set up a virtual environment (optional but recommended)**:

    ```bash
    python -m venv venv
    source venv/bin/activate  # For macOS/Linux
    .\venv\Scripts\activate  # For Windows
    ```

4. **Install the required dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

5. **Create a `.env` file** and add any necessary environment variables. Example:

    ```text
    API_KEY=your-api-key-here
    ```

6. **Run the app**:

    ```bash
    streamlit run app.py
    ```

    The Streamlit app will open in your default web browser.
  
## Usage

- Open the Streamlit app in your browser.
- Type your life problem or question in the input box.
- Click "Get Guidance" to receive a response inspired by the Bhagavad Gita.
- The chatbot will display personalized guidance, helping you find clarity and peace.