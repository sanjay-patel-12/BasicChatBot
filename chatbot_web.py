from flask import Flask, render_template_string, request, jsonify
from datetime import datetime

app = Flask(__name__)

class SimpleChatbot:
    def __init__(self):
        self.fallback_response = "Sorry, I didn't understand that. Can you rephrase?"
        self.rules = {
            "hi": "Hello! How can I help you today?",
            "hello": "Hi there! What can I do for you?",
            "hey": "Hey! What’s up?",
            "good morning": "Good morning! How can I assist?",
            "good evening": "Good evening! How’s your day?",
            "bye": "Goodbye! Have a great day!",
            "goodbye": "See you later! Take care!",
            "how are you": "I'm just a bot, but I'm doing great! How about you?",
            "how’s it going": "All systems go here! How about you?",
            "what is your name": "I'm a simple chatbot created in Python.",
            "who are you": "I'm your friendly chatbot assistant.",
            "help": "I can chat with you about simple things. Try saying hi!",
            "thanks": "You're welcome!",
            "thank you": "My pleasure!",
            "joke": "Why did the computer show up at work late? It had a hard drive!",
            "tell me a joke": "Why don't scientists trust atoms? Because they make up everything!",
            "weather": "I don’t have weather info, but I hope it’s nice where you are!",
            "what’s up": "I’m here to chat! What’s on your mind?",
            "what’s new": "Just learning new things every day!",
            "who created you": "Sir Sanjay created me as a simple chatbot.",
            "what can you do": "I can chat with you about simple topics. Just ask!",
            "tell me about yourself": "I’m a simple chatbot designed to assist you with basic queries.",
            "tell me something interesting": "Did you know that honey never spoils? Archaeologists have found pots of honey in ancient Egyptian tombs that are over 3000 years old and still edible!",
            "tell me a fact": "Did you know that octopuses have three hearts? Two pump blood to the gills, while the third pumps it to the rest of the body.",
            "tell me a fun fact": "Bananas are berries, but strawberries aren't! It's all about the botanical definitions.",    
            "tell me a riddle": "What has keys but can't open locks? A piano!",
            "say a joke": "Why did the scarecrow win an award? Because he was outstanding in his field!",
            "tell me a story": "Once upon a time, in a land far away, there lived a chatbot who loved to chat with everyone. And they all lived happily ever after!",
            "tell me a poem": "Roses are red, violets are blue, I'm just a chatbot, but I love chatting with you!",
            "what is your favorite color": "I don't have eyes, but I think I would like blue! It's calming.",
            "what is your favorite food": "I don't eat, but I hear pizza is quite popular!",
        }

    def ask(self, user_input):
        user_input_lower = user_input.lower()
        # Dynamic time reply
        if "time" in user_input_lower:
            now = datetime.now().strftime("%H:%M:%S")
            return f"The current time is {now}"
        # Match rules
        for key in self.rules:
            if key in user_input_lower:
                return self.rules[key]
        return self.fallback_response

    def reset(self):
        pass  # no state to reset here

bot = SimpleChatbot()

HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Chatbot with Floating Icon & Animation</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0; padding: 0;
            height: 100vh;
        }
        /* Floating Chat Icon */
        #chat-icon {
            position: fixed;
            bottom: 20px;
            right: 20px;
            background: #007bff;
            width: 60px;
            height: 60px;
            border-radius: 50%;
            box-shadow: 0 4px 8px rgba(0,0,0,0.3);
            cursor: pointer;
            display: flex;
            justify-content: center;
            align-items: center;
            z-index: 1000;
            transition: background 0.3s ease;
            /* Animation */
            animation: pulse 2s infinite;
        }
        #chat-icon:hover {
            background: #0056b3;
            animation-play-state: paused; /* pause pulse on hover */
            transform: scale(1.1);
            transition: transform 0.3s ease, background 0.3s ease;
        }
        /* Pulse animation */
        @keyframes pulse {
            0%, 100% {
                box-shadow: 0 0 0 0 rgba(0, 123, 255, 0.7);
            }
            50% {
                box-shadow: 0 0 15px 10px rgba(0, 123, 255, 0);
            }
        }
        /* Chat icon SVG */
        #chat-icon svg {
            fill: white;
            width: 30px;
            height: 30px;
        }

        /* Chat Modal */
        #chat-modal {
            position: fixed;
            bottom: 90px;
            right: 20px;
            width: 320px;
            max-height: 420px;
            background: white;
            border-radius: 8px;
            box-shadow: 0 8px 24px rgba(0,0,0,0.2);
            display: none;
            flex-direction: column;
            overflow: hidden;
            z-index: 1001;
            opacity: 0;
            transform: translateY(20px);
            transition: opacity 0.3s ease, transform 0.3s ease;
        }
        /* Show modal with animation */
        #chat-modal.show {
            display: flex;
            opacity: 1;
            transform: translateY(0);
        }

        #chat-header {
            background: #007bff;
            color: white;
            padding: 12px 16px;
            font-weight: bold;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }

        #chat-header button {
            background: transparent;
            border: none;
            color: white;
            font-size: 20px;
            cursor: pointer;
            font-weight: bold;
            line-height: 1;
        }

        #chatbox {
            padding: 12px;
            height: 320px;
            overflow-y: auto;
            background: #f9f9f9;
            flex-grow: 1;
        }

        .user {
            color: #0056b3;
            font-weight: bold;
            margin-bottom: 6px;
        }

        .bot {
            color: #28a745;
            font-weight: bold;
            margin-bottom: 6px;
        }

        #chat-input-area {
            display: flex;
            border-top: 1px solid #ddd;
            padding: 8px 12px;
            background: white;
        }

        #userInput {
            flex-grow: 1;
            padding: 8px;
            font-size: 14px;
            border: 1px solid #ccc;
            border-radius: 4px;
            outline: none;
        }

        #sendBtn {
            background: #007bff;
            color: white;
            border: none;
            padding: 8px 14px;
            margin-left: 8px;
            cursor: pointer;
            border-radius: 4px;
            font-weight: bold;
            transition: background 0.3s ease;
        }

        #sendBtn:hover {
            background: #0056b3;
        }

        /* Scrollbar for chatbox */
        #chatbox::-webkit-scrollbar {
            width: 6px;
        }
        #chatbox::-webkit-scrollbar-thumb {
            background: rgba(0,0,0,0.1);
            border-radius: 3px;
        }
    </style>
