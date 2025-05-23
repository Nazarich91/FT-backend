FROM python:3.10-slim-buster

RUN apt-get update && apt-get install -y \
    curl \
    postgresql-client \
    && rm -rf /var/lib/apt/lists/*

# Poetry
RUN pip install --no-cache poetry

WORKDIR /app

COPY . /app/

RUN poetry config virtualenvs.create false \
    && poetry install --only main --no-interaction --no-ansi

COPY . /app

ENV FLASK_APP=realworld.app
ENV FLASK_RUN_PORT=8080

EXPOSE 8080

CMD ["poetry", "run", "flask", "--app", "realworld.app", "run", "--host=0.0.0.0", "--port=8080"]
