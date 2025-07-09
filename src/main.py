from fastapi import FastAPI

from src.api import api_router, test_db_router
from src.database import config
from src.modules.person.api.person_router import router as person_router

app = FastAPI()

print("Starting FastAPI application...")
print(f"DB connected: {config.db}")


@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI application!"}


app.include_router(api_router)
app.include_router(test_db_router)
app.include_router(person_router)
