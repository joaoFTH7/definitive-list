FROM python:3.11.2-alpine3.17

WORKDIR /app

ADD app/ poetry.lock pyproject.toml /app/

RUN apk update

RUN pip install poetry 

RUN poetry config virtualenvs.create false && poetry install

EXPOSE 8000

ENTRYPOINT ["uvicorn", "main:app", "--host", "0.0.0.0"]
