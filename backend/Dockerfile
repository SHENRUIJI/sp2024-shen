FROM python:3.10-slim

WORKDIR /app

COPY . /app
# upgrade pip and install requirements
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

CMD ["python", "app.py"]