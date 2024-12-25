# backend
FROM python:3.9-slim as backend

WORKDIR /app

COPY backend /app/.

COPY requirements.txt .

RUN pip install -r requirements.txt

CMD ["uvicorn", "backend.backend:app", "--host", "0.0.0.0", "--port", "8000"]