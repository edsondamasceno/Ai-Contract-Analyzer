from celery import Celery
from app.services.parser import extract_text
from app.services.llm import generate_analysis

celery = Celery("worker", broker="redis://redis:6379/0")

@celery.task
def process_contract(file_bytes):
    text = extract_text(file_bytes)
    analysis = generate_analysis(text)
    return analysis