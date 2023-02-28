from pydantic import BaseModel


class Deck(BaseModel):
    title: str
    description: str
    card_count: int



class Cart(BaseModel):
    deck_id: int
    default_lg: str
    learning_language: str
    status: str
