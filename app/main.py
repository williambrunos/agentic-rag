from fastapi import FastAPI
from app.api import agent, status

def create_app() -> FastAPI:
    app = FastAPI(
        title="AI Agent Backend",
        version="0.0.1",
        description="A backend for an AI agent that can perform various tasks.",
    )

    app.include_router(status.router, prefix="/api/v1")
    app.include_router(agent.router, prefix="/api/v1/agent")
    return app  

app = create_app()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)