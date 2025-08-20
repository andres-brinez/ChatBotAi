document.addEventListener('DOMContentLoaded', () => {
    const chatbotToggle = document.getElementById('chatbot-toggle');
    const chatbotContainer = document.getElementById('chatbot-container');
    const chatbotClose = document.getElementById('chatbot-close');
    const chatBody = document.getElementById('chatbot-body');
    const userInput = document.getElementById('user-input');
    const sendBtn = document.getElementById('send-btn');

    // Función para abrir/cerrar el chatbot
    chatbotToggle.addEventListener('click', () => {
        chatbotContainer.classList.toggle('hidden');
    });

    chatbotClose.addEventListener('click', () => {
        chatbotContainer.classList.add('hidden');
    });

    // Función para mostrar un mensaje en el chat
    function addMessage(message, sender) {
        const messageDiv = document.createElement('div');
        messageDiv.classList.add('message', sender);
        messageDiv.textContent = message;
        chatBody.appendChild(messageDiv);
        chatBody.scrollTop = chatBody.scrollHeight; // Desplazar al último mensaje
    }

   // Evento para enviar mensaje al presionar el botón o Enter
    function sendMessage() {
        const message = userInput.value.trim();
        if (message === '') return;

        addMessage(message, 'user');
        userInput.value = '';

        // Aquí es donde enviamos el mensaje al backend de Flask
        fetch('/api/chat', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ message: message })
        })
        .then(response => response.json())
        .then(data => {
            addMessage(data.response, 'ai');
        })
        .catch(error => {
            console.error('Error:', error);
            addMessage('Lo siento, ha ocurrido un error. Inténtalo de nuevo más tarde.', 'ai');
        });
    }

    sendBtn.addEventListener('click', sendMessage);
    userInput.addEventListener('keypress', (e) => {
        if (e.key === 'Enter') {
            sendMessage();
        }
    });

    // Mensaje de bienvenida inicial
    addMessage('¡Hola! Soy tu asistente. ¿En qué puedo ayudarte hoy?', 'ai');
});