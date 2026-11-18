# HighQ AI Assistant

An AI-powered institute enquiry chatbot built with **Streamlit**, **Groq API**, and **Llama 3.3**. The chatbot answers institute-related queries using a structured JSON knowledge base while maintaining conversation history.

---

## Application Preview

![HighQ AI Assistant](assets/screenshot.png)

---

## Features

- AI-powered question answering
- Streaming responses
- Multi-chat conversation support
- Chat history management
- JSON-based knowledge base
- Responsive Streamlit UI
- Secure API key management using `.env`

---

## Tech Stack

- Python
- Streamlit
- Groq API
- Llama 3.3
- JSON
- Python-dotenv

---

## Installation

**1. Clone the repository**

```bash
git clone https://github.com/Cka000/HighQ-AI-Assistant.git
```

**2. Navigate to the project directory**

```bash
cd HighQ-AI-Assistant
```

**3. Install dependencies**

```bash
pip install -r requirements.txt
```

---

## API Key Configuration

This project uses the Groq API to generate AI-powered responses.

You need to configure your own Groq API key before running the application.

**1. Get your Groq API key**

Visit [Groq Console](https://console.groq.com/keys) and generate your API key.

**2. Create a `.env` file**

The repository includes a `.env.example` file.

Copy `.env.example` and rename the copied file to `.env`.

**3. Add your API key**

Open the `.env` file and replace the placeholder with your actual Groq API key:

```env
GROQ_API_KEY=your_actual_groq_api_key
```

**Important:**
- Never share your API key publicly.
- Do not upload your `.env` file to GitHub.
- The `.env` file is intended to store your private API credentials.

---

## Run the Application

After configuring your API key, start the Streamlit application:

```bash
streamlit run main.py
```

The application will open in your browser.

---

## Project Structure

```text
HighQ-AI-Assistant/
│
├── .streamlit/
├── assets/
├── .env.example
├── .gitignore
├── README.md
├── data.json
├── main.py
└── requirements.txt
```
