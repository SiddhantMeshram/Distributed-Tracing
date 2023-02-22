FROM python:3.9-slim-buster

WORKDIR /test

COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5050

CMD ["python3", "app.py"]

