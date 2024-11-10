FROM python:3.13-slim

LABEL authors="luka"

WORKDIR /app

COPY . /app

RUN python3 -m venv /env \
    && /env/bin/pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

CMD ["/env/bin/gunicorn", "--reload", "-w", "4", "-b", "0.0.0.0:8000", "main:create_app()"]
COPY docker/entrypoints/backend.sh /root
RUN chmod +x /root/backend.sh