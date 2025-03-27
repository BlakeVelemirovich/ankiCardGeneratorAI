# Anki Summarizer

## Overview
This Python script summarizes text using OpenAI's GPT API and automatically creates an Anki flashcard using AnkiConnect. It's designed for efficient note-taking, I use it to study for Azure certifications.

## Features
- Uses **OpenAI GPT-4** (or GPT-3.5) to summarize long text into concise key points.
- Adds summarized notes as flashcards to **Anki**.
- Supports **AnkiConnect**, allowing seamless integration with Anki.

## Prerequisites
### 1. Install Dependencies
Ensure you have Python installed, then install the required packages:
```sh
pip install openai requests
```

### 2. Set Up AnkiConnect
- Install **Anki** (if not already installed).
- Install the **AnkiConnect** add-on from the Anki add-ons menu.
- Keep Anki **running** while executing the script.

### 3. Get OpenAI API Key
- Sign up at [OpenAI](https://openai.com/).
- Get an API key from the OpenAI dashboard.

## Configuration
Edit the script and update the following variables:
```python
OPENAI_API_KEY = "your-openai-api-key"
DECK_NAME = "AZ-400 Study Notes"
NOTE_TYPE = "Basic"
```

## Usage
1. Run the script:
```sh
python anki_summarizer.py
```
2. Paste your text when prompted.
3. The script will:
   - Summarize the text.
   - Create a flashcard in Anki with the summarized information.
4. Open Anki and review your newly added cards!

## Example
**Input Text:**
```
Azure DevOps provides developer services for support teams to plan work, collaborate on code development,
and build and deploy applications. Developers can work in the cloud using Azure DevOps Services or on-premises
using Azure DevOps Server. It includes CI/CD pipelines, Git repositories, Kanban boards, and testing frameworks.
```

**Generated Anki Card:**
- **Front:** What are the key features of Azure DevOps?
- **Back:** Azure DevOps includes CI/CD pipelines, Git repositories, Kanban boards, and testing frameworks.

## Troubleshooting
- Ensure Anki is **running** before running the script.
- If AnkiConnect isn't working, check if it's installed and enabled in Anki.
- If OpenAI API calls fail, ensure your API key is correct and has enough quota.

## Future Enhancements
- Support for **Cloze deletion** flashcards.
- Option to **adjust summary length**.
- Markdown support for better formatting in Anki.

## License
MIT License

