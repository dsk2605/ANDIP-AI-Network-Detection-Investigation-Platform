from pydantic import BaseModel


class SecurityRecommendation(BaseModel):
    priority: str
    message: str