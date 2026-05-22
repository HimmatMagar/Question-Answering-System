from contextlib import asynccontextmanager
from pydantic import BaseModel
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from src.QaSys.pipeline.prediction_pipeline import PredictionPipeline

pipeline = None
@asynccontextmanager
async def lifespan(app: FastAPI):
    global pipeline
    pipeline = PredictionPipeline()   # ✅ loads once on startup
    yield
    del pipeline  

app = FastAPI(
      title="QA system",
      lifespan=lifespan
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class QuestionRequest(BaseModel):
      question: str


class AnswerResponse(BaseModel):
      question: str
      answer: str

@app.get("/")
def root():
      return {"status": "running", "model": "flan-t5-base + LoRA"}


@app.get("/health")
def health():
    return {"status": "healthy"}


@app.post("/ask", response_model=AnswerResponse)
def answer_question(request: QuestionRequest):
      if not request.question.strip():
            raise HTTPException(status_code=400, detail="Question cannot be empty")
      
      answer = pipeline.ask(request.question)
      return AnswerResponse(
            question=request.question,
            answer=answer
      )