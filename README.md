
---

## ⚙️ Tecnologías utilizadas

- **Backend**: [FastAPI](https://fastapi.tiangolo.com/)
- **Base de Datos**: MongoDB (usando [Motor](https://motor.readthedocs.io/en/stable/))
- **Frontend**: HTML + TailwindCSS + JavaScript
- **Pydantic**: Para validación de datos
- **Difflib / Regex**: Para comparación semántica de preguntas

---

## 🚀 Funcionalidades

- ✨ Preguntas sobre expresiones en LSM
- 📜 Historia de la LSM
- 💬 Interpretación de comandos mediante sinónimos
- 💾 Guardado automático de historial (pregunta, respuesta y timestamp)
- 📚 Visualización interactiva del historial
- 🖼️ Asociaciones con imágenes e instrucciones de señas

---

## 🧠 Lógica del Chatbot

- Normaliza la entrada (acentos, mayúsculas, símbolos).
- Reemplaza sinónimos para entender diferentes formas de preguntar.
- Busca coincidencias en:
  - Funcionalidades (cómo hacer señas)
  - Historia (datos culturales e históricos)
  - Expresiones (frases como "hola", "gracias", etc.)
- Evalúa similitud con `SequenceMatcher` (difflib).
- Responde con:
  - Respuesta exacta si la similitud > 0.8
  - Sugerencia si la similitud > 0.5
  - Mensaje de error si no se entiende la pregunta

---

## 📦 Instalación

1. Clona el repositorio:

```bash
git clone https://github.com/tu_usuario/chatbot-lsm.git
cd chatbot-lsm
