FROM python:3.13-slim

RUN apt update && apt install -y curl

RUN curl -sSL https://install.python-poetry.org | python3 -

ENV PATH=/root/.local/bin:$PATH

WORKDIR /app

COPY pyproject.toml poetry.lock ./

RUN poetry install --no-root --only main

COPY ./ ./

CMD ["sh", "-c", "poetry run alembic upgrade head && poetry run python main.py"]
