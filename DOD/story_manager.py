from openai import OpenAI
from utils import get_openai_api_key
client = OpenAI(api_key=get_openai_api_key())

class StoryManager:
    def __init__(self, character):
        self.character = character
        self.history = []

    def generate_prompt(self, user_input):
        prompt = f"""
        You are the Dungeon Master guiding the player through the adventure.
        Player Character: {self.character.name}, Role: {self.character.role}
        Attributes: {self.character.attributes}
        Skills: {self.character.skills}
        History: {self.history}
        Player says: {user_input}
        """
        return prompt

    def get_response(self, user_input):
        prompt = self.generate_prompt(user_input)
        response = client.chat.completions.create(model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a creative and adaptive Dungeon Master."},
            {"role": "user", "content": prompt}
        ])
        message = response.choices[0].message.content
        self.history.append({"player": user_input, "dm": message})
        return message
