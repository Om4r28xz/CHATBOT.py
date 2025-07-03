const form = document.getElementById('chat-form');
const input = document.getElementById('user-input');
const chat = document.getElementById('chat');

form.addEventListener('submit', async (e) => {
  e.preventDefault();
  const question = input.value.trim();
  if (!question) return;

  // Mostrar pregunta del usuario
  const userMsg = document.createElement('div');
  userMsg.className = 'question';
  userMsg.textContent = question;
  chat.appendChild(userMsg);

  // Enviar pregunta al backend
  try {
    const res = await fetch(`/chatbot/ask?question=${encodeURIComponent(question)}`);
    const data = await res.json();

    // Mostrar respuesta
    const botMsg = document.createElement('div');
    botMsg.className = 'answer';
    botMsg.textContent = data.response;
    chat.appendChild(botMsg);
  } catch (err) {
    const errorMsg = document.createElement('div');
    errorMsg.className = 'answer';
    errorMsg.textContent = 'Error al obtener la respuesta del chatbot.';
    chat.appendChild(errorMsg);
  }

  input.value = '';
  chat.scrollTop = chat.scrollHeight;
});
