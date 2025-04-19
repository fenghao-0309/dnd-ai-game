import os
import json
from character import Character
from story_manager import StoryManager

import os

def list_templates():
    templates_dir = os.path.join(os.path.dirname(__file__), "templates")
    return [f for f in os.listdir(templates_dir) if f.endswith(".json")]

def start_game():
    # Step 1: Let user choose a game scenario
    templates = list_templates()
    print("Choose a game to play:")
    for idx, file in enumerate(templates, 1):
        print(f"{idx}. {file.replace('.json', '')}")
    file_idx = int(input("Enter the number of your choice: ")) - 1
    selected_template = templates[file_idx]

    template_path = os.path.join(os.path.dirname(__file__), "templates", selected_template)
    with open(template_path, "r") as f:
        template = json.load(f)

    scenario = template.get("Dnd-Scenario", "Unknown Scenario")
    print(f"\nYou have selected: {scenario}")

    customizations = template["playerCustomizations"]
    attributes_template = template["attributes"]
    skills_template = template["baseSkills"]

    # Step 2: Character setup
    name = input("Enter your character's name: ")

    # Helper for role/background selection
    def choose_from_customization(label, data):
        if isinstance(data, dict):
            print(f"\nChoose your {label}:")
            print(f"Note: {data.get('description', '')}")
            content = data.get("content", {})
            options = list(content.keys())
            for idx, opt in enumerate(options, 1):
                print(f"{idx}. {opt} - {content[opt].get('description', '')}")
            choice = int(input("Enter the number of your choice: ")) - 1
            selection = options[choice]
            bonus = content[selection].get("attributeBonus", {})
        else:
            options = data
            for idx, opt in enumerate(options, 1):
                print(f"{idx}. {opt}")
            choice = int(input("Enter the number of your choice: ")) - 1
            selection = options[choice]
            bonus = {}
        return selection, bonus

    # Role selection
    role, role_bonus = choose_from_customization("role", customizations.get("role", []))

    # Background selection
    background, background_bonus = choose_from_customization("background", customizations.get("background", []))

    # Step 3: Attribute point distribution
    print("\nDistribute 10 points among the following attributes:")
    attributes = {}
    remaining = 10
    for attr, desc in attributes_template.items():
        while True:
            print(f"{attr}: {desc}")
            points = int(input(f"Assign points to {attr} (remaining {remaining}): "))
            if 0 <= points <= remaining:
                attributes[attr] = points
                remaining -= points
                break
            else:
                print("Invalid input. Try again.")

    # Step 4: Apply bonuses
    print("\nApplying role and background bonuses:")
    for source, bonus_dict in [("Role", role_bonus), ("Background", background_bonus)]:
        for attr, bonus in bonus_dict.items():
            attributes[attr] = attributes.get(attr, 0) + bonus
            print(f"{source} Bonus → +{bonus} to {attr}")

    # Step 5: Show base skills
    print("\nHere are your available actions (baseSkills):")
    for skill, desc in skills_template.items():
        print(f"- {skill}: {desc}")

    # Step 6: Initialize skills with minimal base values
    skills = {skill: 1 for skill in skills_template}

    # Step 7: Start the story
    player = Character(name, f"{role}, {background}", attributes, skills)
    story = StoryManager(player)

    print(f"\n🎮 Game Start: {scenario}! Type 'exit' to quit.\n")
    while True:
        user_input = input("Your action: ")
        if user_input.lower() == "exit":
            print("Thanks for playing!")
            break
        response = story.get_response(user_input)
        print(f"\n{response}\n")
