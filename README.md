# Skinwise_Agentic_AI

Skinwise is an interactive multi-agent Agentic AI application powered by [PhiData](https://docs.phidata.com/), tailored to answer all your skincare queries using web crawling, Wikipedia, and search engine tools. It features a sleek React frontend and a Python Flask backend.


# Tech Stack
Frontend: React, Custom CSS

Backend: Flask (Python), Phidata, Groq

AI Agents: WikipediaTool, Crawl4aiTools, SerpAPI 

Model: LLaMA 3.3 70B via Groq API 

# Features

- 🔍 Classifies user queries: ingredients, product suggestions, routines, comparisons, etc.
  
- 📖 Fetches definitions from Wikipedia (via Phi’s `WikipediaTool`)

- 🌐 Crawls trusted sources using `Crawl4aiTools`

- 🤖 Built on the powerful `LLaMA 3.3 70B` model via `Groq`

- 🧠 Agentic task routing via a `Query Analyzer Agent`

- 💅 Clean React frontend with dynamic UI changes


## 📸 Preview

![Skinwise UI Preview]([path/to/screenshot.png](https://github.com/arjumand252/Skinwise_Agentic_AI/blob/main/Skinwise%20Agentic%20AI%20-%20Google%20Chrome%202025-06-22%2019-50-18.mp4%20(1).gif))

---

## 🛠️ Setup Instructions

### 1. Clone the Repo

git clone [https://github.com/your-username/skinwise.git](https://github.com/arjumand252/Skinwise_Agentic_AI.git)

cd skinwise

### 2. Backend Setup
```bash
cd backend
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 3. Create a .env file

```bash
GROQ_API_KEY=your-groq-key
SERPAPI_API_KEY=your-serpapi-key
```

### 4. Setup the Flask server

```bash
python app.py
```

### 5. Frontend Setup

```bash
cd ../skincare-agent-ui
npm install
npm start
```

## Folder Structure

```bash
skinwise/
│
├── backend/
│   ├── app.py
│   ├── agents.py
│   └── .env
│
├── skincare-agent-ui/
│   ├── public/
│   ├── src/
│   ├── App.js
│   ├── App.css
│   └── package.json
│
├── .gitignore
└── README.md
```
