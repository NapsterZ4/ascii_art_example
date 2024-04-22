FROM python:latest
WORKDIR app
COPY . /app
RUN pip install pillow

ENTRYPOINT ["python", "main.py"]