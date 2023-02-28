from fastapi import FastAPI
import models

fake_users = [{"name": "Анна", "age": 25, "profession": "врач"},
 {"name": "Дмитрий", "age": 32, "profession": "программист"},
 {"name": "Екатерина", "age": 41, "profession": "учитель"},
 {"name": "Иван", "age": 19, "profession": "студент"},
 {"name": "Ксения", "age": 36, "profession": "журналист"},
 {"name": "Максим", "age": 47, "profession": "бизнесмен"},
 {"name": "Надежда", "age": 29, "profession": "бухгалтер"},
 {"name": "Ольга", "age": 23, "profession": "юрист"},
 {"name": "Павел", "age": 55, "profession": "инженер"},
 {"name": "Сергей", "age": 28, "profession": "маркетолог"}]




app = FastAPI(
    title="Он вам не Anki"
)

@app.get('/')
def index():
    return 'hello world'


@app.post('/deck', response_model=models.Deck)
def post_deck(deck: models.Deck):
    return 'ok'
