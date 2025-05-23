# AI Chatbot Web Application

A simple, interactive AI chatbot web application built with Python and Flask. The chatbot features a modern floating chat icon, animated UI, and handles basic conversational queries using rule-based logic.

## Features

- **Floating Chat Icon**: Modern, animated chat icon that opens a chat modal on click.
- **Responsive Chat UI**: Clean, accessible chat window with smooth transitions and keyboard navigation.
- **Rule-Based Chatbot**: Handles greetings, farewells, jokes, facts, and simple questions using predefined rules.
- **Dynamic Time Response**: Replies with the current server time when asked.
- **No External Dependencies**: All logic is contained in a single Python file; no database or external AI required.

## Tech Stack

- **Backend**: Python 3, Flask
- **Frontend**: HTML, CSS (inlined), JavaScript (inlined)

## How It Works

- The Flask server serves a single-page web app with a floating chat icon.
- User messages are sent to the `/ask` endpoint via AJAX.
- The backend `SimpleChatbot` class matches user input to rules and returns a response.
- The chat UI displays both user and bot messages in real time.

## Getting Started

### Prerequisites
- Python 3.x
- Flask (`pip install flask`)

### Installation & Running
1. Clone or download this repository.
2. Install Flask:
   ```powershell
   pip install flask
   ```
3. Run the application:
   ```powershell
   python chatbot_web.py
   ```
4. Open your browser and go to `http://127.0.0.1:5000/`.

## File Structure

- `chatbot_web.py` — Main application file containing Flask server, chatbot logic, and HTML/CSS/JS for the UI.
- `README.md` — Project documentation.

## Example Interactions
- **User**: Hi
  **Bot**: Hello! How can I help you today?
- **User**: Tell me a joke
  **Bot**: Why don't scientists trust atoms? Because they make up everything!
- **User**: What time is it?
  **Bot**: The current time is 14:23:10

## Customization
- To add or modify chatbot responses, edit the `rules` dictionary in `SimpleChatbot` inside `chatbot_web.py`.
- UI styles and chat behavior can be customized in the HTML template string in the same file.

## Credits
- Developed by Sanjay Patel.
GitHub - https://github.com/sanjay-patel-12

## License
This project is open source and free to use for educational and personal projects.
