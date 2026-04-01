# Multi-LLM-Rating-Platform

A FastAPI-based web application that allows users to compare and rate responses from multiple LLM providers.

Users can ask the same query to different models, evaluate their responses, and contribute to real-time leaderboards based on community ratings.

---

## 🚀 Live Demo

https://llm-evaluator-fastapi.onrender.com/

---

## ✨ Features

* Multi-LLM chat interface (Gemini, Mistral, Groq, OpenRouter)
* User-driven rating system (0–10 scoring)
* Real-time leaderboards (24h & 7d)
* Secure authentication (JWT + HTTP-only cookies)
* Model-specific conversation memory
* FAQ-grounded chatbot responses

---

## 📸 Screenshots

### Homepage

![Homepage](https://github.com/user-attachments/assets/f692cc99-cf2e-4389-9284-10b5d10c05d5)

### Chat Page

![Chat Page](https://github.com/user-attachments/assets/4f4103d0-4ba3-4bd5-a21c-ccddb9e3b397)

### User Dashboard

![User Dashboard](https://github.com/user-attachments/assets/bb2707ce-d069-4fc6-8781-fc94506ec794)

---

## 🧠 How It Works

### Chat System

* FAQ data is loaded from a CSV file and injected into prompts
* Models respond strictly within provided context
* Fallback response if answer is not found
* Session-based conversation memory per model

---

### Rating & Leaderboards

* Users compare responses across models
* Rate each response from 0–10
* Ratings stored in PostgreSQL with timestamp
* Leaderboards generated for:

  * Last 24 hours
  * Last 7 days

---

### Authentication

* User registration & login (email/username)
* Password hashing (bcrypt)
* JWT-based auth with HTTP-only cookies
* Protected routes with backend validation

---

## 🛠 Tech Stack

**Backend**

* FastAPI (async)
* PostgreSQL
* SQLAlchemy (async ORM)

**Frontend**

* Jinja2
* HTML / CSS / JavaScript

**Authentication**

* JWT (HS256)
* HTTP-only cookies

**LLM Providers**

* Groq
* Google Gemini
* Mistral
* OpenRouter

---

## ⚙️ Setup

```bash
pip install -r requirements.txt
```

Create `.env`:

```env
GROQ_API_KEY=your_groq_api_key
MISTRAL_API_KEY=your_mistral_api_key
GEMINI_API_KEY=your_gemini_api_key
OPEN_ROUTER_API_KEY=your_openrouter_api_key
DATABASE_URL=your_database_url
SECRET_KEY=your_secret_key
```

Run:

```bash
python main.py
```

---

## 📌 Notes

* Uses user-driven ratings for benchmarking (not automated evaluation)
* API keys managed via environment variables
* Sessions expire based on JWT tokens
