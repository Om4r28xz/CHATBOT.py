from fastapi import APIRouter, Query, Request
from fastapi.responses import HTMLResponse

from app.config.db_methods import get_chatbot_history
from app.controllers import controller
from app.utils.plantillas import templates

router = APIRouter(prefix="/chatbot", tags=["Chatbot"])

@router.get("/ask") # "..." indicates that the parameter is required
async def ask(question: str = Query(..., description="Pregunta para el chatbot")):
    return {"response": await controller.get_chatbot_response(question)}

@router.get("/history")
async def history():
    historial = await get_chatbot_history()
    return {"history": [message.dict() for message in historial]}


@router.get("/", response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "title": "Chatbot"})
