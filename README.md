# 🐉 DnD-AI: An Interactive, AI-Powered Text Adventure Game

**DnD-AI** is a full-stack application that merges the immersive storytelling of Dungeons & Dragons with the power of Large Language Models. The project allows users to play dynamic, branching narrative games — powered by an AI Dungeon Master — all within a secure, personalized user experience.

---

## 🎯 Problem Statement

Traditional text-based RPGs like Dungeons & Dragons are incredibly fun and engaging — but they often require a real human Dungeon Master to guide the game and tailor the story. What if AI could take that role? And what if we could make it web-based, interactive, persistent, and personalized?

---

## 🚀 What This Project Does

### ✅ Core Features

- ✨ **AI Dungeon Master**: Uses OpenAI’s LLMs to dynamically narrate, adapt, and respond to your choices.
- 👤 **Supabase Auth Integration**: Users can sign up, log in, and return to their personalized game sessions.
- 🧠 **Character Customization**: Story templates define attributes, roles, skills, and scenarios.
- 🔁 **Interactive Text Loop**: Players input commands; AI responds and drives the story forward.
- 💾 **Session Management**: Each user’s game is isolated and tracked through session IDs.
- 🖥️ **Modern Web Frontend**: Built with Next.js 15, TailwindCSS, and custom Shadcn-style UI.
- 🔗 **FastAPI Backend**: Game logic and AI calls are served via a Python API, keeping things modular and scalable.

---

## 🏗️ Tech Stack

| Layer       | Tech                        |
|-------------|-----------------------------|
| Frontend    | Next.js 15 + Tailwind CSS   |
| Auth        | Supabase                    |
| Backend     | FastAPI (Python)            |
| AI Engine   | OpenAI API (GPT)            |
| UI Toolkit  | Shadcn-style components     |

---

## 🧑‍💻 How to Set Up Locally

### 1. Clone the repo

```bash
git clone https://github.com/your-username/dnd-ai-game.git
cd dnd-ai-game
```

### 2. Install frontend dependencies

```bash
npm install
```

### 3. Create `.env.local` for frontend

Create this file in the root:

```env
NEXT_PUBLIC_SUPABASE_URL=your_supabase_url
NEXT_PUBLIC_SUPABASE_ANON_KEY=your_anon_key
```

> Get these from [Supabase → Project → Settings → API](https://app.supabase.com)

### 4. Set up Python backend

Install dependencies in a virtual environment:

```bash
cd DOD
pip install fastapi uvicorn openai python-dotenv
```

Create a `.env` file:

```env
OPENAI_API_KEY=your_openai_key_here
```

### 5. Run the backend server

```bash
cd DOD
uvicorn main:app --reload --port 8000
```

### 6. Run the frontend server

```bash
npm run dev
```

Go to: [http://localhost:3000](http://localhost:3000)

---

## 🎮 How to Play

1. **Log in or sign up** using your email.
2. Once logged in, you will be placed into the game interface.
3. The AI will begin the story (e.g., "You are a National Security Advisor in the White House...").
4. Type what your character does, says, or thinks. For example:

   ```
   I walk into the war room and demand an update on the situation.
   ```

5. The AI Dungeon Master will respond and advance the narrative.
6. You can continue issuing commands and seeing the story evolve in real-time!

---

## 📁 Project Structure

```
dnd-ai-game/
├── DOD/                  # Python backend (FastAPI, AI logic, templates)
│   ├── main.py
│   ├── game_engine.py
│   ├── story_manager.py
│   └── templates/
├── app/                  # Next.js 15 App Router frontend
│   ├── page.tsx
│   └── api/game/route.ts
├── components/           # React components
│   ├── AuthForm.tsx
│   ├── ProtectedGame.tsx
│   ├── DnDGameUI.tsx
│   └── ui/               # Manually added Shadcn-style components
├── lib/
│   └── supabase.ts
├── styles/
│   └── globals.css
├── .env.local
├── package.json
└── README.md
```

---

## 🔐 Security Notes

- API keys are **never hardcoded**.
- OpenAI key is loaded securely from `.env` in the backend.
- Supabase keys are loaded only in the frontend from `.env.local`.

---

## 🧠 Future Ideas

- Save/load game progress using Supabase database
- Add inventory, quest logs, or relationship maps
- Enable multiplayer scenarios
- Add voice input or AI-generated art for scenes

---

## ✨ Credits

- Designed and built by [Your Name]
- Inspired by D&D, powered by OpenAI and Supabase
