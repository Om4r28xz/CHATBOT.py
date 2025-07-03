from fastapi import FastAPI
from app.routes import router
from fastapi.staticfiles import StaticFiles
from app.utils.plantillas import static_dir

app = FastAPI(title="Chatbot Lengua de Señas")
app.include_router(router.router)
app.mount("/static", StaticFiles(directory=static_dir), name="static")


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)