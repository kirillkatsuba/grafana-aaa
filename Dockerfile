FROM python:3.10-slim
WORKDIR /app
COPY ml_service.py /app/
RUN pip install fastapi uvicorn prometheus-client
CMD ["uvicorn", "ml_service:app", "--host", "0.0.0.0", "--port", "8000"]

