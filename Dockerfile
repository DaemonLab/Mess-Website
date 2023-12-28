FROM python:3.11

ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt

RUN pip install -r requirements.txt

COPY . /app

COPY ./entrypoint.sh /app/entrypoint.sh

RUN chmod +x /app/entrypoint.sh

# Set the entrypoint to the entrypoint.sh script
ENTRYPOINT ["/app/entrypoint.sh"]