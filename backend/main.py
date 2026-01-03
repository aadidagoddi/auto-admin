from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List

from database import init_db, insert_business, get_all_businesses

# --------------------
# APP SETUP
# --------------------
app = FastAPI()

# --------------------
# CORS MIDDLEWARE
# --------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],        # Development only
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --------------------
# STARTUP EVENT
# --------------------
@app.on_event("startup")
def startup_event():
    init_db()

# --------------------
# REQUEST MODEL
# --------------------
class BusinessRequest(BaseModel):
    description: str

# --------------------
# RESPONSE MODEL
# --------------------
class BusinessEntry(BaseModel):
    id: int
    description: str

# --------------------
# ROUTES
# --------------------
@app.post("/business")
def receive_business(req: BusinessRequest):
    insert_business(req.description)
    return {"message": "Business saved"}

@app.get("/businesses", response_model=List[BusinessEntry])
def list_businesses():
    return get_all_businesses()