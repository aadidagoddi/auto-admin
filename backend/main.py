from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

# 1️⃣ Create the app
app = FastAPI()

# 2️⃣ Allow frontend requests (CORS)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # for now, allow all origins
    allow_methods=["*"],
    allow_headers=["*"],
)

# 3️⃣ Pydantic model for request validation
class BusinessRequest(BaseModel):
    description: str

# Optional: Pydantic model for response
class BusinessResponse(BaseModel):
    message: str
    description: str

# 4️⃣ POST endpoint to receive business descriptions
@app.post("/business")
def receive_business(req: BusinessRequest):
    return {
        "message": "Business description received",
        "description": req.description
    }

# 5️⃣ Health check endpoint
@app.get("/")
def health_check():
    return {"status": "backend running"}