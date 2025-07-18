# Skinwise_Agentic_AI

Skinwise is an interactive multi-agent Agentic AI application powered by [PhiData](https://docs.phidata.com/), tailored to answer all your skincare queries using web crawling, Wikipedia, and search engine tools. It features a sleek React frontend and a Python Flask backend.


## Tech Stack
Frontend: React, Custom CSS

Backend: Flask (Python), Phidata, Groq

AI Agents: WikipediaTool, Crawl4aiTools, SerpAPI, Firecrawl

Model: LLaMA 3.3 70B via Groq API 

## Features

- 🔍 Classifies user queries: ingredients, product suggestions, routines, comparisons, etc.
  
- 📖 Fetches definitions from Wikipedia (via Phi’s `WikipediaTool`)

- 🌐 Crawls trusted sources using `Crawl4aiTools`

- 🛍️ Crawls popular E-commerce sites to search for the best skincare products using `Firecrawl`.

- 🤖 Built on the powerful `LLaMA 3.3 70B` model via `Groq`

- 🧠 Agentic task routing via a `Query Analyzer Agent`

- 💅 Clean React frontend with dynamic UI changes

## Query Processing

### High Level Design

![Query Processing2](flowchart2.png)


### Low Level Design

![Query processing](flowchart.png)


## 📸 Preview

Ask any skincare-related query:

![Skinwise UI Preview 1](skincare_3.png)

Get instant, coherent responses:

![Skinwise UI Preview 2](skinwise_1.gif)

Ask for skincare product recommendations: 

![Skinwise UI Preview 3](skincare_5.png)

<!-- 
![Skinwise UI Preview](skinwise_2.gif) -->

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