</head>
<body>

<!-- Floating Chat Icon -->
<div id="chat-icon" title="Chat with us" aria-label="Open chat window" role="button" tabindex="0">
    <svg viewBox="0 0 24 24" aria-hidden="true">
        <path d="M20 2H4C2.9 2 2 2.9 2 4v14l4-4h14c1.1 0 2-0.9 2-2V4c0-1.1-0.9-2-2-2z"/>
    </svg>
</div>

<!-- Chat Modal -->
<div id="chat-modal" role="dialog" aria-modal="true" aria-labelledby="chat-header">
    <div id="chat-header">
        Chatbot
        <button id="close-btn" aria-label="Close chat">&times;</button>
    </div>
    <div id="chatbox" aria-live="polite" aria-relevant="additions"></div>
    <div id="chat-input-area">
        <input type="text" id="userInput" placeholder="Type your message..." aria-label="Chat input" />
        <button id="sendBtn" aria-label="Send message">Send</button>
    </div>
</div>

<script>
    const chatIcon = document.getElementById('chat-icon');
    const chatModal = document.getElementById('chat-modal');
    const closeBtn = document.getElementById('close-btn');
    const chatbox = document.getElementById('chatbox');
    const userInput = document.getElementById('userInput');
    const sendBtn = document.getElementById('sendBtn');

    function openChat() {
        chatModal.classList.add('show');
        userInput.focus();
    }

    function closeChat() {
        // Fade out animation using class removal and delay display:none
        chatModal.classList.remove('show');
        // After transition (300ms), hide to remove from layout
        setTimeout(() => {
            if (!chatModal.classList.contains('show')) {
                chatModal.style.display = 'none';
            }
        }, 300);
    }

    chatIcon.addEventListener('click', () => {
        chatModal.style.display = 'flex'; // show for animation
        // Small delay to trigger transition
        setTimeout(() => openChat(), 10);
    });

    closeBtn.addEventListener('click', closeChat);

    window.addEventListener('click', e => {
        if (e.target === chatModal) {
            closeChat();
        }
    });

    function appendMessage(sender, text) {
        const div = document.createElement('div');
        div.className = sender;
        div.textContent = `${sender === 'user' ? 'You' : 'Bot'}: ${text}`;
        chatbox.appendChild(div);
        chatbox.scrollTop = chatbox.scrollHeight;
    }

    function sendMessage() {
        const message = userInput.value.trim();
        if (!message) return;
        appendMessage('user', message);
        userInput.value = '';

        fetch('/ask', {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({message})
        })
        .then(response => response.json())
        .then(data => {
            appendMessage('bot', data.response);
        });
    }

    sendBtn.addEventListener('click', sendMessage);
    userInput.addEventListener('keypress', e => {
        if (e.key === 'Enter') {
            sendMessage();
        }
    });
</script>

</body>
</html>
"""

@app.route("/")
def index():
    return render_template_string(HTML_TEMPLATE)

@app.route("/ask", methods=["POST"])
def ask():
    data = request.get_json()
    user_input = data.get("message", "")
    reply = bot.ask(user_input)
    return jsonify({"response": reply})

@app.route("/reset", methods=["POST"])
def reset():
    bot.reset()
    return jsonify({"response": "Chat reset."})

if __name__ == "__main__":
    app.run(debug=True)
