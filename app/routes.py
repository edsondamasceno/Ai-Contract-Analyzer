from fastapi import APIRouter, UploadFile, File
from worker.celery_worker import process_contract

router = APIRouter()

@router.post("/analyze")
async def analyze(file: UploadFile = File(...)):
    content = await file.read()
    task = process_contract.delay(content)
    return {"task_id": task.id}