# 💼 LinkedIn Post Generator

An AI-powered tool that generates professional LinkedIn posts using **LLM (Large Language Model)** with **few-shot learning**. Select a topic, language, and length — get a polished, ready-to-publish LinkedIn post in seconds.

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://linkedinpostgenerator-saikat.streamlit.app/)
[![Python 3.11+](https://img.shields.io/badge/Python-3.11%2B-3776AB?logo=python&logoColor=white)](https://python.org)
[![LangChain](https://img.shields.io/badge/LangChain-Framework-1C3C3C?logo=chainlink)](https://langchain.com)
[![Groq](https://img.shields.io/badge/Groq-LLM%20API-F55036)](https://groq.com)

---

## ✨ Features

| Feature | Description |
|---|---|
| 🤖 **AI-Powered Generation** | Uses Groq's blazing-fast LLM inference for real-time post creation |
| 📚 **Few-Shot Learning** | Learns from curated LinkedIn post examples to match authentic writing styles |
| 🌐 **Multi-Language** | Supports **English** and **Hinglish** (Hindi + English) output |
| 📏 **Length Control** | Choose between Short (1–5 lines), Medium (6–10 lines), or Long (11–15 lines) |
| 🏷️ **Topic Tags** | Auto-extracted and unified topics from real LinkedIn posts |
| 📥 **Download** | One-click download of generated posts as `.txt` files |

---

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────┐
│                  Streamlit UI (main.py)              │
│         Topic | Language | Length → Generate         │
└───────────────────┬─────────────────────────────────┘
                    │
                    ▼
┌─────────────────────────────────────────────────────┐
│            Post Generator (post_generator.py)        │
│   Builds dynamic prompt + injects few-shot examples  │
└───────────────────┬─────────────────────────────────┘
                    │
          ┌─────────┴──────────┐
          ▼                    ▼
┌──────────────────┐  ┌────────────────────┐
│  Few-Shot Engine │  │   Groq LLM API     │
│  (fewshot.py)    │  │   (model.py)       │
│                  │  │                    │
│  Filters posts   │  │  LangChain +       │
│  by tag/lang/len │  │  ChatGroq          │
└────────┬─────────┘  └────────────────────┘
         │
         ▼
┌──────────────────────────────────────────────────────┐
│          Data Pipeline (preprocess.py)                │
│  raw_data.json → LLM metadata extraction →           │
│  tag unification → processed_post.json               │
└──────────────────────────────────────────────────────┘
```

---

## 🚀 Quick Start

### Prerequisites

- Python 3.11 or higher
- A free [Groq API key](https://console.groq.com/keys)

### 1. Clone the Repository

```bash
git clone https://github.com/<your-username>/linkedin-post-generator.git
cd linkedin-post-generator
```

### 2. Create Virtual Environment

```bash
python -m venv .venv

# Windows
.venv\Scripts\activate

# macOS / Linux
source .venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment

```bash
cp .env.example .env
```

Open `.env` and paste your Groq API key:

```
GROQ_API_KEY=gsk_your_actual_key_here
```

### 5. Run the App

```bash
streamlit run main.py
```

The app will open at `http://localhost:8501` 🎉

---

## ☁️ Deploy to Streamlit Cloud

1. **Push** this repo to GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Connect your GitHub repo
4. Set **Main file path** to `main.py`
5. In **Advanced settings → Secrets**, add:
   ```toml
   GROQ_API_KEY = "gsk_your_actual_key_here"
   ```
6. Click **Deploy** — your app is live!

---

## 📁 Project Structure

```
linkedin-post-generator/
├── main.py                 # Streamlit app entry point & UI
├── model.py                # LLM initialization (Groq + LangChain)
├── post_generator.py       # Prompt engineering & post generation
├── fewshot.py              # Few-shot example retrieval engine
├── preprocess.py           # Data pipeline: raw → enriched posts
├── data/
│   ├── raw_data.json       # Original scraped LinkedIn posts
│   └── processed_post.json # Enriched posts with metadata & unified tags
├── .streamlit/
│   └── config.toml         # Streamlit theme configuration
├── requirements.txt        # Python dependencies
├── .env.example            # Environment variable template
├── .gitignore              # Git ignore rules
└── README.md               # You are here
```

---

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| **[Streamlit](https://streamlit.io)** | Web UI framework for rapid prototyping |
| **[LangChain](https://langchain.com)** | LLM orchestration, prompt templates, output parsing |
| **[Groq API](https://groq.com)** | Ultra-fast LLM inference (OpenAI-compatible) |
| **[Pandas](https://pandas.pydata.org)** | Data manipulation for few-shot example filtering |
| **Python 3.11** | Core language |

---

## 💡 How It Works

1. **Data Preprocessing** (`preprocess.py`):  
   Raw LinkedIn posts are analyzed by the LLM to extract metadata — line count, language (English/Hinglish), and topic tags. Similar tags are then unified using LLM-powered semantic merging.

2. **Few-Shot Retrieval** (`fewshot.py`):  
   When a user selects a topic, language, and length, the engine filters the processed dataset to find matching example posts that serve as style references.

3. **Prompt Engineering** (`post_generator.py`):  
   A dynamic prompt is constructed with the user's preferences + up to 2 few-shot examples, then sent to the Groq LLM.

4. **Generation** (`model.py`):  
   The Groq-hosted LLM generates a LinkedIn post that matches the style, tone, and format of real high-engagement posts.

---

## 📜 License

This project is open source and available under the [MIT License](LICENSE).

---

<p align="center">
  Built by <strong>Saikat</strong> | 
  <a href="https://www.linkedin.com/in/">LinkedIn</a> · 
  <a href="https://github.com/">GitHub</a>
</p>
