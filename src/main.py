from fastapi import FastAPI

from src.modules.person.api.person_router import router as person_router
from src.shared.database import config

app = FastAPI()

print("Starting FastAPI application...")
print(f"DB connected: {config.db}")


@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI application!"}


app.include_router(person_router)
