FROM python:3.10-slim

WORKDIR /app

COPY . .

RUN pip install poetry

RUN poetry config virtualenvs.create false

RUN poetry install --no-interaction --no-ansi --no-root

CMD ["python", "hm_2/hm1.py"]
