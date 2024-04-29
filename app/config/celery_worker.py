from celery import Celery
from datetime import timedelta
from app.tasks.news_api import fetch_news_api

CELERY_BROKER_URL = "redis://localhost:6379/0"
CELERY_RESULT_BACKEND = "redis://localhost:6379/0"

celery = Celery(
    "worker",
    backend=CELERY_RESULT_BACKEND,
    broker=CELERY_BROKER_URL,
)


celery.conf.beat_schedule = {
    "call-api-every-minute": {
        "task": "call_api_task",
        "schedule": timedelta(minutes=1),
    }
}


@celery.task
def test_task():
    print("Test task executed")


@celery.task(name="call_api_task")
def call_api_task():
    try:
        fetch_news_api()
    except Exception as e:
        print("call_api_task| fetch_news_api", str(e))
