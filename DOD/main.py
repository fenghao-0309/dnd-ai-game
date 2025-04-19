from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from game_engine import initialize_game, continue_game
import os

app = FastAPI()

# Allow CORS for frontend on localhost:3000
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Memory store (basic)
game_sessions = {}

class GameRequest(BaseModel):
    session_id: str
    message: str

@app.post("/start")
def start_game(req: GameRequest):
    session_id = req.session_id
    intro_text, character = initialize_game(session_id)
    game_sessions[session_id] = character
    return {"reply": intro_text}

@app.post("/play")
def play_game(req: GameRequest):
    character = game_sessions.get(req.session_id)
    if not character:
        return {"reply": "Session not found. Start a new game."}
    reply = continue_game(req.message, character)
    return {"reply": reply}
