document.addEventListener("DOMContentLoaded", () => {
  const form = document.getElementById("chat-form");
  const input = document.getElementById("user-input");
  const chat = document.getElementById("chat");
  const historyList = document.getElementById("history");

  // Mostrar mensaje en el chat
  function appendMessage(text, isUser) {
    const div = document.createElement("div");
    div.className = "flex"

    const bubble  = document.createElement("div")
    bubble.className = `chat-bubble ${isUser ? 'chat-user ml-auto' : 'chat-bot mr-auto'}`;
    bubble.textContent = text;

    div.appendChild(bubble);
    chat.appendChild(div);
    chat.scrollTop = chat.scrollHeight;
    console.log("Mensaje add:" + text)
  }

  // Cargar historial desde el backend
  async function cargarHistorial() {
  try {
    const res = await fetch("/chatbot/history");
    const data = await res.json();
    const historial = data.history || [];
    historyList.innerHTML = ""; // Limpiar

    historial.forEach(entry => {

      const li = document.createElement("li");
      li.className = "mb-2";

      // Formatear fecha
      const fecha = new Date(entry.timestamp);
      const soloFecha = fecha.toLocaleDateString();
      const soloHora = fecha.toLocaleTimeString();

      // Texto principal pregunta en negrita y azul
      const preguntaTexto = document.createElement("span");
      preguntaTexto.className = "cursor-pointer text-blue-700 hover:underline font-bold";
      preguntaTexto.innerHTML = `
        Consultaste:<strong> "${entry.pregunta}"</strong><br/>
        El: ${soloFecha}, a las: ${soloHora} ¿Quieres ver la respuesta?
      `;


      // Botón para mostrar/ocultar respuesta
      const toggleBtn = document.createElement("button");
      toggleBtn.textContent = " Ver respuesta";
      toggleBtn.className = "text-sm text-gray-600 hover:text-gray-800 ml-2";

      // Contenedor oculto para la respuesta
      const respuestaDiv = document.createElement("div");
      respuestaDiv.style.display = "none";
      respuestaDiv.className = "mt-1 ml-4 p-2 bg-blue-50 rounded border border-blue-200 text-sm text-gray-800";


      respuestaDiv.innerHTML = `
        <em>${entry.descripcion}</em><br/> 
      `;

      // Función para alternar visibilidad y setear input
      function toggleRespuesta() {
        if (respuestaDiv.style.display === "none") {
          respuestaDiv.style.display = "block";
          input.value = entry.pregunta;
        } else {
          respuestaDiv.style.display = "none";
        }
      }

      // Eventos para mostrar/ocultar
      preguntaTexto.addEventListener("click", toggleRespuesta);
      toggleBtn.addEventListener("click", toggleRespuesta);

      li.appendChild(preguntaTexto);
      li.appendChild(toggleBtn);
      li.appendChild(respuestaDiv);
      historyList.prepend(li);

    });
  } catch (error) {
    console.error("Error al cargar historial:", error);
  }
}


  // Enviar pregunta
  form.addEventListener("submit", async (e) => {
    e.preventDefault();
    const question = input.value.trim();
    if (!question) return;

    appendMessage(question, true);
    input.value = "";

    const res = await fetch(`/chatbot/ask?question=${encodeURIComponent(question)}`);
    const data = await res.json();

    appendMessage(data.response, false);
    cargarHistorial(); // Actualiza historial después de preguntar
  });

  cargarHistorial(); // Cargar historial al inicio
});
