FROM python:3.11 AS builder

ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir --prefix=/install -r requirements.txt

COPY . /app

RUN chmod +x /app/entrypoint.sh

FROM python:3.11

ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY --from=builder /install /usr/local
COPY --from=builder /app /app

ENTRYPOINT ["/app/entrypoint.sh"]
