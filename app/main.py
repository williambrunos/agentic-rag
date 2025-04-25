from fastapi import FastAPI
from app.api import agent, status

def create_app() -> FastAPI:
    app = FastAPI(
        title="AI Agent Backend",
        version="0.1.0",
        description="Backend para operação do agente de IA"
    )
    # app.include_router(status.router, prefix="/api/v1")
    app.include_router(agent.router, prefix="/api/v1/agent")
    return app

app = create_app()
