import uvicorn
import json
import requests
import numpy as np
import pandas as pd

from pydantic import BaseModel
from fastapi import FastAPI
from mangum import Mangum
from fastapi.middleware import Middleware
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/hello")
async def root():
    return {"message": "Hello World"}


handler = Mangum(app)