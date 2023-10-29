// chatbot/static/chatbot/script.js
document.addEventListener('DOMContentLoaded', function () {
    const form = document.getElementById('message-form');
    const input = document.getElementById('message-input');
    const chatContainer = document.getElementById('chat-container');

    form.addEventListener('submit', async function (e) {
        e.preventDefault();
        const message = input.value.trim();
        if (message !== '') {
            const messageElement = document.createElement('div');
            messageElement.classList.add('message', 'user-message');
            messageElement.textContent = message;

            const timestampElement = document.createElement('span');
            timestampElement.classList.add('timestamp');
            const now = new Date();
            timestampElement.textContent = now.toLocaleString();

            messageElement.appendChild(timestampElement);
            chatContainer.appendChild(messageElement);

            // Send user message to the server
            const response = await fetch('/chatbot/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ message: message }),
            });

            const data = await response.json();

            // Update the chat interface with the bot's response
            const botResponseElement = document.createElement('div');
            botResponseElement.classList.add('message', 'bot-message');
            botResponseElement.textContent = data.bot_response;

            const botTimestampElement = document.createElement('span');
            botTimestampElement.classList.add('timestamp');
            botTimestampElement.textContent = now.toLocaleString();

            botResponseElement.appendChild(botTimestampElement);
            chatContainer.appendChild(botResponseElement);

            input.value = '';
        }
    });
});
