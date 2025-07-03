from app.services.service import buscar_respuesta

async def get_chatbot_response(question: str) -> str:
    return await buscar_respuesta(question)
