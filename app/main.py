from fastapi import FastAPI
from controllers import list_controller


app = FastAPI()

@app.get("/")
def root():
    return "Hello World!"

app.include_router(list_controller.router)
