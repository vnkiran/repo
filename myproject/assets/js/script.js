// chatbot/static/chatbot/script.js
document.addEventListener('DOMContentLoaded', function () {
    const form = document.getElementById('message-form');
    const input = document.getElementById('message-input');
    const chatContainer = document.getElementById('chat-container');

    form.addEventListener('submit', function (e) {
        e.preventDefault();
        const message = input.value.trim();
        if (message !== '') {
            const messageElement = document.createElement('div');
            messageElement.classList.add('message');
            messageElement.textContent = message;

            const timestampElement = document.createElement('span');
            timestampElement.classList.add('timestamp');
            const now = new Date();
            timestampElement.textContent = now.toLocaleString();

            messageElement.appendChild(timestampElement);
            chatContainer.appendChild(messageElement);

            // You can add AJAX request here to save the message to the server

            input.value = '';
        }
    });
});
