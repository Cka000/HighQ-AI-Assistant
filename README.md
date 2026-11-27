# HighQ AI Assistant

An AI-powered institute enquiry chatbot built with **Streamlit**, **Groq API**, and **GPT-OSS 120B**. The chatbot answers institute-related queries using a structured JSON knowledge base while maintaining conversation history.

---

## Application Preview

![HighQ AI Assistant](assets/screenshot.png)

---

## Features

- AI-powered question answering
- Streaming AI responses
- Multi-chat conversation support
- Chat history management
- JSON-based knowledge base
- Responsive Streamlit UI
- Secure API key management using `.env`
- Customizable LLM model selection
- Customizable institution information through JSON

---

## Tech Stack

- **Programming Language:** Python
- **Frontend:** Streamlit
- **AI API:** Groq API
- **Default LLM:** GPT-OSS 120B
- **Knowledge Base:** JSON
- **Environment Management:** Python-dotenv

---

## Installation

Follow these steps to set up the project on your local machine.

**1. Clone the repository**

```bash
git clone https://github.com/Cka000/HighQ-AI-Assistant.git
```

**2. Navigate to the project directory**

```bash
cd HighQ-AI-Assistant
```

**3. Create a virtual environment (recommended)**

```bash
python -m venv venv
```

Activate the environment:

Windows:

```bash
venv\Scripts\activate
```

Mac/Linux:

```bash
source venv/bin/activate
```

**4. Install dependencies**

```bash
pip install -r requirements.txt
```

---

## API Key Configuration

This project uses the Groq API to generate AI-powered responses.

You need your own Groq API key to run the application.

**1. Get your Groq API key**

Visit [Groq Console](https://console.groq.com/keys) and generate an API key.

**2. Create a `.env` file**

The repository includes a `.env.example` file.

Copy `.env.example` and rename the copied file to `.env`.

**3. Add your API key**

Open the `.env` file and replace the placeholder with your actual Groq API key.

```env
GROQ_API_KEY=your_actual_groq_api_key
```

**Important:**
- Never share your API key publicly.
- Do not upload your `.env` file to GitHub.
- Keep your API credentials private.
- Each developer must configure their own API key.

---

## AI Model

By default, this project uses **GPT-OSS 120B** through the Groq API.

Default model ID:

```text
openai/gpt-oss-120b
```

The model generates responses based on the institute's structured JSON knowledge base.

---

## Customizing the AI Model (LLM)

You can change the default LLM and experiment with other models supported by Groq.

**Steps to change the model:**

1. Visit [Groq Console - Models](https://console.groq.com/docs/models).
2. Explore the available models.
3. Copy the model ID you want to use.
4. Open `main.py`.
5. Find the `client.chat.completions.create()` method.

```python
stream = client.chat.completions.create(
    model="openai/gpt-oss-120b",
    messages=messages,
    stream=True
)
```

6. Replace the existing model ID with your preferred model ID.

For example:

```python
model="your_preferred_model_id"
```

**Note:**
- Make sure the selected model is available on your Groq account.
- Check model compatibility with the API features used in this project.
- Changing to another LLM provider may require modifications to the API client, authentication, and application code.

---

## Customizing the Knowledge Base (data.json)

This chatbot uses a JSON file (`data.json`) as its knowledge base to answer institute-related questions.

You can customize the chatbot by adding your own institution's information to this file.

This means developers can adapt the chatbot for different educational institutions without having to rewrite the entire application.

### How to Add Your Institution Data

1. Open the `data.json` file in the project directory.
2. Add your institution's information in JSON format.
3. Include relevant details such as:
   - Institution name
   - Institution location
   - Courses offered
   - Admission process
   - Eligibility criteria
   - Fee structure
   - Placement information
   - Contact details
   - Other important institutional information
4. Save the changes.
5. Restart the application if required.

### Example JSON Structure

```json
{
    "institution": {
        "name": "ABC Institute",
        "location": "Bengaluru",
        "courses": [
            "Computer Science",
            "Information Science",
            "Electronics"
        ],
        "admission": {
            "process": "Entrance examination and counselling",
            "eligibility": "10+2 with relevant subjects"
        },
        "placements": {
            "average_package": "6 LPA",
            "highest_package": "18 LPA"
        },
        "contact": {
            "email": "info@example.com",
            "phone": "9876543210"
        }
    }
}
```

*The above JSON is only an example. Replace it with information about your own institution.*

**Important:**
- Maintain valid JSON syntax.
- Use double quotes for keys and string values.
- Do not add trailing commas.
- Keep the information accurate and up to date.
- Follow the existing JSON structure expected by `main.py` when modifying the knowledge base.

By updating `data.json`, you can provide institution-specific information and customize the chatbot according to your requirements.

---

## Run the Application

After configuring your API key and institution data, execute:

```bash
streamlit run main.py
```

The application will automatically open in your default browser.

---

## Project Structure

```text
HighQ-AI-Assistant/
│
├── .streamlit/
│
├── assets/
│   └── screenshot.png
│
├── .env.example
├── .gitignore
├── README.md
├── data.json
├── main.py
└── requirements.txt
```

---

## Security

- API keys are stored in environment variables.
- The `.env` file should be excluded from Git tracking.
- Never commit private credentials or API keys to the repository.

---

## Future Improvements

- Support for additional LLM providers
- Improved knowledge base management
- Enhanced chatbot interface
- More advanced conversation management

---

## Author

**Cka000**

GitHub: https://github.com/Cka000

---

If you find this project useful, consider giving the repository a ⭐ on GitHub!
