from app.config.db import db
from app.models.models import Message, Funcionalidad, Expresion, HistoriaLSM, RespuestaRapida
from datetime import datetime, timezone
import random


async def get_functionalities():
    functionalities = await db.functionalities.find().to_list(length=None)
    if not functionalities:
        return []

    return [Funcionalidad(**func) for func in functionalities]

async def get_expressions():
    expressions = await db.expressions.find().to_list(length=None)
    if not expressions:
        return []

    return [Expresion(**expr) for expr in expressions]


async def get_story():
    story = await db.stories.find().to_list(length=None)
    if not story:
        return []

    return [HistoriaLSM(**item) for item in story]

async def get_quick_responses():
    quick_responses = await db.quick_responses.find().to_list(length=None)
    if not quick_responses:
        return []

    return [RespuestaRapida(**resp) for resp in quick_responses]

async def get_quick_response_by_type(response_type: str):
    response = await db.quick_responses.find({"tipo": response_type}).to_list(length=None)
    if not response:
        return None
    seleccionada = random.choice(response)
    return RespuestaRapida(**seleccionada)

async def save_message(pregunta: str, descripcion: str):
    message = Message(pregunta=pregunta, descripcion=descripcion, timestamp=datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    await db.history.insert_one(message.dict())
    return "Message saved successfully."

async def get_chatbot_history():
    messages = await db.history.find().to_list(length=None)
    if not messages:
        return []

    return [Message(**msg) for msg in messages]
#** es para tener los datos de ese diccionario como atributos del objeto ya con eso puedes acceder a los atributos de este