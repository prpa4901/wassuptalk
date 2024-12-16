from pydantic import BaseModel
from typing import List

class MessageStr(BaseModel):
    user_input: str
    message_history: List
