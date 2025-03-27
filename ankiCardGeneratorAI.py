import openai
import requests
import json

# OpenAI API Key (Replace with your own)
OPENAI_API_KEY = "your-openai-api-key"

# AnkiConnect API Endpoint
ANKI_CONNECT_URL = "http://localhost:8765"

# Your Anki Deck & Note Type
DECK_NAME = "AZ-400 Study Notes"
NOTE_TYPE = "Basic"

def summarize_text(text, model="gpt-4", max_sentences=3):
    """Summarizes the input text using OpenAI's GPT API."""
    prompt = f"""
    Summarize the following study material into {max_sentences} concise key points for review:
    
    {text}
    """
    
    response = openai.ChatCompletion.create(
        model=model,
        messages=[{"role": "user", "content": prompt}],
        api_key=OPENAI_API_KEY
    )
    
    return response["choices"][0]["message"]["content"].strip()

def add_anki_card(question, answer):
    """Creates an Anki flashcard using AnkiConnect."""
    payload = {
        "action": "addNote",
        "version": 6,
        "params": {
            "note": {
                "deckName": DECK_NAME,
                "modelName": NOTE_TYPE,
                "fields": {
                    "Front": question,
                    "Back": answer
                },
                "tags": ["AZ-400", "Study"]
            }
        }
    }
    
    response = requests.post(ANKI_CONNECT_URL, json=payload)
    return response.json()

if __name__ == "__main__":
    # Example: Paste text from Microsoft Learning Path
    study_text = """
    Azure DevOps provides developer services for support teams to plan work, collaborate on code development,
    and build and deploy applications. Developers can work in the cloud using Azure DevOps Services or on-premises
    using Azure DevOps Server. It includes CI/CD pipelines, Git repositories, Kanban boards, and testing frameworks.
    """
    
    # Summarize the text
    summary = summarize_text(study_text)
    print("Summarized Text:\n", summary)
    
    # Add to Anki as a flashcard
    response = add_anki_card("What are the key features of Azure DevOps?", summary)
    print("Anki Response:\n", response)
