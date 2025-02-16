FROM python:3.13-slim

RUN apt update && \ 
    apt install -y curl && \
    curl -sSL https://install.python-poetry.org | python3 -

ENV PATH=/root/.local/bin:$PATH

WORKDIR /app

COPY pyproject.toml poetry.lock ./

RUN poetry install --no-root --only main

COPY . .

RUN chmod +x /app/entrypoint.sh

ENTRYPOINT [ "/app/entrypoint.sh" ]
