import os
from fastapi import FastAPI
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

@app.get("/")
def read_root():
    api_key = os.getenv("MY_API_KEY", "keyMissingHaiBhaiKyaKarRahaHai?")
    env_name = os.getenv("ENVIRONMENT")
    return {
        "hello": "world",
        "apiKey": api_key,
        "environment": env_name
    }