# frontend
FROM python:3.9-slim

WORKDIR /app

COPY . /app/.

COPY requirements.txt .

RUN pip install -r requirements.txt

EXPOSE 8501

CMD ["streamlit", "run", "app.py", "--server.port=8501"]


