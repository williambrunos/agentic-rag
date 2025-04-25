from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from app.services.agent import alfred

router = APIRouter(tags=["agent"])

class QueryRequest(BaseModel):
    question: str

class QueryResponse(BaseModel):
    answer: str


@router.post("/query", response_model=QueryResponse)
async def query_agent(request: QueryRequest):
    """
    Endpoint to query the AI agent.
    """
    try:
        result = await alfred.run(request.question)
        chat_msg = getattr(result, "response", None)
        if chat_msg is not None:
            answer = chat_msg.content or ""
        else:
            answer = str(result)
        return QueryResponse(answer=answer)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))