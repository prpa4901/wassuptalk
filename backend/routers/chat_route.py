from fastapi import APIRouter
from backend.schemas.message_schema import MessageStr

router = APIRouter()

@router.post("/chat", response_model=dict)
def respond()

