# Python Notepad Automation Bot

A Python bot to automate data entry in Notepad using pyautogui, created for the TJM Labs take-home project.

## Features

- Fetches the first 10 posts from JSONPlaceholder API.
- Automates opening Notepad, typing the post title and body.
- Saves each post as a separate .txt file in a `tjm-project` directory on the Desktop.
- Skips files that already exist to prevent errors on re-runs.

## How to Run

1. Clone the repository.
2. Create a virtual environment: `python -m venv venv`
3. Activate it: `source venv/bin/activate` (or `venv\Scripts\activate` on Windows)
4. Install dependencies: `pip install -r requirements.txt`
5. Run the script: `python notepad_bot.py`
