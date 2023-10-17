from fastapi import FastAPI
import wikipedia
from pydantic import BaseModel
app = FastAPI(
    title = "WIKI"
)

wikipedia.set_lang('ru')

@app.get('/{sents}/{words}')
def wikipage(sents:int, words: str):
    return wikipedia.summary(words, sentences=sents)

class inf(BaseModel):
    sent: int
    words: str

@app.post('/')
def new_wikipage(information: inf):
    return wikipedia.summary(information.words, sentences=information.sent)

