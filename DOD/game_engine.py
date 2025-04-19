import json
import os
from character import Character
from story_manager import StoryManager

TEMPLATES_DIR = os.path.join(os.path.dirname(__file__), "templates")

# Global story managers per session
active_stories = {}

def initialize_game(session_id: str):
    """
    Initializes a game with default setup and returns the opening narrative.
    """
    default_template = "White_House_Chaos.json"
    with open(os.path.join(TEMPLATES_DIR, default_template), "r") as f:
        template = json.load(f)

    # Use default values for testing (can customize per-user later)
    attributes = {key: 2 for key in template["attributes"]}
    skills = {key: 1 for key in template["baseSkills"]}

    # Hardcoded character customization (for MVP)
    name = "Ron Vara"
    role = "National Security Advisor"
    background = "Political Operative"

    player = Character(name, f"{role}, {background}", attributes, skills)
    story = StoryManager(player)

    active_stories[session_id] = story
    intro = f"🎲 Welcome {name} the {role}!\nYour mission begins...\n\n"
    return intro + story.get_response(""), player


def continue_game(user_input: str, character: Character):
    """
    Sends player input to the existing story manager and returns response.
    """
    # Find story linked to character
    for sid, sm in active_stories.items():
        if sm.player == character:
            return sm.get_response(user_input)
    return "No active story found for this character."
