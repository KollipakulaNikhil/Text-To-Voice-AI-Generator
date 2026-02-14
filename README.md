# Text-To-Voice AI Generator

A simple **Text-to-Speech (TTS) web app** that converts user text input into spoken audio using AI voice synthesis.  
This tool demonstrates prompt building, UI interaction, and backend integration for voice generation.

---

## 🔊 Overview

This project provides:
- A **frontend UI** (`index.html`) for users to input text
- A **Python backend** (`main.py`) handling text input and generating speech
- AI text-to-voice capability using Python libraries

It is useful for:
- Learning TTS systems
- Prototyping voice interfaces
- Audio accessibility tools

---

## 🚀 Features

✅ Input text via web interface  
✅ Convert input text into audio speech  
✅ Play or download generated speech  
✅ Lightweight and easy to run locally

---

## 🧠 How It Works

1. User opens the web page (`index.html`)
2. Enters text into the input field
3. Submits request to the Python backend
4. Backend synthesizes voice from text
5. The generated audio is returned to the browser

*(The project uses common text-to-speech libraries — you can enhance it with more advanced TTS engines later.)*

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|------------|
| Frontend | HTML |
| Backend | Python |
| Speech Generation | Python TTS libraries |
| Deployment | Localhost / Simple server |

---

## 📦 Installation

1. **Clone the repository**
```bash
git clone https://github.com/KollipakulaNikhil/Text-To-Voice-AI-Generator.git
cd Text-To-Voice-AI-Generator
Create a Python virtual environment

python3 -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate      # Windows
Install dependencies

pip install -r requirements.txt
Run the application

python main.py
Open web UI
Open index.html in your browser (served via Python or locally)

📄 Usage
In the text box, type the sentence you want to convert to speech

Click “Generate”

The app will synthesize the audio and allow playback/download

💡 How to Improve This Project
Here are enhancement ideas you can implement next:

Integrate a modern AI TTS API (e.g., OpenAI, ElevenLabs, Coqui-TTS) for higher quality speech

Add support for multiple voices or languages

Deploy as a web service (e.g., Vercel, Render)

Add audio download functionality

Improve UI with frameworks like React or Vue

Current open-source TTS models and tools can generate more natural voices and support expressive speech synthesis. 

🧪 Testing
Use tools like Postman or browser DevTools to test API requests and audio responses.

📚 Resources
🐸 Coqui-TTS — a powerful open-source TTS library with many models 

Text-to-speech GitHub topic (list of community resources) 

📜 License
This project is open source — feel free to use or modify it.


---

### 💡 Why This README Is Strong

✔ Explains *what* the project does and *why*  
✔ Includes clear *installation and usage steps*  
✔ Lists *enhancement ideas* for future work  
✔ Shows that you understand TTS concepts

---

If you want, I can also **suggest improvements to your UI or backend code** to make the voice output more natural or support multiple voices — just ask!
::contentReference[oaicite:4]{index=4}
