FROM python:3.11-alpine AS builder

ENV PYTHONUNBUFFERED 1

WORKDIR /app

RUN apk add --no-cache gcc musl-dev python3-dev libffi-dev

COPY ./requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir --prefix=/install -r requirements.txt

COPY . /app

RUN chmod +x /app/entrypoint.sh


FROM python:3.11-alpine

ENV PYTHONUNBUFFERED 1

WORKDIR /app

RUN apk add --no-cache libffi

COPY --from=builder /install /usr/local
COPY --from=builder /app /app

# Set the entrypoint to the entrypoint.sh script
ENTRYPOINT ["/app/entrypoint.sh"]