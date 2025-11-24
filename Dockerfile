# Simple image for running CLI (dev/testing)
FROM python:3.11-slim

WORKDIR /app

# system deps for opencv (small set)
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc libgl1 libglib2.0-0 \
 && rm -rf /var/lib/apt/lists/*

COPY pyproject.toml poetry.lock* /app/ 2>/dev/null || true

RUN pip install --no-cache-dir poetry \
 && poetry config virtualenvs.create false \
 && poetry install --no-interaction --no-ansi || true

COPY . /app

ENTRYPOINT ["python", "-m", "bsort.cli"]
